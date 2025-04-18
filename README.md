# 🚗 Avtonet Skraper

> ⚠️ **Opozorilo:** Ta skraper je namenjen **izključno za osebno uporabo** in **ni namenjen uporabi, ki krši pogoje storitev avto.net**.  
> Ne prevzemam **odgovornosti** za morebitne posledice, kot so **začasne ali trajne IP prepovedi** zaradi prekomernega števila zahtev.  
> **Uporabljajte na lastno odgovornost.**

## [SLO]

## O projektu

- To je moj prvi skraper, narejen za spremljanje novejših oglasov na [avto.net](https://www.avto.net/).
- Projekt **ne bo vzdrževan**, zato obstaja velika verjetnost, da bo treba **posodobiti zahtevke** za Avtonet ali Discord.

---

## Uporaba

### 1. Namestitev knjižnic

- Poskrbite, da so vse uporabljene knjižnice nameščene. 
- Namestite jih lahko ročno ali preko requirements datoteke, in sicer s komando:
- `pip install -r common/requirements.txt`

### 2. Discord Webhook

- Za obveščanje o novih oglasih, je uporabljen Discord, in sicer preko Webhook-ov. Sistem je zelo enostaven, ter deluje brez velikih zamikov.
- Za pošiljanje oglasov na Discord potrebujete **webhook URL**.

**Ustvarjanje URL-ja:**

- Webhook URL lahko pridobite iz obstoječega Discord serverja, in sicer:
- `Server settings -> Integrations -> Webhooks -> New Webhook`
- Nato izberete kanal, v katerega bodo prihajala sporočila.
- Ko dobite generiran URL, ga shranite v datoteko `config/webhook.json`:

```json
{
	"url": "webhook_url"
}
```

### 3. Konfiguracija iskanja

- V mapi config se nahajata:
- (USTVARI) `params.json`– oznake za filtriranje (npr. znamka, model, leto, cena)
  - Dodeljena je datoteka `params_example.json` z privzetimi vrednostmi.
  - Za opise ključnih parametrov, se obrnite [tukaj](./docs/search_parameters.md)
- `scheduler.json` – opcijska nastavitev za razporejanje poizvedb
- `selectors.json` – razredi HTML elementov, ki jih uporablja scraper (če Avtonet spremeni strukturo strani)
- Datoteko `config/params.json` lahko prilagodite svojim željam. Dodani so samo parametri, ki sem jih uporabljal sam.
- Če želite dodatne filtre, preverite omrežne zahteve na Avtonetu pri uporabi filtrov in ustrezne parametre vključite ročno.


## Omejitve

- Omejitve, proti zaznavi, da gre za skraper:
  - Omejena paginacija (podprto do max 3 strani)
  - Omejene znamke (do max 3)
  - Omejeno na samo en model
  - Rešljivo z ostrejšim filtrom
- Slabo dokumentirani parametri iskanja
- Projekt ne bo redno vzdrževan – posodobitve Avtoneta ali Discorda lahko povzročijo napake
- Namenjen zgolj osebni rabi, ni produkcijsko optimiziran

---

## [EN]

## About the Project

- This is my first scraper, created to monitor new listings on avto.net.
- The project **will not maintained**, so there's a high chance that requests to Avtonet or Discord will **need to be updated** in the future.

## Usage

### 1. Install Required Libraries

- Make sure all the libraries used are installed. 
- You can install them manually, or via a requirements file:
- `pip install -r common/requirements.txt`

### 2. Discord Webhook

- For notifications about new listings, I've decided to use Discord, via their channel webhooks. It's simple, and it works without major delays.
- To send listings to Discord, you’ll need a **webhook URL**.

**How to create the URL:**

- The Webhook URL can be generated for an existing Discord server:
- `Server settings -> Integrations -> Webhooks -> New Webhook`
- Select which channel should be used for the sent messages.
- Once you get the URL, place it in: `config/webhook.json`:

```json
{
	"url": "your_webhook_url"
}
```

### 3. Search Configuration

- Inside the config folder, you'll find:
- (CREATE) `params.json` – search parameters for filters (e.g. brand, model, year, price)
  - Provided example file `params_example.json` with default values.
  - To view explanation for the important parameters, check [the docs](./docs/search_parameters.md)
- `scheduler.json` – optional settings for scheduling queries
- `selectors.json` – HTML class selectors used for scraping (in case Avtonet changes their site structure)
- You can customize the config/params.json file to your preferences. Only the filters I used myself are included.
- If you want additional filters, check the network requests on Avtonet when using filters and manually include the appropriate parameters.

## Limitations

- Limits, to attempt to prevent detection as a scrapper:
  - Limited pagination (up to 3 pages)
  - Limited brand support (up to 3 brands)
  - Limited to only one model
  - This can be resolved with tighter filters. 
- Poor search parameter documentation
- The project is not maintained – updates to Avtonet or Discord may cause errors
- Intended for personal use only, not optimized for production
