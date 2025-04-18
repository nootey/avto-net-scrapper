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