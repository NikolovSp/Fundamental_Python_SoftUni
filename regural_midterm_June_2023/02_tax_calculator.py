cars_to_be_taxed = input().split('>>')
# print(cars_to_be_taxed)
total_income = 0

for cars in cars_to_be_taxed:

    cars = cars.split()
    type_vehicle = cars[0]
    years = int(cars[1])
    kilometers = int(cars[2])
    # print(type_vehicle)
    current_car_income = 0
    if type_vehicle == 'family':
        current_car_income = 50
        current_car_income -= years * 5
        current_car_income += (kilometers // 3000) * 12
    elif type_vehicle == 'heavyDuty':
        current_car_income = 80
        current_car_income -= years * 8
        current_car_income += (kilometers // 9000) * 14
    elif type_vehicle == 'sports':
        current_car_income = 100
        current_car_income -= years * 9
        current_car_income += (kilometers // 2000) * 18
    else:
        print('Invalid car type.')
        continue

    print(f'A {type_vehicle} car will pay {current_car_income:.2f} euros in taxes.')
    total_income += current_car_income
print(f"The National Revenue Agency will collect {total_income:.2f} euros in taxes.")
