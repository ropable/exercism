def convert(number):
    resp = ''
    if not number % 3:
        resp += 'Pling'
    if not number % 5:
        resp += 'Plang'
    if not number % 7:
        resp += 'Plong'
    if not resp:
        return str(number)
    return resp
