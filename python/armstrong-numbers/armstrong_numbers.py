def is_armstrong_number(number):
    power = len(str(number))
    total = sum([int(i) ** power for i in str(number)])
    return total == number
