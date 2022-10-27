numbers =[2, 2, 4, 6, 4, 7, 8]
uniques=[]
for i in numbers:
    if i  not in uniques:
        uniques.append(i)
print(numbers)
print(uniques)