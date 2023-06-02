:warning: **Ta skraper je namenjen izključno za osebno uporabo in ni namenjen uporabi, ki krši pogoje storitev avto.net. Ne prevzemam odgovornosti za morebitne posledice, kot so začasne ali pa trajne IP prepovedi zaradi prekomernega števila zahtev. Uporabljajte na lastno odgovornost.**

# Avtonet Skraper

To je moj prvi skraper, zato funkcionalnost ni popolna. Paginacija ni implementirana, saj se je uporabljal samo za iskanje novejših oglasov.

Projekt ne bo vzdrževan, tako da obstaja velika verjetnost, da bo treba posodobiti zahtevke za Avtonet oz. za Discord.

## Uporaba

Za delovanje je potrebno namestiti knjižnice, ki so uporabljene v main.py, če še niso.

Prav tako je za delovanje potrebno pridobiti webhook naslov za discord strežnik. 

> server settings -> intergrations -> webhooks -> create -> copy URL

Za uporabo URLja ustvarite datoteko webhook.json s spodnjo strukturo:

```json
{
	"url": "url_string"
}
```

V mapi config se prav tako nahajajo konfiguracijske datoteke za parametre iskalnega niza, ter za razporejevalnik

V datoteki "config/params.json" se lahko ureja isalne parametre. Zapisani so tisti, katere sem uporabljal sam, za vrednosti dodatnih parametrov, je potrebno preverti poizvedbo z le temi in jih izločiti.