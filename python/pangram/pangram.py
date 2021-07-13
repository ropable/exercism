import string


def is_pangram(sentence):
    chars = string.ascii_lowercase
    sentence = sentence.lower()

    for letter in sentence:
        chars = chars.replace(letter, "")

    if not chars:
        return True

    return False
