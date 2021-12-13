from random import randit
# randint(a,b) --> a<=N<=break

randVal = randit.randint(0, 100)

while(True):
    guess = int(input("Please enter your guess"))
    if guess == randVal:
        break
    elif guess < randVal:
        print("Your guess was too low")
    else:
        print("Your guess was too high")
