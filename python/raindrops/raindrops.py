def convert(number):
    resp = ''

    # Construct the response using modulo operators.
    if number % 3 == 0:
        resp += 'Pling'
    if number % 5 == 0:
        resp += 'Plang'
    if number % 7 == 0:
        resp += 'Plong'

    # Return resp (if truthy) or number as a string.
    return resp or str(number)
