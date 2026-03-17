"""
xxx
"""
def is_valid(isbn):
    """
    xxx
    """
    chars = isbn.replace("-", "")
    if len(chars) != 10:
        return False
    digits = []
    for digit, char in enumerate(chars):
        if char.isdigit():
            digits.append(int(char))
        elif char == 'X' and digit == 9:
            digits.append(10)
        else:
            return False
    total = sum(dig * (10 - digit) for digit, dig in enumerate(digits))
    return total % 11 == 0
