def fibo(a):

    if a <= 1:

        return a

    else:

        return fibo(a-1) + fibo(a-2)


num = int(input("Enter no. of terms: "))
for i in range(num):
    print(fibo(i), end=',')
