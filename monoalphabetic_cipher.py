keys = {'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c', 'f': 'x', 'g': 'z', 'h': 'a', 'i': 's', 'j': 'd', 'k': 'f', 'l': 'g', 'm': 'h', 'n': 'j',
        'o': 'k', 'p': 'l', 'q': 'p', 'r': 'o', 's': 'i', 't': 'u', 'u': 'y', 'v': 't', 'w': 'r', 'x': 'e', 'y': 'w', 'z': 'q', ' ': ' ', }
reverse_keys = {}
for key, value in keys.items():
    reverse_keys[value] = key


def encrypt(yourtext):
    text = str(yourtext)
    encrypting = []
    for l in yourtext:
        encrypting.append(keys.get(l, l))
    print("Your text: ", (''.join(encrypting)))


def decipher(yourtext):
    text = str(yourtext)
    decrypted = []
    for l in yourtext:
        decrypted.append(reverse_keys.get(l, l))
    print("Your text: ", (''.join(decrypted)))


yourtext = input("Enter your text: ")
ch = int(input("Enter 1 for encrypt and 2 for decrypt: "))
if (ch == 1):
    (encrypt(yourtext))
elif (ch == 2):
    (decipher(yourtext))
