import re


def is_valid(isbn):
    # Remove all non-numeric, non-X characters from the input string.
    accept = '0123456789X'
    isbn = ''.join(filter(lambda i: i in accept, isbn))
    # A valid input string must be nine digits, plus a one final digit or "X".
    pattern = r"^\d{9}[\d|X]$"
    if not re.match(pattern, isbn):
        return False

    total = 0
    for i in zip(isbn, [i for i in range(10, 0, -1)]):
        if i[0] == 'X':
            total += 10 * i[1]
        else:
            total += int(i[0]) * i[1]
    return total % 11 == 0
