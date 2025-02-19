#
# Name: Wil Wagner
# Date:
# Kilometer Converter problem
# COSC 1010
#

# Named Constant
CONVERSION_FACTOR = 0.6214

# Declare variables
# No Declared variables due to the variables being local.

# The main function gets a distance in kilometers and calls
# the show_miles function to convert it.
def main():
    kilometers = 0          # Set the local initial value of kilometers to 0.
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance coverted to miles.
    show_miles(kilometers)

# The show_miles function converts the parameter km from
# kilometers to miles and displays the results.
def show_miles(km):
    miles = 0               # Set the local initial value of miles to 0.
    # Calculate miles.
    miles = km * CONVERSION_FACTOR

    # Display the miles.
    print(km, 'kilometers equals', format(miles, ',.3f'), 'miles.')

# Call the main function.
main()
