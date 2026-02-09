def square(number):
    if not 1 <= number <= 64:
        raise ValueError("square must be between 1 and 64")
        
    # formula: 2 ** (n-1)
    # square 1: 2^0 = 1
    # square 2: 2^1 = 2
    # square 64: 2^63
    return 2 ** (number - 1)
def total():
    return (2 ** 64) - 1
