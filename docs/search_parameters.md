## Search field parameters 

This is a list of the most used parameters with explanations:

> Disclaimer: If you search for a specific model, only use the correct brand. Multiple brands AND multiple different models are not supported.

- Working example: znamka = \["Volkswagen"], model = \["Golf"]
- Non working example: znamka = \["Volkswagen", "Audi"], model = "Golf"
- The latter will just work for Volkswagen golfs, but it will exclude Audis ... I'd have to make a list of all brands and models, and that's just not in my interest atm.

---

- `znamka` - Brand of car ... Can be either an empty string ("") to fetch all brands, or an array of provided brands: ["Audi", "BMW"]
- `model` - Model of car ... Can be either an empty string ("") to fetch all models for each brand, or a provided model: "Golf
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

- `EQ7` - Status
  - novo, testno, rabljeno | new, test-car, used (default): 1110100120
  - novo, testno | new, test-car: 1110000120
  - novo, rabljeno | new, used: 1100100120
  - novo | new: 1100000120
  - rabljeno | used: 1000100120
  - "ne prikazi oglasov brez cene" | "don't show listings without a price": update the *seventh* value: default = on: (novo, rabljeno, testno) -> 1110100120; off: (novo, rabljeno, testno) -> 1110101120
- `bencin` - Gas
  - 0 - vsi | all (default)
  - 201 - bencinski motor | petrol
  - 202 - diesel nmotor | diesel
  - 207 - električni pogon | EV
- `EQ3` - Transmission
  - Vsi (default): 1000000000
  - 1002000000 - ročni (manual)
  - 1001000000 - avtomatski (automatic)
- `EQ1` - Climate control
  - Off (default) - 1000000000
  - Included - 1001000000
- `zaloga` - Stock
  - 10 (default) - vsi | all statuses
  - 1 - samo na zalogi | in stock
- `lokacija` - Location
  - 0 (default) - vse
  - 1 - Ljubljana
  - 2 - Maribor
  - 3 - Celje
  - 4 - Kranj
  - 5 - Gorica
  - 6 - Koper
  - 8 - Novo Mesto
  - 9 - Murska Sobota
