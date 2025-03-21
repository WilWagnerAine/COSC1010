#
# Name: Wil Wagner
# Date: 13 Mar 2025
# Average of Numbers
# COSC 1010
#

# main function
def main():
    # Open the file number.txt.
    with open('numbers.txt', 'r') as myfile:

        # Declare variables
        total = 0
        lines = 0
        number = 0

        # Read the first line from the file.
        line = myfile.readline()

        # If the is not an empty string, continue.
        while lines != '':
            # Add 1 to number of lines
            lines += 1
            # Place the number in line as interger in the number variable.
            number = int(line)
            # Add number variable to total variable
            total += number
            # Check for end of file for while loop.
            line = myfile.readline()

        # Calculate average.
        average = total / lines
        # Print average
        print (f'The average of the numbers in the file is: {average}.')

# Call main function
main()
