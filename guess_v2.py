# Guess (v2)
# A game where a player tries to guess a random number
#
# Jon Cooper
# September 24, 2013

import random

# config
low = 0
high = 100
limit = 7

# start the game
rand = random.randrange(low, high + 1)
print("I'm thinking of a number from 1 to 100.");

guess = -1
tries = 0;

# play the game
while guess != rand and tries < limit:
    guess = input("Take a guess: ")
    guess = int(guess)

    if guess < rand:
        print("You guessed too low.")
    elif guess > rand:
        print("You guessed too high.")

    tries = tries + 1

# end the game
if guess==rand:
    print("You got it!")
else:
    print("Sorry, the number was", rand)
