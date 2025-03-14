#
# Name: Wil Wagner
# Date: 14 Mar 2025
# File Display
# COSC 1010
#

# main function
def main():
    # Open the file number.txt.
    with open('numbers.txt', 'r') as myfile:

        # Read the first line from the file.
        line = myfile.readline()

        # If the is not an empty string, continue.
        while line != '':
            # If converted to integer striping isn't necessary.
            # Strip the '\n' from the end (right) of field.
            line = line.rstrip('\n')
            # Print the variable line.
            print(line)
            # Check for end of file for while loop.
            line = myfile.readline()

    # Do not need to close file while using with open.

# Call main function
main()
