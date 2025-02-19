#
# Name: Wil Wagner
# Date:
# Program Name
# COSC 1010
#

# Comment

# Named Constant
INCHES_PER_FOOT = 12    # Constant of inches per foot.

# Declare variables
# No Declared variables due to the variables being local.

# This is the main function.
def main():
    feet = 0            # Set the local initial value of feet to 0
    # Get a number of feet from the used
    feet = int(input('Enter a number of feet: '))

    # Convert feet to inches.
    print(feet, 'equals ', feet_to_inches(feet), 'inches.')

# The feet_to_inches converts feet to inches.
def feet_to_inches(feet):
    # Return conversion feet multiplied by INCHES_PER_FOOT.
    return feet * INCHES_PER_FOOT

# Call the main function.
main()
