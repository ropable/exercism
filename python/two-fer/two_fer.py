def two_fer(name=None):
    if name:
        return "One for {}, one for me.".format(name)
    else:
        return "One for you, one for me."
