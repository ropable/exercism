def classify(number):
    if number <= 0:
        raise ValueError("Input integer must be greater than 0")

    divisors = []
    candidate = int(number / 2)
    while candidate > 1:
        if number % candidate == 0:
            divisors.append(candidate)
        candidate -= 1

    divisors.append(candidate)  # 1 is always a divisor
    aliquot = sum(divisors)
    if aliquot == number:
        return "perfect"
    elif aliquot > number:
        return "abundant"
    else:
        return "deficient"
