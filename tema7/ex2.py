#Write a program that generates a random number between 1 and 100 and lets the user guess the number.
# The program should provide feedback ("higher" or "lower") until the user guesses the correct number.
# The program should also keep track of the number of guesses it takes for the user to guess correctly.

import random

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 100)
print('Hello, ' + myName + ', I am thinking of a number between 1 and 100.')

unsuccessful_tries = 0
hint_taken = 0
while guessesTaken < 10:
    if unsuccessful_tries > 1 and hint_taken<3:
        print('Press 0 to get hint')
        need_hint = int(input())
        if need_hint == 0:
            hint_taken += 1
            guessesTaken += 1
            print('Here is hint')


    print('Take a guess.\t%d Attempts Left'%(10 - guessesTaken))
    guess = input()
    guess = int(guess)
    if guess >100 or guess<0:
        continue

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')

    if guess == number:
        break
    unsuccessful_tries+=1

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)