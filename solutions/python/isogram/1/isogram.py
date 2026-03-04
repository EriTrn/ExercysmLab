"""
abcd
"""

def is_isogram(string):
    """
    abcd
    """
    letters = [char for char in string.lower() if char.isalpha()]
    
    return len(letters) == len(set(letters))