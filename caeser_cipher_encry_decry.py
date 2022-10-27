#this is a code for simple encryption and decryption
print("...................................................................")
text = input("Enter your string: ")
key = 3
ch = int(input("Enter 1 for encryption and 2 for decryption below \n>"))
output = ""
if(ch==1):
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            output += chr((ord(char) + key - 65)% 26 +65)
        elif(char.islower()):
            output += chr((ord(char)+key -97)%26 + 97)
        else:
            output = ""
elif(ch==2):
    for i in range(len(text)):
        char = text[i]
        if(char.isupper()):
            output += chr((ord(char)-key -65)%26 +65)
        elif(char.islower()):
            output += chr((ord(char)-key -97)%26 +97)
        else:
            output = ""
print("Output= " + output)