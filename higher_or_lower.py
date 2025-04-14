# Importing the random module for the random numbers
import random

# setting the 2 numbers
num_1 = random.randint(1, 100)
num_2 = random.randint(1, 100)

# making sure both numbers are not equal
def num_not_equal(num_1, num_2):
    while num_1 == num_2:
        num_2 = random.randint(1, 100)
    return num_2

# Making sure both numbers are not equal before the start of the game
num_2 = num_not_equal(num_1, num_2)

# setting guess to True, simulating an on/off switch for the game
game = True

while game:
    # Display the first number
    print(num_1)

    # User's guess
    guess = input("Higher or Lower? ")

    # The Reveal
    if (num_2 > num_1 and guess == "Higher") or (num_2 < num_1 and guess == "Lower"):
        print("Correct\n")
        num_1 = num_2
        num_2 = num_not_equal(num_1, num_2)

    else:
        print("Wrong\n")
        game = False