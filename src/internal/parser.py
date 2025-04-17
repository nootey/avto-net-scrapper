from datetime import datetime

from bs4 import BeautifulSoup
from src.shared.utils import extract_property, collect_car_data, format_price
import pandas as pd
from src.shared.config import get_columns, get_base_url
from src.shared.log import logger

def populate_data(html, cars):
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_='GO-Results-Row')

    logger.info(f"Found {len(results)} car listings")

    for result in results:
        data_block = extract_property(result, 'GO-Results-Top-Data', 'div')
        if data_block is None:
            data_block = extract_property(result, 'GO-Results-Data', 'div')

        data = collect_car_data(data_block) if data_block else None

        title = extract_property(result, 'GO-Results-Naziv', 'div')
        price = extract_property(result, 'GO-Results-Top-Price', 'div') or extract_property(result, 'GO-Results-Price', 'div')

        link_raw = extract_property(result, 'stretched-link', 'a')
        link = link_raw.replace("..", get_base_url()) if link_raw else None

        if data:
            row = {
                'Naziv': title,
                'Cena': format_price(price) if price else '',
                'URL': link,
                **data
            }
            data_cleaned = {col: row.get(col, None) for col in get_columns()}
            new_row = pd.DataFrame([data_cleaned])
            cars = pd.concat([cars, new_row], ignore_index=True)

    return cars
