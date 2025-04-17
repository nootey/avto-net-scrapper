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
from src.shared.log import log

async def scrape_with_js_and_cookies(params):
    url = build_url(params)
    browser = None

    try:
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=False)
            page = await browser.new_page()
            log("Initial scrape successful.")

            await page.goto(url, timeout=60000)
            await page.wait_for_selector("div.GO-Results-Row", timeout=15000)

            content = await page.content()
            soup = BeautifulSoup(content, "html.parser")
            for tag in soup(["script", "style"]):
                tag.decompose()
            cleaned_content = str(soup)

            return cleaned_content

    except KeyboardInterrupt:
        print(f"\n[{datetime.now()}] Scraping manually interrupted by user")
        return 500
    except Exception as e:
        print(f"[{datetime.now()}] Error during scraping: {e}")
        return 500
    finally:
        if browser:
            await browser.close()


def scrape(init=False):
    cars = pd.DataFrame(columns=get_columns())

    def run_scrape():
        return asyncio.run(scrape_with_js_and_cookies(params))

    # Always scrape fresh page and save HTML
    result = run_scrape()
    if result in [500, 403, 404]:
        print(f"[{datetime.now()}] Scrape failed, aborting.")
        return None


    # Parse and build dataset
    cars = populate_data(result, cars)

    if init:
        os.makedirs("data", exist_ok=True)
        cars.to_csv("data/listings.csv", sep=';', index=False)
        print(f"[{datetime.now()}] Initial listings saved")
    else:
        compare_data(cars)

    print(f"[{datetime.now()}] Scrape complete")
    return cars
