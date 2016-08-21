# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
# converts the string ðš—ðšŠðš–ðšŽ into a number between 0 and 4
import random
def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        return "Error: This is a wrong input!"

# converts a number in the range 0 to 4 into its corresponding
#name as a string.
def number_to_name(number):
     if number == 0:
        return "rock"
     elif number == 1:
        return "Spock"
     elif number == 2:
        return "paper"
     elif number == 3:
        return "lizard"
     elif number == 4:
        return "scissors"
     else:
        return "Error:"


def rpsls(player_choice):
    print
    print "Player chooses " + player_choice

# convert the player's choice to player_number

    player_number = name_to_number(player_choice)

# compute random guess for comp_number
    comp_number = random.randrange(0,5)

# convert comp_number to comp_choice
    comp_choice = number_to_name(comp_number)

    print "Computer chooses " + comp_choice

# compute difference of comp_number and player_number

    d = comp_number - player_number
# use if/elif/else to determine winner

    if d == 0:
        print "Player and computer tie!"
    elif d % 5 == 1 or d % 5 == 2:
        print "Computer wins!"

    else:
        print "Player wins!"




# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric

