weight = float(input("Enter your weight: "))
unit = input(" In (K)gs or (L)bs: ")
if unit.upper() == "K":
    converted = weight * 2.205
    unit = "pounds"
elif unit.upper() == "L":
    converted = weight / 2.205
    unit = "kilos"
print("Your weight in " + unit + " Is ",str(converted))
# A simple code to convert pounds to kilos and vice versa