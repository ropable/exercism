def distance(strand_a: str, strand_b: str) -> int:
    if not len(strand_a) == len(strand_b):
        raise ValueError("Input strands are not of equal length")

    strands = zip(strand_a, strand_b)
    return sum([1 for i in strands if i[0] != i[1]])
