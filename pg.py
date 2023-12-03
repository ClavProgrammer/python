warehouse = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

str = "1N4148"
warehouse.pop(str)

for klic, hodnota in warehouse.items():
    print(f"{klic} : {hodnota}")

