#
# Name: Wil Wagner
# Date: 15 April 2025
# Capital Quiz Problem
# COSC 1010
#

# Import pickle
import pickle

# Constant for the number of states to quiz the user on.
NUM_QUEST = 5

# main function
def main():
    # Initialize the state_caps_dict.
    state_caps = state_caps_dict()

    # The repeat variable
    again = 'y'

    # Correct and incorrect variables
    correct = 0
    incorrect = 0

     # Continue to repeat quiz.
    while again.lower() == 'y':

        # Quiz the user.
        for count in range(NUM_QUEST):
            # Get a random entry from the dictionary.
            state, capital = state_caps.popitem()

            # Quiz the user.
            print()
            print('What is the capital of ', state, '? ', end='')
            response = input()

            # Check answer.
            if response.lower() == capital.lower():
                correct += 1
                print('Correct!')
            else:
                incorrect += 1
                print('Incorrect, sorry! The correct answer is: ', capital, '.')

        # Results.
        print()
        print('Correct results:\t', correct)
        print('Incorrect results:\t', incorrect)

        # Ask if user wishes to take the quiz again.
        print()
        print('Would you like to take the quiz again?')
        again = input('y for yes / any other for no: ')
        print()

# Build a dictionary of states and capitals.
def state_caps_dict():
    with open('state_capital.dat', 'rb') as inputfile:
        sc = pickle.load(inputfile)

    return sc

#Call the main function.
if  __name__  == '__main__':
    main()