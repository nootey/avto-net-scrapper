:warning: **Ta skraper je namenjen izključno za osebno uporabo in ni namenjen uporabi, ki krši pogoje storitev avto.net. Ne prevzemam odgovornosti za morebitne posledice, kot so začasne ali pa trajne IP prepovedi zaradi prekomernega števila zahtev. Uporabljajte na lastno odgovornost.**

# Avtonet Skraper

To je moj prvi skraper, zato funkcionalnost ni popolna. Paginacija ni implementirana, saj se je uporabljal samo za iskanje novejših oglasov.

Projekt ne bo vzdrževan, tako da obstaja velika verjetnost, da bo treba posodobiti zahtevke za Avtonet oz. za Discord.

## Uporaba

Za delovanje je potrebno namestiti knjižnice, ki so uporabljene v main.py, če še niso.

Prav tako je za delovanje potrebno povezati Discord uporabnika (ne bot-a):
v /config ustvarite discord_params.json in vnesite spodnjo json strukturo, s svojimi podatki.

Pridobite jih tako, da se v brskalniku prijavite v Discord z željenim računom in odprete Network Tools. V željen kanal napišete sporočilo, s kakršno koli vsebino, ter pridobite request v network zavihku.

```json
{
    "channel_id": "",
    "user_id": ""
}
```

V /config sta tudi json datoteki, s parametri za iskalnik avtov in za razporejevalnik.