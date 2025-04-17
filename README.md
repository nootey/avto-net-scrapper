# 🚗 Avtonet Skraper

> ⚠️ **Opozorilo:** Ta skraper je namenjen **izključno za osebno uporabo** in **ni namenjen uporabi, ki krši pogoje storitev avto.net**.  
> Ne prevzemam **odgovornosti** za morebitne posledice, kot so **začasne ali trajne IP prepovedi** zaradi prekomernega števila zahtev.  
> **Uporabljajte na lastno odgovornost.**

---

## [SLO]

## 🧰 O projektu

To je moj prvi skraper, narejen za spremljanje novejših oglasov na [avto.net](https://www.avto.net/).
Projekt **ne bo vzdrževan**, zato obstaja velika verjetnost, da bo treba **posodobiti zahtevke** za Avtonet ali Discord.

---

## 🚀 Uporaba

### 1. Namestitev knjižnic

Poskrbite, da so vse knjižnice, uporabljene v `main.py`, nameščene. Namestite jih lahko ročno ali pa ustvarite `requirements.txt`.

### 2. Discord Webhook

Za pošiljanje oglasov na Discord potrebujete **webhook URL**.

**Ustvarjanje URL-ja:**

URL shranite v datoteko `webhook.json`:

```json
{
	"url": "tvoj_webhook_url"
}
```

### 3. Konfiguracija iskanja
V mapi config se nahajata:

`params.json`– iskalni filtri (npr. znamka, model, leto, cena)

`scheduler.json` – opcijska nastavitev za razporejanje poizvedb

Datoteko config/params.json lahko prilagodite svojim željam.
Dodani so samo parametri, ki sem jih uporabljal sam.
Če želite dodatne filtre, preverite omrežne zahteve na Avtonetu pri uporabi filtrov in ustrezne parametre vključite ročno.


## Omejitve
Brez paginacije (pridobiva samo prvo stran rezultatov)

Projekt ni vzdrževan – posodobitve Avtoneta ali Discorda lahko povzročijo napake

Namenjen zgolj osebni rabi, ni produkcijsko optimiziran

---

## [EN]

# 🚗 Avtonet Scraper

> ⚠️ Warning: This scraper is intended for personal use only and must not be used in a way that violates the terms of service of avto.net.
> I do not take responsibility for any consequences, such as temporary or permanent IP bans due to excessive requests.
> Use at your own risk.

## 🧰 About the Project
This is my first scraper, created to monitor new listings on avto.net.
The project **will not maintained**, so there's a high chance that requests to Avtonet or Discord will **need to be updated** in the future.

## 🚀 Usage

### 1. Install Required Libraries

Make sure all the libraries used in main.py are installed. You can install them manually or by creating a requirements.txt file.

### 2. Discord Webhook

To send listings to Discord, you’ll need a **webhook URL**.

**How to create the URL:**

Save the URL in a file called webhook.json:

```json
{
	"url": "your_webhook_url"
}
```

### 3. Search Configuration

Inside the config folder, you'll find:

`params.json` – search filters (e.g. brand, model, year, price)

`scheduler.json` – optional settings for scheduling queries

You can customize the config/params.json file to your preferences.
Only the filters I used myself are included.
If you want additional filters, check the network requests on Avtonet when using filters and manually include the appropriate parameters.

## Limitations

No pagination (only fetches the first page of results)

The project is not maintained – updates to Avtonet or Discord may cause errors

Intended for personal use only, not optimized for production
