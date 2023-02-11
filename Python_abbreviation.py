name = "Damodar Valley Corporation"
abbreviation = ""

for word in name.split():
    abbreviation += word[0]

abbreviation = abbreviation.upper()

print("Abbreviation:", abbreviation)
