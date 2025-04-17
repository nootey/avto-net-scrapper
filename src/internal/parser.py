from bs4 import BeautifulSoup
from src.shared.utils import extract_property, collect_car_data, format_price
import pandas as pd

base_url = 'https://www.avto.net'
columns = ['URL', 'Cena', 'Naziv', '1.registracija', 'Prevoženih', 'Menjalnik','Motor']

def populate_data(html, cars):
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_='GO-Results-Row')

    for result in results:
        data = collect_car_data(extract_property(result, 'GO-Results-Top-Data', 'div'))
        if data is None:
            data = collect_car_data(extract_property(result, 'GO-Results-Data', 'div'))
        title = extract_property(result, 'GO-Results-Naziv', 'div')
        price = extract_property(result, 'GO-Results-Top-Price', 'div') or extract_property(result, 'GO-Results-Price', 'div')
        link = extract_property(result, 'stretched-link', 'a').replace("..", base_url)

        if data:
            row = {'Naziv': title, 'Cena': format_price(price) if price else '', 'URL': link, **data}
            data_cleaned = {col: row.get(col, None) for col in columns}
            new_row = pd.DataFrame([data_cleaned])
            cars = pd.concat([cars, new_row], ignore_index=True)
    return cars
