:warning: **Ta skraper je namenjen izključno za osebno uporabo in ni namenjen uporabi, ki krši pogoje storitev avto.net. Ne prevzemam odgovornosti za morebitne posledice, kot so začasne ali pa trajne IP prepovedi zaradi prekomernega števila zahtev. Uporabljajte na lastno odgovornost.**

# Avtonet Scrapper

To je moj prvi scrapper, zato funkcionalnost ni popolna. Paginacija ni implementirana, saj se je uporabljal samo za iskanje novejših oglasov.

Projekt ne bo vzdrževan, tako da obstaja velika verjetnost, da bo treba posodobiti zahtevke na avto-net oz. discord.

## Uporaba

Za delovanje je potrebno namestiti knjižnice, ki so uporabljene v main.py, če še niso.

Prav tako je za delovanje potrebno povezati Discord uporabnika (ne bot-a):
v /config ustvarite discord_params.json in vnesite spodnjo json strukturo, s svojimi podatki:

```json
{
    "channel_id": "",
    "user_id": ""
}
```

V /config sta tudi json datoteki, s parametri za iskalnik avtov in za razporejevalnik.