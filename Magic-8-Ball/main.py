#
# Name: Wil Wagner
# Date: 31 Mar 2025
# Magic 8 Ball Programming Project
# COSC 1010
#

# Import Random
import random

# Main Function
def main():
    # Set local variables
    again = 'Y'
    question = ''

    # Open file 8_ball_responses.txt
    my_file = open('8_ball_responses.txt', 'r')

    # Read the file to my_list
    my_list = my_file.readlines()

    # Strip the '\n' from the end (right) of each field.
    for index in range(len(my_list)):
        my_list[index] = my_list[index].rstrip('\n')

    # Welcome the user.
    print('Welcome to the Magic 8 Ball!')

    # Ask a question and answer it.    
    while again == 'Y' or again == 'y':
        print()
        # Ask the question.
        question = input('What is your Question? ')

        # Answer the question.
        print(my_list[random.randint(0, len(my_list)-1)])

        print()
        # Ask if the user wishes to continue.
        print('Do you wish to ask another question?')
        again = input('[Y/y] for yes: ')

    # Exit message.
    print()
    print('Good-bye!')
        
main()
