from random import randint
# randint(a,b) --> a<=N<=break

randVal = randint(0, 100)

while(True):
    guess = int(input("Please enter your guess: "))
    if guess == randVal:
        break
    elif guess < randVal:
        print("Your guess was too low...")
    else:
        print("Your guess was too high...")
print("You guessed correctly!!")
