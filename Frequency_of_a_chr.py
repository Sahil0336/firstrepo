text = input("Enter your string: ")
char_count = input("Enter thr character to count: ")
count = 0
for i in text:
    if i == char_count:
        count += 1
print(f"{char_count} has occured {count} times .")
