import json
import sys

# Config limits
# Change these at your own discretion.
# This is as far as I'd go, you might arouse suspicion with too many requests per scrape
MAX_PAGES = 3
MAX_BRANDS = 2
MIN_SCRAPE_INTERVAL_MINUTES = 2

with open('config/params.json') as f:
    params = json.load(f)

with open('config/webhook.json') as f:
    webhook = json.load(f)

with open('config/scheduler_params.json') as f:
    scheduler_params = json.load(f)

def get_param_limits() -> dict:
    return {"max_pages": MAX_PAGES, "max_brands": MAX_BRANDS, "min_scrape_interval_m": MIN_SCRAPE_INTERVAL_MINUTES}

def get_selectors() -> dict:
    with open('config/selectors.json') as f:
        return json.load(f)

def get_base_url():
    return 'https://www.avto.net'

def build_url(params: dict) -> str:
    sort = params.get("sort", "")
    sort_order = params.get("sort_order", "")
    presort = params.get("presort", "")
    tipsort = params.get("tipsort", "")
    page_num = params.get("stran", 1)

    return get_base_url() + f"/Ads/results.asp?znamka={params['znamka']}&model={params['model']}&modelID=&tip=&znamka2=&model2=&tip2=&znamka3=&model3=&tip3=" \
        f"&cenaMin={params['cenaMin']}&cenaMax={params['cenaMax']}&letnikMin={params['letnikMin']}&letnikMax={params['letnikMax']}" \
        f"&bencin={params['bencin']}&starost2=999&oblika={params['oblika']}&ccmMin={params['ccmMin']}&ccmMax={params['ccmMax']}&mocMin={params['mocMin']}&mocMax={params['mocMax']}" \
        f"&kmMin={params['kmMin']}&kmMax={params['kmMax']}&kwMin={params['kwMin']}&kwMax={params['kwMax']}" \
        f"&motortakt=&motorvalji=&lokacija=0&sirina=&dolzina=&dolzinaMIN=&dolzinaMAX=&nosilnostMIN=&nosilnostMAX=" \
        f"&sedezevMIN=&sedezevMAX=&lezisc=&presek=&premer=&col=&vijakov=&EToznaka=&vozilo=&airbag=&barva=&barvaint=&doseg=&BkType=&BkOkvir=&BkOkvirType=&Bk4=" \
        f"&EQ1={params['EQ1']}&EQ2={params['EQ2']}&EQ3={params['EQ3']}&EQ4={params['EQ4']}&EQ5={params['EQ5']}&EQ6={params['EQ6']}&EQ7={params['EQ7']}&EQ8={params['EQ8']}&EQ9={params['EQ9']}&EQ10={params['EQ10']}" \
        f"&KAT=1010000000&PIA=&PIAzero=&PIAOut=&PSLO=&akcija=&paketgarancije=0&broker=&prikazkategorije=&kategorija=&ONLvid=&ONLnak=&zaloga=10&arhiv=" \
        f"&presort={presort}&tipsort={tipsort}&stran={page_num}&subSORT={sort}&subTIPSORT={sort_order}&subLOCATION={params['subLOCATION']}&subSELLER=2"

def get_columns():
    return ['HASH', 'URL', 'Cena', 'Naziv', '1.registracija', 'Prevoženih', 'Menjalnik', 'Motor']

def validate_params(params: dict) -> None:
    brand = params.get("znamka")

    if isinstance(brand, list):
        if len(brand) > MAX_BRANDS:
            print(f"[ERROR] Too many brands provided. Max allowed is {MAX_BRANDS}. You gave: {len(brand)}")
            sys.exit(1)
    elif isinstance(brand, str):
        if brand == "":
            # Allow empty string → all brands
            params["znamka"] = [""]
        else:
            # Convert single string into list, for consistency
            params["znamka"] = [brand]
    else:
        print("[ERROR] 'znamka' must be either a string, an empty string, or a list of strings.")
        sys.exit(1)

    interval = scheduler_params.get("interval_minute", 1)
    if int(interval) < MIN_SCRAPE_INTERVAL_MINUTES:
        print(f"[ERROR] Scrape interval too short. Must be at least {MIN_SCRAPE_INTERVAL_MINUTES} minute(s).")
        sys.exit(1)

# Run validation on import
validate_params(params)