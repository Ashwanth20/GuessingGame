import random

number = random.randint(1,50)
chances = 0
print("Guess A Number Between 1-50")
while chances < 5:
    player = int(input("Enter Your Guess"))
    if player == number:
        print("GG U Have Done It")
        break
    elif player < number:
        print("Ur Guess is Lesser..")
    else:
        print("Ur Guess is Higer..")
    chances += 1
if not chances < 5:
    print("Sorry Ur Guesses was Wrong, Ur Guess Was Supposed To Be", number)
