import requests
from bs4 import BeautifulSoup
import json
from plyer import notification
from apscheduler.schedulers.blocking import BlockingScheduler
import pytz
import re
import pandas as pd
from discord_notify import DiscordBot
from datetime import datetime
import os
import math

base_url = 'https://www.avto.net'

def init_advanced_results(params, page):

    sort = 3
    sort_order = 'DESC'
    
    url = base_url + f"/Ads/results.asp?znamka={params['znamka']}&model={params['model']}&modelID=&tip=&znamka2=&model2=&tip2=&znamka3=&model3=&tip3=" \
        f"&cenaMin={params['cenaMin']}&cenaMax={params['cenaMax']}&letnikMin={params['letnikMin']}&letnikMax={params['letnikMax']}" \
            f"&bencin=0&starost2=999&oblika=11,%2012&ccmMin={params['ccmMin']}&ccmMax={params['ccmMax']}&mocMin={params['mocMin']}&mocMax={params['mocMax']}" \
                f"&kmMin={params['kmMin']}&kmMax={params['kmMax']}&kwMin={params['kwMin']}&kwMax={params['kwMax']}" \
                    f"&motortakt=&motorvalji=&lokacija=0&sirina=&dolzina=&dolzinaMIN=&dolzinaMAX=&nosilnostMIN=&nosilnostMAX=&lezisc=&presek=&premer=&col=&vijakov=&EToznaka=&vozilo=&airbag=&barva=&barvaint=&EQ1=1001000000&EQ2=1000000000&EQ3=1000000000&EQ4=100000000&EQ5=1000000000&EQ6=1000000000&EQ7=1100100020&EQ8=101000000&EQ9=1000000000&KAT=1010000000&PIA=&PIAzero=&PIAOut=&PSLO=&akcija=&paketgarancije=0&broker=&prikazkategorije=&kategorija=&ONLvid=&ONLnak=&zaloga=10&arhiv=" \
                        f"&presort=3&tipsort=ASC&stran={page}&subSORT={sort}&subTIPSORT={sort_order}" \
                            f"&subLOCATION={params['subLOCATION']}"

    payload={}
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'ogledov=; COOKizpis100=1; statAvtokatalog=13; statistika=ID18379680=0&ID18378880=0&ID18379557=0; model1=; datadome=5cd8DsXRvwMa0XX3-puPfc6bSSPurxX-tmksJfEXNljrFws9CIptGj1QF7Ac_dxpVfmyJJL-7SmNP-bBQZIxmaGPjny_UJ5yIUI_eLjefDBxjCBB5uGNPBBqAvlkIWen; datadome=1H9TTkHdp8F9rjUIzBch7HPfb8OHQIeK8kmEX68pKY9SsFsAwBOYql_Xv~r3Lu50S8E4nQKUJjHJWQUwM1iyTPLe5eBsoo2AlMkYLKmIOCl3ZQMH_nnHo6N0MdgVsr-k; COOKizpis100=1; ogledov=; statAvtokatalog=12',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68',
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find_all('div', class_='GO-Results-Row')

def init_top_recent_results():
    url = "https://www.avto.net/Ads/results_100.asp"

    payload={}
    headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': 'ogledov=; COOKizpis100=1; statAvtokatalog=12; statistika=ID18379557=0&ID18378880=0; datadome=~Vm5SjqHVwKNHFkc6h50OWxr9sz79ZV3hHHxqIYEEEl5YDlHz~_CZ2LXZLPTx6nZZ~V1gC1-v065M3Un8RgMgSG0_hsPun1d_8adZ~kD4JAGu6kZ2X_DxTs3hmmCzfM; datadome=1H9TTkHdp8F9rjUIzBch7HPfb8OHQIeK8kmEX68pKY9SsFsAwBOYql_Xv~r3Lu50S8E4nQKUJjHJWQUwM1iyTPLe5eBsoo2AlMkYLKmIOCl3ZQMH_nnHo6N0MdgVsr-k; COOKizpis100=1; ogledov=; statAvtokatalog=12',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    soup = BeautifulSoup(response.content, 'html.parser')
    return soup.find_all({'div': {'class': 'GO-Results-Row'}, 'a': True})

def extract_property(result, property_class, type):
    try:
        extract_elem = result.find(type, class_=property_class)
        if extract_elem is not None:
            if type == 'div':
                return extract_elem.text.strip()
            elif type == 'a':
                return extract_elem['href']
            else:
                return None
    except AttributeError:
        return None

def collect_car_data(result):
    if result is not None:
        try:
            old_data = [line.strip() for line in result.split('\n') if line.strip()]
            new_data = {}

            if len(old_data) % 2 != 0:
                old_data = old_data[:-1]

            for i in range(0, len(old_data), 2):
                if old_data[i+1] is not None: 
                    new_data[old_data[i]] = old_data[i+1]

            if len(new_data) > 0:
                return new_data
            else:
                return None

        except AttributeError:
            return None

def format_price(price):
    pattern = re.compile(r"[\d,.]+(?=\s*€)")
    match = pattern.search(price)
    return match.group(0).replace(".", "").replace(",", "")

def populate_data(results, cars):  

    for i, result in enumerate(results):
        data = collect_car_data(extract_property(result, 'GO-Results-Top-Data', 'div'))
        if data is None: data = collect_car_data(extract_property(result, 'GO-Results-Data', 'div'))
        title = extract_property(result, 'GO-Results-Naziv', 'div')
        price = extract_property(result, 'GO-Results-Top-Price', 'div')
        if price is None: price = extract_property(result, 'GO-Results-Price', 'div')
        link = extract_property(result, 'stretched-link', 'a')
        link = link.replace("..", base_url)

        if data is not None: 
            data = {'Naziv': title, **data}
            if price is not None: data = {'Cena': format_price(price), **data}
            else: data = {'Cena': '', **data}
            data = {'URL': link, **data}
            new_row = pd.DataFrame.from_dict(data, orient='index').transpose()
            cars = pd.concat([cars, new_row], ignore_index=True)
    return cars

def compare_data(new_cars):
    existing_cars = pd.read_csv('data/listings.csv', sep=';', encoding='utf-8')
    merged_cars = pd.merge(existing_cars, new_cars, on=['URL'], how='outer', indicator=True, suffixes=['_old', '_new'])
    diff = merged_cars[merged_cars['_merge'] != 'both']
    if 'right_only' in diff['_merge'].unique():
        diff = diff.drop(diff.filter(regex='_old$').columns, axis=1)
        diff = diff.rename(columns={col: col.replace('_new', '') for col in diff.columns if '_new' in col})
        diff['action'] = 'new'
    elif 'left_only' in merged_cars['_merge'].unique():
        diff = diff.drop(diff.filter(regex='_new$').columns, axis=1)
        diff = diff.rename(columns={col: col.replace('_old', '') for col in diff.columns if '_old' in col})
        diff['action'] = 'delete'
    diff = diff.drop('_merge', axis=1)
    
    if not diff.empty:
        handle_data(diff)

def handle_data(data):
    try:
        existing_cars = pd.read_csv('data/listings.csv', sep=';', encoding='utf-8').copy()
    except IOError:
        print("Error: Could not read CSV file")
        return None
        
    new_rows = data[data['action'] == 'new'].drop('action', axis=1)
    existing_cars = pd.concat([existing_cars, new_rows], ignore_index=True)

    delete_rows = data[data['action'] == 'delete']['URL']
    existing_cars = existing_cars[~existing_cars['URL'].isin(delete_rows)]
    existing_cars = existing_cars.reset_index(drop=True)
    if '0' in existing_cars.columns: existing_cars = existing_cars.drop('0', axis=1) 
    existing_cars.to_csv('data/listings.csv', sep=';', index=False, encoding='utf-8')
    if new_rows.shape[0] >= 1: send_discord_notifications(new_rows)

def send_discord_notifications(rows):
        is_nan = False
        bot = DiscordBot()
        if bot.check_auth() == 200:
            for index, row in rows.iterrows():
                print(row)
                try:
                    is_nan = math.isnan(float(row['Cena']))
                except (TypeError, ValueError):
                    is_nan = True
                
                if is_nan == True: 
                    price = ":x:"
                    title = ":interrobang:"
                else: 
                    price = str(row['Cena']) + ' €'
                    title = row['Naziv']
                
                message = ('AVTO: ' + title + '\n'
                    + 'CENA: ' + price + '\n'
                    + 'URL: ' + row['URL'])
                bot.send_message(message)
                print('Notified via Discord at: {}'.format(datetime.now()))
        else:
            send_notification()
            print('Notified via notification at: {}'.format(datetime.now()))
        
def send_notification():
    notification.notify(
        title='Nova Objava',
        message='Nov avto je bil objavljen.',
        app_name='Avto-Net Scrapper',
        timeout=10,
    )

def scrape(init = False):
    with open('config/params.json', 'r') as f:
        params = json.load(f)
    cars = pd.DataFrame()
    results = init_advanced_results(params, 1)
    cars = populate_data(results, cars)
    if init == True: 
        if not os.path.exists('data'):
            os.makedirs('data')
        cars.to_csv('data/listings.csv', sep=';', index=False, encoding='utf-8')
        print('Initial Scrape executed at {}'.format(datetime.now()))
    else: 
        print('Scrape executed at {}'.format(datetime.now()))
        compare_data(cars)

if __name__ == '__main__':

    # initial scrape
    scrape(True)

    # run scheduler
    with open('config/scheduler_params.json', 'r') as f:
        scheduler_params = json.load(f)
    
    time_zone = pytz.timezone(scheduler_params['timezone'])
    scheduler = BlockingScheduler()
    print('Scheduler started at {}'.format(datetime.now()))
    if scheduler_params['hourly'] == 1: scheduler.add_job(scrape, 'cron', hour = '*/' + scheduler_params['interval_hour'], minute=scheduler_params['start_minute'], args=[False], timezone=time_zone)
    elif scheduler_params['hourly'] == 0: scheduler.add_job(scrape, 'cron', minute='*/' + scheduler_params['interval_minute'], args=[False], timezone=time_zone)
    else: scheduler.add_job(scrape, 'cron', hour='*', minute=0, args=[False], timezone=time_zone)
    
    try:
        scheduler.start()
    except KeyboardInterrupt:
        print('Scheduler stopped manually by user at {}'.format(datetime.now()))
    except Exception as e:
        print('Scheduler stopped unexpectedly with error: {}'.format(str(e)))