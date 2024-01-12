number = int(input('Enter an even positive nymber:'))

if number % 2:
    if number > 0:
        for item in range(1, number, 2):
            string = '*' * item
            print(string.center(number))
        for item in range(number, 0, -2):
            string = '*' * item
            print(string.center(number))
    else:
        print('Number must be positive')
else:
    print('Number must be even')