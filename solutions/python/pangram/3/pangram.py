"""
This module provides a utility to determine if a sentence is a pangram.

A pangram is a sentence that contains every letter of the alphabet 
at least once, such as 'The quick brown fox jumps over the lazy dog'.
"""

def is_pangram(sentence):
    """
    Determine if a sentence is a pangram.

    :param sentence: str - The sentence to check.
    :return: bool - True if the sentence is a pangram, False otherwise.
    """
    alphabet_set = {char for char in sentence.lower() if char.isalpha()}
    return len(alphabet_set) == 26