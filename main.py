import requests
from bs4 import BeautifulSoup
import json

base_url = 'https://www.avto.net'

def init_advanced_results(params):
    
    url = url = base_url + f"/Ads/results.asp?znamka={params['znamka']}&model={params['model']}&modelID=&tip=&znamka2=&model2=&tip2=&znamka3=&model3=&tip3=" \
        f"&cenaMin={params['cenaMin']}&cenaMax={params['cenaMax']}&letnikMin={params['letnikMin']}&letnikMax={params['letnikMax']}" \
            f"&bencin=0&starost2=999&oblika=11,%2012&ccmMin=0&ccmMax=99999&mocMin=&mocMax=" \
                f"&kmMin={params['kmMin']}&kmMax={params['kmMax']}&kwMin=0&kwMax=999" \
                    f"&motortakt=&motorvalji=&lokacija=0&sirina=&dolzina=&dolzinaMIN=&dolzinaMAX=&nosilnostMIN=&nosilnostMAX=&lezisc=&presek=&premer=&col=&vijakov=&EToznaka=&vozilo=&airbag=&barva=&barvaint=&EQ1=1001000000&EQ2=1000000000&EQ3=1000000000&EQ4=100000000&EQ5=1000000000&EQ6=1000000000&EQ7=1100100020&EQ8=101000000&EQ9=1000000000&KAT=1010000000&PIA=&PIAzero=&PIAOut=&PSLO=&akcija=&paketgarancije=0&broker=&prikazkategorije=&kategorija=&ONLvid=&ONLnak=&zaloga=10&arhiv=&presort=&tipsort=&stran="

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

if __name__ == '__main__':

    with open('config/params.json', 'r') as f:
        params = json.load(f)
    
    results = init_advanced_results(params)
    cars = {}

    for i, result in enumerate(results):
        if i == 10:
            break
        title = extract_property(result, 'GO-Results-Naziv', 'div')
        data = collect_car_data(extract_property(result, 'GO-Results-Data', 'div'))
        price = extract_property(result, 'GO-Results-Price', 'div')
        link = extract_property(result, 'stretched-link', 'a')
        link = link.replace("..", base_url)

        if data is not None: 
            if price is not None: data = {'Cena': price.split('€')[0].strip() + ' €', **data}
            else: data = {'Cena': 'NEZNANA', **data}
            data = {'URL': link, **data}
            cars[title] = data

        for title, data in cars.items():
            print("TITLE: " + f"{title}:")
            print("DATA: ")
            for property, value in data.items():
                print(f"\t{property}: {value}")

       
    
