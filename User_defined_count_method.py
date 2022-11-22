def count1(ch, s):
    char_count = 0
    for i in s:
        if i == ch:
            char_count += 1
    print(ch, 'has occured', char_count, 'times')


s = input("Enter the string: ")
ch = input("Enter the character: ")
count1(ch, s)
