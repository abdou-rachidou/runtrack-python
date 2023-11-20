import string

def reversedAlphabet():
    alphabet_reverse = list(reversed(string.ascii_uppercase))
    return alphabet_reverse

print(reversedAlphabet())