import requests
from bs4 import BeautifulSoup

def init_results():
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
    return soup.find_all('div', class_='GO-Results-Row')

def extract_property(result, property_class):
    extract_div = result.find('div', class_=property_class)
    return extract_div.text.strip()

def collect_car_data(result):
    print(result)
    result_index = 1
    # if(result_index % 2 == 0): cars.insert()


if __name__ == '__main__':

    results = init_results()

    cars = []

    for i, result in enumerate(results):
        if i == 1:
            break
        car = []
        title = extract_property(result, 'GO-Results-Naziv')
        car_data = extract_property(result, 'GO-Results-Data')
        print(title)
        collect_car_data(car_data)
       
    