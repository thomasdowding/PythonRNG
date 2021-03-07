##START OF PROGRAM##

import random
number = random.randint(1, 50)
guesses = 0
game = True
print("I am thinking of a number between 1 and 50.")

while game == True:
    
    guess = input("Enter your guess here: ")
    guess = int(guess)

    if guess == number:
        guesses = guesses + 1
        print("Congratulations! You guessed my number!")
        print("You guessed my number in ", guesses, " number of guesses!")
        game = False
    
    if guess < number:
        guesses = guesses + 1
        print("Sorry, my number's higher than that!")

    if guess > number:
        guesses = guesses + 1
        print("Sorry, my number's lower than that.")

while game == False:
    end = input("Press ENTER to end.")
    game = "man"
    
##END OF PROGRAM##
