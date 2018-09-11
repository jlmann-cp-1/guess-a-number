# imports
import random

# config
low = 1
high = 20
limit = 5

# helper functions
def start_screen():
    print("***********************************")
    print("******    Guess A Number!    ******")
    print("***********************************")
    print()
    
    input("Press 'Enter' to begin")
    print()
    
def end_screen():
    print("Bye.")
    print("This awesome game was made by Coop Dogg.")

def play_again():
    while True:
        again = input("Would you like to play again? (y/n) ")

        if again == 'y':
            return True
        elif again == 'n':
            return False
        else:
            print("Invalid guess. Please enter y or n.")

def pick_number():
    print("I'm thinking of a num from " + str(low) + " to " + str(high) + ".")
    return random.randint(low, high)

def get_guess():
    while True:
        num = input("Take a guess: ")

        if num.isnumeric():
            num = int(num)
            return num
        else:
            print("Invalid guess. Please enter a number.")

def check_guess(rand, guess):
        if guess > rand:
            print("You guessed too high.")
        elif guess < rand:
            print("You guessed to low.")

        if guess == rand:
            return True
        else:
            return False
    
def show_result(got_it):
    if got_it == True:
        print("You got it!")
    else:
        print("You are such a LOSER!!!!!!!!")


def play():
    rand = pick_number()
    got_it = False
    tries = 0
    
    while got_it == False and tries < limit:
        guess = get_guess()
        got_it = check_guess(rand, guess)
        tries += 1
        
    show_result(got_it)
    
# Game starts running here
start_screen()

playing = True

while playing == True:
    play()
    playing = play_again()

end_screen()

    
