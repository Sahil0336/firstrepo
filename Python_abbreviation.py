def fxn(text):

    output = text[0]

    for i in range(1, len(text)):

        if text[i-1] == " ":

            output += text[i]

    output = output.upper()
    return output


text_input = input("Enter your string: ")
print(fxn(text_input))
