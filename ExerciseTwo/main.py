warehouse = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}


#Can be upgrade by while

print("Parts that are stored in warehouse: ")
print("")
for key, item in warehouse.items():
    print(f"{key} : {item}")

print("")
print("Please enter the part key: ")
input_key = input()

#User put number from console input, but there is no check if its int (isdigit())
print("")
print("Please enter the number of how many parts the customer wants to buy: ")
input_number = input()

if input_key in warehouse :
    if warehouse[input_key] < int(input_number):
        #F-string (interpolation)
        print(f"Only limited amount of parts {input_key} can be sold. ({warehouse[input_key]})")
        del warehouse[input_key]
    else: 
        print(f"Parts {input_key} can be sold.")
        warehouse[input_key] = warehouse[input_key] - int(input_number)
else:
    print(f"Parts {input_key} is not in warehouse!")

print("")
for key, item in warehouse.items():
    print(f"{key} : {item}")