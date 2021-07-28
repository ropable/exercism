import re


def is_isogram(string: str) -> bool:
    # Remove non-letter characters from our string.
    string = re.sub('[^a-z]', '', string.lower())
    return len(string) == len(set(string))
