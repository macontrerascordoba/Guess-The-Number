import random
import os
import time

# Fuction to make sure the input is a number
def isNumber(text):
    while True:
        try:
            os.system("clear")
            print("GUESS THE NUMBER\n")
            ret = int(input(text))
        except:
            print("Please select a valid number...")
            time.sleep(2)
        else:
            return ret

os.system("clear")
print("GUESS THE NUMBER\n")

higherNumber = isNumber("Enter the highest number you want the program to consider: ")
numberToGuess = random.randint(1, higherNumber)

os.system("clear")
print("GUESS THE NUMBER\n")

inp = isNumber("Guess the number between 1 and " + str(higherNumber) + ": ")


tries = 1
while inp != numberToGuess:
    os.system("clear")
    print("GUESS THE NUMBER\n")

    if tries <= higherNumber/4:
        inp = isNumber("Guess the number between 1 and " + str(higherNumber) + "\nWrong number! Please try again: ")
        tries += 1

    elif tries <= higherNumber/2:
        inp = isNumber("Guess the number between 1 and " + str(higherNumber) + "\nCome on you can do it! Try again: ")
        tries += 1

    elif tries <= higherNumber/1.33:
        inp = isNumber("Guess the number between 1 and " + str(higherNumber) + "\nIt is really not difficult -_-. Try again: ")
        tries += 1
    
    else:
        inp = isNumber("Guess the number between 1 and " + str(higherNumber) + "\nYou should really just give up... Try again... ")
        tries += 1


if tries <= higherNumber/4:
    print("Congratulations!! The number was indeed " + str(numberToGuess))

elif tries <= higherNumber/2:
    print("Let's go! You guessed correctly")

elif tries <= higherNumber/1.33:
    print("Finally...")

else:
    print("You should never play again...")

input("\nPress Enter to exit...")
os.system("clear")