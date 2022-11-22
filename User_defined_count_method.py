def count1(ch, s):
    c = 0
    for i in s:
        if i == ch:
            c += 1
    print(ch, 'has occured', c, 'times')


s = input("Enter the string: ")
ch = input("Enter the character: ")
count1(ch, s)
