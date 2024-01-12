# 6.
# Написати функцію, яка буде підносити число у квадрат.
# Написати другу, яка буде перевіряти, чи є число простим.
# Потрібно видрукувати в головній програмі квадрати усіх простих чисел
# зі списку від 0 до 50 за допомогою map


def square(x):
    return x*x


def is_prime(x):
    if x == 0:
        return False

    for n in range(2, x):
        if x % n == 0:
            return False
    return True


def square_prime(x):
    if is_prime(x) == True:
        return square(x)
    else:
        return 0


def print_square_prime(x):
    if x > 0:
        print(x)


squares = map(square_prime, range(1, 51))
for x in map(print_square_prime, squares):
    pass
