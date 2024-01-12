while True:
    nominal_currency = [10, 20, 50]
    user_nominal = int(input('Enter a sum: '))

    if not str(user_nominal).isnumeric():
        print('You need enter a number')
    elif user_nominal == 0:
        print('You need to enter a sum that is more than 0')
    elif user_nominal > 800:
        print('Sorry, but the ATM will not dispense more than 800₴ at a time')
    else:
        if user_nominal <= 100:
            print(f'{user_nominal // 10} x 10₴')

        if 100 < user_nominal <= 200:
            temp = user_nominal - 100
            twenty = user_nominal - temp
            print(f'{temp // 10} x 10₴')
            print(f'{twenty // 20} x 20₴')

        if 200 < user_nominal <= 300:
            ten = user_nominal - 200
            twenty = user_nominal - ten
            print(f'{ten // 10} x 10₴')
            print(f'{twenty // 20} x 20₴')

        if 300 < user_nominal <= 400:
            ten = user_nominal - 300
            twenty = user_nominal - ten - 100
            fifty = user_nominal - ten - twenty
            print(f'{ten // 10} x 10₴')
            print(f'{twenty // 20} x 20₴')
            print(f'{fifty // 50} x 50₴')

        if 400 < user_nominal <= 500:
            ten = user_nominal - 400
            twenty = user_nominal - ten - 200
            fifty = user_nominal - ten - twenty
            print(f'{ten // 10} x 10')
            print(f'{twenty // 20} x 20')
            print(f'{fifty // 50} x 50')

        if 500 < user_nominal <= 600:
            ten = user_nominal - 500
            twenty = user_nominal - ten - 300
            fifty = user_nominal - ten - twenty
            print(f'{ten // 10} x 10')
            print(f'{twenty // 20} x 20')
            print(f'{fifty // 50} x 50')

        if 600 < user_nominal <= 700:
            ten = user_nominal - 600
            twenty = user_nominal - ten - 400
            fifty = user_nominal - ten - twenty
            print(f'{ten // 10} x 10')
            print(f'{twenty // 20} x 20')
            print(f'{fifty // 50} x 50')

        if 700 < user_nominal <= 800:
            ten = user_nominal - 700
            twenty = user_nominal - ten - 500
            fifty = user_nominal - ten - twenty
            print(f'{ten // 10} x 10')
            print(f'{twenty // 20} x 20')
            print(f'{fifty // 50} x 50')
