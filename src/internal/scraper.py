from playwright.async_api import async_playwright
from src.shared.config import params
from src.internal.parser import populate_data
from src.internal.data_handler import compare_data
import pandas as pd
import asyncio
from datetime import datetime
import os
from bs4 import BeautifulSoup
from src.shared.config import params, build_url, get_columns
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

            await page.goto(url, timeout=60000)
            await page.wait_for_selector("div.GO-Results-Row", timeout=15000)

            content = await page.content()
            soup = BeautifulSoup(content, "html.parser")
            for tag in soup(["script", "style"]):
                tag.decompose()
            cleaned_content = str(soup)

            return cleaned_content

    except KeyboardInterrupt:
        logger.warning("Scraping manually interrupted by user.")
        return 500
    except Exception as e:
        logger.exception("Error during scraping.")
        return 500
    finally:
        if browser:
            await browser.close()


def scrape(init=False):
    logger.info("Starting scrape process...")
    cars = pd.DataFrame(columns=get_columns())

    def run_scrape():
        return asyncio.run(scrape_with_js_and_cookies(params))

    result = run_scrape()
    if isinstance(result, int) and result in [500, 403, 404]:
        logger.error(f"Scrape failed with error code {result}, aborting.")
        return None


    try:
        cars = populate_data(result, cars)

        if init:
            os.makedirs("data", exist_ok=True)
            cars.to_csv("data/listings.csv", sep=';', index=False)
            logger.info("Initial listings saved to data/listings.csv")
        else:
            compare_data(cars)

        logger.info("Scrape complete")
        return cars

    except Exception as e:
        logger.exception("Error during data population or comparison.")
        return None