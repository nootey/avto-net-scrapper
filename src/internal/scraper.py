import random

from playwright.async_api import async_playwright
from src.internal.parser import populate_data
from src.internal.data_handler import compare_data
import pandas as pd
import asyncio
import os
from bs4 import BeautifulSoup
from src.shared.config import (
    params, build_url, get_columns, get_selectors, get_param_limits
)
from src.shared.log import logger

async def scrape_with_js_and_cookies(params):
    url = build_url(params)
    browser = None

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(
                headless=True,
                args=["--disable-blink-features=AutomationControlled"]
            )
            context = await browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115 Safari/537.36")
            page = await context.new_page()

            await asyncio.sleep(random.uniform(2, 5))  # anti-bot cooldown
            await page.goto(url, timeout=60000)

            content = await page.content()

            # Check for empty result message
            if "Ni zadetkov" in content or "ni rezultatov" in content:
                logger.info(f"No results on page {params['stran']} for '{params['znamka']}' — skipping.")
                return ""

            await page.wait_for_selector("div." + get_selectors()["result_row"], timeout=15000)

            soup = BeautifulSoup(content, "html.parser")
            for tag in soup(["script", "style"]):
                tag.decompose()
            cleaned_content = str(soup)

            return cleaned_content

    except KeyboardInterrupt:
        logger.warning("Scraping manually interrupted by user.")
        return 500
    except Exception:
        logger.exception("Error during scraping.")
        return 500
    finally:
        if browser:
            await browser.close()


async def scrape_brand_with_pagination(brand: str, max_pages: int) -> pd.DataFrame:
    logger.info(f"Scraping brand: '{brand or 'ALL'}' with {max_pages} pages")
    brand_results = pd.DataFrame(columns=get_columns())

    for page in range(1, max_pages + 1):
        local_params = params.copy()
        local_params["znamka"] = brand
        local_params["stran"] = page

        logger.debug(f"Fetching page {page} for brand '{brand}'")
        result = await scrape_with_js_and_cookies(local_params)
        if isinstance(result, int):  # If 500 or error
            logger.warning(f"Skipping page {page} for '{brand}' due to error code {result}")
            continue

        page_data = populate_data(result, pd.DataFrame(columns=get_columns()))
        brand_results = pd.concat([brand_results, page_data], ignore_index=True)

    return brand_results

async def scrape(init=False):
    logger.info("Starting scrape process...")

    param_limits = get_param_limits()
    all_results = pd.DataFrame(columns=get_columns())

    for brand in params["znamka"]:
        brand_data = await scrape_brand_with_pagination(brand, param_limits["max_pages"])
        all_results = pd.concat([all_results, brand_data], ignore_index=True)

    if all_results.empty:
        logger.warning("No results fetched from any brand/page.")
        return None

    if init:
        os.makedirs("data", exist_ok=True)
        all_results.to_csv("data/listings.csv", sep=';', index=False)
        logger.info("Initial listings saved to data/listings.csv")
    else:
        compare_data(all_results)

    logger.info("Scrape complete")
    return all_results