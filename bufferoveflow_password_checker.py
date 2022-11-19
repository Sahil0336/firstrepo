l, u, p, d = 0, 0, 0, 0
s = input("Enter a password: ")
if (len(s) == 8 and s[0].isupper() == True and s[7].islower() == True):
    for i in s:
        if (i.islower()):
            l += 1
        if (i.isupper()):
            u += 1
        if (i.isdigit()):
            d += 1
        if (i == '@' or i == '$' or i == '_' or i == ','):
            p += 1
if (l >= 1 and u >= 1 and p >= 1 and d >= 1 and l+p+u+d == len(s)):
    print("\nValid password...")
else:
    print('\nInvalid password...')
