def fact_numb(n):
    if n == 1:
        return n
    else:
        return n*fact_numb(n-1)


num = int(input("Enter a number: "))
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:
    print(
        f"------------\nFactorial of {num} is {fact_numb(num)}\n------------")
