# numbers = [21,55,30,12,32,46,54,31]
# value= 0
# for i in numbers:
#     if(i>value):
#         value=i
#     else:
#         value=value
# print(f"The largest number in the is: {value}")

# Another more  efficient way
numbers = [21,55,30,19,26,54,37,45]
Max = numbers[0]
for i in numbers:
    if i> Max:
        Max= i
print(f"The largest number in the list is: {Max}")
# how to comment a whole portion just press ctrl and / together