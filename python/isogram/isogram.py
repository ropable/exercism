import re


def is_isogram(string: str) -> bool:
    # Remove non-ASCII characters from our string.
    string = re.sub('[^a-z]', '', string.lower())
    seen = []
    for i in string:
        if i in seen:
            return False
        seen.append(i)
    return True
