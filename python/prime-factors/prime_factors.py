def factors(value:int) -> list[int]:
    factors = []
    factor = 2
    # Starting at 2, calculate all the factors of `value`.
    while value > 1:
        if (value / factor).is_integer():
            factors.append(factor)
            value = int(value / factor)
        else:
            factor += 1

    return factors
