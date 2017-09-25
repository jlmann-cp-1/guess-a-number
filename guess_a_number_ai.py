import random

# config
low = 1
high = 1000


# helper functions
def show_start_screen():
    print("**************************")
    print("*  Guess a Number A.I.!  *")
    print("**************************")

def show_credits():
    print("This awesome game was created by Coop Dogg.")
    
def get_guess(current_low, current_high):
    """
    Returns a truncated average of the current low and high
    """
    pass

def pick_number():
    """
    Ask the player to pick a number and waits until the player
    confirms they have a number by pressing enter.
    """
    pass

def check_guess(guess):
    """
    Ask the player if the computer's number was too high, too low,
    or just right.

    Returns -1 if the guess was too low
             0 if the guess was correct
             1 if the guess was too high
    """
    pass

def show_result():
    pass

def play_again():
    while True:
        decision = input("Would you like to play again? (y/n) ")

        if decision == 'y' or decision == 'yes':
            return True
        elif decision == 'n' or decision == 'no':
            return False
        else:
            print("I don't understand. Please enter 'y' or 'n'.")

def play():
    current_low = low
    current_high = high
    result = -1
    
    pick_number()
    
    while result != 0:
        guess = get_guess(current_low, current_high)

        result = check_guess(guess)

        if result == -1:
            # adjust current high
            pass
        elif result == 1:
            # adjust current low
            pass

    show_result()

# Game starts running here
show_start_screen()

playing = True

while playing:
    play()
    playing = play_again()

show_credits()



