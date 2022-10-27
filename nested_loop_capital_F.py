#values = [5,2,5,2,2]
#for i in values:
#    print(i*'*')

# By using nested loop to print F is below
##################################################

values= [5,2,5,2,2]
for i in values:
    output = ""
    for x in range(i):
        output += "X"
    print(output)