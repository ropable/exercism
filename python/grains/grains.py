def square(number: int) -> int:
    if number < 1 or number > 64:
        raise ValueError("Input number is outside allowed range")
    return 2 ** (number - 1)


def total() -> int:
    return sum([square(i) for i in range(1, 65)])
