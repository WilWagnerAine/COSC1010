#
# Name: Wil Wagner
# Date: 20 Mar 2025
# Lottery Number Generator
# COSC 1010
#

# Import the random module
import random

# Define constants
MAX_DIGITS = 7      # Max number of digits
START = 0           # Start of random number range
END = 9             # End of random number range

# main function
def main():

    # Create list
    numbers = []

    # Append random number to list
    for count in range(MAX_DIGITS):
        numbers.append(random.randint(START, END))
    
    # Display lottery numbers
    print('Here are your random lottery numbers:')
    for count in range(MAX_DIGITS):
        print(numbers[count], end=' ')
    print()

# Call main function
main()
