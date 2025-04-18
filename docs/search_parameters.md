## Search field parameters 

This is a list of the most used parameters with explanations:

> Disclaimer: If you search for a specific model, only use the correct brand. Multiple brands AND multiple different models are not supported.

- Working example: znamka = \["Volkswagen"], model = \["Golf"]
- Non working example: znamka = \["Volkswagen", "Audi"], model = "Golf"
- The latter will just work for Volkswagen golfs, but it will exclude Audis ... I'd have to make a list of all brands and models, and that's just not in my interest atm.

---

- `znamka` - Brand of car ... Can be either an empty string ("") to fetch all brands, or an array of provided brands: ["Audi", "BMW"]
- `model` - Model of car ... Can be either an empty string ("") to fetch all models for each brand, or an array of provided models: ["Golf"]
- `cenaMin` - Minimum wanted price
- `cenaMax` - Maximum wanted price
- `letnikMin` - Minimum wanted registration date
- `letnikMax` - Maximum wanted registration date
- `kmMin` - Minimum wanted driven range
- `kmMax` - Maximum wanted driven range
- `kwMin` - Minimum wanted engine power (HP)
- `kwMax` - Maximum wanted engine power (HP)
- `subLOCATION` - Wanted location
- `bencin` - Type of wanted fuel

---

## Value documentation

Documenting some values for *some* parameters.

- `EQ7` - Starost
  - novo, testno, rabljeno (default): 1110100120
  - novo, testno: 1110000120
  - novo, rabljeno: 1100100120
  - novo: 1100000120
  - rabljeno: 1000100120
  - ne prikazi oglasov brez cene: spremeni *sedmo* vrednost: default = on: (novo, rabljeno, testno) -> 1110100120; off: (novo, rabljeno, testno) -> 1110101120
- `bencin` - Gorivo
  - 0 - vsi (default)
  - 201 - bencinski motor
  - 202 - diesel nmotor
  - 207 - električni pogon
- `EQ3` - Menjalnik
  - Vsi (default): 1000000000
  - 1002000000 - ročni
  - 1001000000 - avtomatski
- `EQ1` - Klimatska naprava
  - Off (default) - 1000000000
  - Included - 1001000000
- `zaloga` - Zaloga ...
  - 10 (default) - vsi
  - 1 - samo na zalogi
- `lokacija` - Lokacija ...
  - 0 (default) - vse
  - 1 - Ljubljana
  - 2 - Maribor
  - 3 - Celje
  - 4 - Kranj
  - 5 - Gorica
  - 6 - Koper
  - 8 - Novo Mesto
  - 9 - Murska Sobota