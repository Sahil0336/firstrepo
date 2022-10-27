phone= input("Phone: ")
Digit_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five"
}
output =""
for i in phone:
    output += Digit_mapping.get(i, "!") + ", "
print(output)