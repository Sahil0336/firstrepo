n = int(input("Enter the number of rows: "))
for i in range(1, n+1):
    ch = 'A'
    for i in range(1, i+1):
        print(ch, end=' ')
        ch = chr(ord(ch)+1)
    print()
# A
# A B
# A B C
# A B C D
