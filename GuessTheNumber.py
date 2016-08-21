# "Guess the number" mini-project
import math
import random
import simplegui
# initialize global variables used in your code here
number_range = 100
secret_number = 0
remaining_guesses = 0
# helper function to start and restart the game
def new_game():

    global secret_number, remaining_guesses



    secret_number = random.randrange(0,number_range)
    remaining_guesses = int(math.ceil((math.log(number_range, 2))))

    print "New game. Range is from 0 to", number_range
    print "Number of remaining guesses is ", remaining_guesses
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game
    global number_range
    number_range = 100
    new_game()
    # remove this when you add your code
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game
    global number_range
    number_range = 1000
    new_game()
    pass

def input_guess(guess):
    # main game logic goes here

    global  remaining_guesses
    remaining_guesses -= 1
    print "Number of remaining guesses is", remaining_guesses
    g_number = int(guess)
    if g_number == secret_number:
        print "Correct!"
        new_game()
        return

    print "Guess was ", g_number
    if secret_number > g_number:
        print "Higher"
        return
    elif secret_number < g_number:
        print "Lower"
        return
    else:
        print "Correct"

    pass



# create frame
f = simplegui.create_frame("Guess the number", 200, 200)
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)
# register event handlers for control elements and start frame
f.start()

# call new_game
new_game()


# always remember to check your completed program against the grading rubric