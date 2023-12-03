def get_average_temp(temp):
    average_temp = []
    for item in temp:
        average_day_temp = round(sum(item)/len(item), 3)
        average_temp.append(average_day_temp)
    return average_temp

def get_morning_temp(temp):
    morning_temp = []
    for item in temp:
        morning_temp.append(item[0])
    return morning_temp

def get_noon_and_night_temp(temp):
    noon_and_night_temp = []
    for item in temp:
        noon_and_night_temp.append([item[1], item[3]])
    return noon_and_night_temp

temp = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

average_temp = get_average_temp(temp)
print(f"Average temperatures: {average_temp}")

morning_temp = get_morning_temp(temp)
print(f"Morning temperatures: {morning_temp}")

noon_and_night_temp = get_noon_and_night_temp(temp)
print(f"Noon and night temperatures: {noon_and_night_temp}")

