secret_number = 7
guess_count = 0
guess_limit = 4 
while guess_count < guess_limit:
    guess =int(input("guess the number: "))
    guess_count += 1
    if guess == secret_number:
        
        print(f"\n**********************************************\nyou guessed right, fair enough... the secret number was {secret_number}")
        break
else:
    print("sorry you failed!...")