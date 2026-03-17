def is_valid(isbn):
    chars = isbn.replace("-", "")
    if len(chars) != 10:
        return False
    digits = []
    for i, char in enumerate(chars):
        if char.isdigit():
            digits.append(int(char))
        elif char == 'X' and i == 9:
            digits.append(10)
        else:
            return False
    total = sum(d * (10 - i) for i, d in enumerate(digits))
    return total % 11 == 0
