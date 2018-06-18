# This is a guess the number game.
import random

print('Hello. What is your name?')
name = input().title()

secretNumber = random.randint(1, 20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.')

# Ask the player to guess 6 times.
for guessesTaken in range(0, 6):
    if guessesTaken == 0: 
        print('Take a guess.')
    else:
        print('Take another guess.') 
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess

if guess == secretNumber:
    print('Good job,' + name + '. You guessed my number in ' + str(guessesTaken + 1) + ' guesses.')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.')