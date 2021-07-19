def slices(series, length):
    if length > len(series) or length <= 0:
        raise ValueError("Length must be greater than zero and equal to or less than series length")

    slices = []

    for i in range(0, (len(series) - length)+1):
        slices.append(series[i:i + length])

    return slices
