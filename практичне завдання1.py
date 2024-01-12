import math

flat = int(input('Flat number: '))
floor = int(input('Number of floor: '))
flats_on_floor = int(input('Flats on the floor: '))

entrance_has = floor * flats_on_floor

entranse_number = 0
if not flat % entrance_has:
    entranse_number += flat // entrance_has
elif flat % entrance_has:
    entranse_number += flat // entrance_has + 1

floor_number = flat // flats_on_floor

temp = entranse_number - 1
current_entranse_flats_numbers = temp * (flats_on_floor * floor)
current_floor = math.ceil((flat - current_entranse_flats_numbers) / flats_on_floor)

print(f'You need an entranse №{entranse_number}, {current_floor} floor, apartment №{flat}')
