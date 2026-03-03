def is_pangram(sentence):
    """
    Determine if a sentence is a pangram.

    A pangram is a sentence using every letter of the alphabet at least once.
    The most famous pangram in English is:
    "The quick brown fox jumps over the lazy dog"

    :param sentence: str - The sentence to check.
    :return: bool - True if the sentence is a pangram, False otherwise.
    """
    alphabet_set = {char for char in sentence.lower() if char.isalpha()}
    return len(alphabet_set) == 26
