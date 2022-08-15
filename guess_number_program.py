# This is a guess number game.
import random

print('Hello. What is your name?')
name = input()

print('Well, ' + name + ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)

#print('DEBUG: Secret number is ' + str(secretNumber))

for guessesTaken in range(1, 7):
    print('Take a guess.')
    try:
        guess = int(input())
    except ValueError:
        print('You did not enter a number, try again.')
        continue
    if guess < secretNumber:
        print('Your guess is too low.')   
    elif guess > secretNumber:
        print('Your guess is too high.')
    else: break #This condition is for the correct guess!
     
try:    
    if guess == secretNumber:
        print('Good job, ' + name + '! you guessed my number in ' +str(guessesTaken) + ' guesses.')
    else:
        print('Nope. The number I was thinking of is ' +str(secretNumber) + '.')

except NameError:
        print('You did not enter any valid numbers. Sorry we could not play today.')
