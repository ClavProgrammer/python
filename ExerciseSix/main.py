from Car import Car

first_car = Car(registration_mark="4A2 3020", car_type="Peugeot 403 Cabrio", driven_km=47534)
second_car = Car(registration_mark="1P3 4747", car_type="Škoda Octavia", driven_km=41253)

should_end = False

while(should_end == False):

    print("For end type end")
    print("Enter which car you wnat to lend: ")
    car_type = input()
    
    if car_type == "end":
        should_end = True
    else:
        if car_type == "Peugeot":
            print(first_car.get_info())
            print(first_car.lend_car())
        if car_type == "Škoda":
            print(second_car.get_info())
            print(second_car.lend_car())
        else:
            print("Please enter only Škoda or Peugeot")

