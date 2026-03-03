def is_pangram(sentence):
    alphabet_set = {char for char in sentence.lower() if char.isalpha()}
    return len(alphabet_set) == 26
