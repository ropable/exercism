def is_isogram(string: str) -> bool:
    # Remove spaces and hyphens from our string.
    string = string.lower().replace(" ", "").replace("-", "")
    allowed = "abcdefghijklmnopqrstuvwxyz"
    for i in string:
        if i not in allowed:  # Whoops, we must have already used this letter!
            return False
        allowed = allowed.replace(i, "")
    return True
