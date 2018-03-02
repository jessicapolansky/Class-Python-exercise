import random
luckyNumber = random.randint(1, 10)
guessTracker = []
guess = int(input("Guess my lucky number, between 1 and 10: "))
game = True
restart = True
while restart:
    restart = False
while game:
    if len(guessTracker) > 3:
        print("Too many guesses! You lose.")
        again = input("Should we play again? Y/N ").upper()
        guessTracker = []
        if again == "Y":
            restart = True
        else:
            game = False
    elif guess > 10 or guess < 1:
        guessTracker.append(guess)
        guess = int(input("I said between 1 and 10...: "))
    elif guess < luckyNumber:
        guessTracker.append(guess)
        guess = int(input("{} is too low, try again: ".format(guess)))
    elif guess > luckyNumber:
        guessTracker.append(guess)
        guess = int(input("{} is too high, try again: ".format(guess)))
    else:
        print("You guessed it! Good job.")
        game = False