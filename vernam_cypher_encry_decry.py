def vernam_encrypt(plain_text, key):
    plain_text = plain_text.replace(" ", "")
    key = key.replace(" ", "")
    plain_text = plain_text.lower()
    key = key.lower()
    if (len(plain_text) != len(key)):
        print("Lengths are different")

    else:
        cipher_text = ""
        for i in range(len(plain_text)):
            k1 = ord(plain_text[i])-97
            k2 = ord(key[i])-97
            s = chr((k1+k2) % 26+97)
            cipher_text += s
        print("Enrypted message is: ", cipher_text)


def vernam_decrypt(cipher_text, key):
    cipher_text = cipher_text.lower()
    key = key.lower()
    cipher_text = cipher_text.replace(" ", "")
    key = key.replace(" ", "")

    plain_text = ""
    for i in range(len(cipher_text)):
        k1 = ord(cipher_text[i])-97
        k2 = ord(key[i])-97
        s = chr((((k1-k2)+26) % 26)+97)
        plain_text += s
    print("Decrypted message is: ", plain_text)


plain_text = input("Enter the message: ")
key = input("Enter the key: ")
ch = int(input("Enter 1 for encryption and 2 for decryption: "))
if (ch == 1):
    vernam_encrypt(plain_text, key)
elif (ch == 2):
    vernam_decrypt(plain_text, key)
else:
    print('Invalid input: ')
