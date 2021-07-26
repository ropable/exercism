def square(number, start=1):
    if number < 1 or number > 64:
        raise ValueError("Input number is outside allowed range")
    for i in range(1, number):
        start = start * 2
    return start


def total():
    total = 0
    for i in range(1, 65):
        total += square(i)

    return total
