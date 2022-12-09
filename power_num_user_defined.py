def power_of_num(number, power):

    value = 1

    for i in range(1, power+1):

        value = value * number

    return value


number = int(input("Enter the number: "))

power = int(input("Enter power: "))

print(
    f"value of {number}  to the power {power} is  {power_of_num(number, power)}")
