print('...................................\nEnter your command down below \n')
guess =""
started = False #boolean value for status if already started or already stopped
while True:
    guess = input(">").upper()
    if guess == 'START':
        if started:
            print("Car is already started...")
        else:
            started= True
            print('your car is started ')
    elif guess == 'STOP':
        if not started:
            print("Car is already stopped...")
        else:
            started=False
            print('your car is stopped....')
    elif guess == 'EXIT':
        break
    elif guess == 'HELP':
        print('''
here's the guide for you
start - start the car 
stop - stops the car
exit - quits the game ''')
    else:
        print("sorry I didn't get that.... type 'help' for help")

