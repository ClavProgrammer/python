warehouse = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

print("Parts that are stored in warehouse: ")
print("")
for key, item in warehouse.items():
    print(f"{key} : {item}")

input_key = input("Please enter the part key: ")
input_number = input("Please enter the number of how many parts the customer wants to buy: ")

if input_key in warehouse :

    if warehouse.get(input_key) <= int(input_number):
        print(f"Only limited amount of parts {input_key} can be sold. ({warehouse.get(input_key)})")
        warehouse.pop(input_key)
    else: 
        print(f"Parts {input_key} can be sold.")
        warehouse[input_key] = warehouse[input_key] - int(input_number)
else:
    print(f"Parts {input_key} is not in warehouse!")

print("")
for key, item in warehouse.items():
    print(f"{key} : {item}")