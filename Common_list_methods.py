numbers = [6, 2, 1, 4, 5, 7, 9, 5, 4, 8]
numbers2 = numbers.copy() #copies the list
numbers.append(10) #to insert at the end of the list 
numbers.pop() # To delete last item of the list
numbers.insert(0, 11) # to insert at any given index
numbers.remove(1) #To removw a given value in the list
#print(numbers.clear())  #To clear the list doesn't take any values
numbers.sort() # sorts the list by ascending order
numbers.reverse() # make the list reverse

print(numbers2)
print(numbers)
print(f'The index of 6 is {numbers.index(6)}') # gives the position
print(50 in numbers) # gives a boolean value 
print(f'The frequency of 5 is {numbers.count(5)}') #counts frequency of the item in the list
