# numbers = [21,55,30,12,32,46,54,31]
# value= 0
# for i in numbers:
#     if(i>value):
#         value=i
#     else:
#         value=value
# print(f"The largest number in the is: {value}")

# Another more  efficient way
def find_max(numbers):
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    return max


numbers = [21, 55, 30, 19, 26, 54, 37, 45]
print(max)

# how to comment a whole portion just press ctrl and / together
