def steps(number:int) -> int:
    if number <= 0:
        raise ValueError("Input must be a positive integer")

    steps = 0
    while number != 1:
        if number % 2 == 0:
            number = int(number / 2)
        else:
            number = int(number * 3) + 1
        steps += 1

    return steps
