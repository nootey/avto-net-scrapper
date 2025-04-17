from pyppeteer import launch
from src.shared.config import params
from src.internal.parser import populate_data
from src.internal.data_handler import compare_data
import pandas as pd
import asyncio
from datetime import datetime
import os

base_url = 'https://www.avto.net'
columns = ['URL', 'Cena', 'Naziv', '1.registracija', 'Prevoženih', 'Menjalnik','Motor']
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

async def scrape_with_js_and_cookies(params):
    browser = await launch(
        headless=True,
        executablePath=CHROME_PATH,  # 👈 specify your system Chrome/Edge path here
        args=['--no-sandbox', '--disable-setuid-sandbox']
    )
    page = await browser.newPage()

    sort = 3
    sort_order = 'DESC'
    url = base_url + f"/Ads/results.asp?znamka={params['znamka']}&model={params['model']}&modelID=&tip=&znamka2=&model2=&tip2=&znamka3=&model3=&tip3=" \
        f"&cenaMin={params['cenaMin']}&cenaMax={params['cenaMax']}&letnikMin={params['letnikMin']}&letnikMax={params['letnikMax']}" \
        f"&bencin=0&starost2=999&oblika={params['oblika']},%2012&ccmMin={params['ccmMin']}&ccmMax={params['ccmMax']}&mocMin={params['mocMin']}&mocMax={params['mocMax']}" \
        f"&kmMin={params['kmMin']}&kmMax={params['kmMax']}&kwMin={params['kwMin']}&kwMax={params['kwMax']}" \
        f"&motortakt=&motorvalji=&lokacija=0&sirina=&dolzina=&dolzinaMIN=&dolzinaMAX=&nosilnostMIN=&nosilnostMAX=" \
        f"&lezisc=&presek=&premer=&col=&vijakov=&EToznaka=&vozilo=&airbag=&barva=&barvaint=" \
        f"&EQ1={params['EQ1']}&EQ2={params['EQ2']}&EQ3={params['EQ3']}&EQ4={params['EQ4']}&EQ5={params['EQ5']}&EQ6={params['EQ6']}&EQ7={params['EQ7']}&EQ8={params['EQ8']}&EQ9={params['EQ9']}" \
        f"&KAT=1010000000&PIA=&PIAzero=&PIAOut=&PSLO=&akcija=&paketgarancije=0&broker=&prikazkategorije=&kategorija=&ONLvid=&ONLnak=&zaloga=10&arhiv=" \
        f"&presort=3&tipsort=ASC&stran=1&subSORT={sort}&subTIPSORT={sort_order}" \
        f"&subLOCATION={params['subLOCATION']}"

    try:
        await page.setJavaScriptEnabled(True)
        response = await page.goto(url)
        if response.status == 200:
            content = await page.content()
        else:
            return 500
    except Exception:
        return 500
    finally:
        await browser.close()
    return content

def scrape(init=False):
    cars = pd.DataFrame(columns=columns)

    def run_scrape():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        return loop.run_until_complete(scrape_with_js_and_cookies(params))

    result = run_scrape()
    if result in [500, 403, 404]:
        return None
    cars = populate_data(result, cars)

    if init:
        os.makedirs('data', exist_ok=True)
        cars.to_csv('data/listings.csv', sep=';', index=False)
    else:
        compare_data(cars)
    print(f"Scrape completed at {datetime.now()}")
    return cars
