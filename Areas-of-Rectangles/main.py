#
# Name: Wil Wagner
# Date: 4 Feb 2025
# Areas of Rectangles
# COSC 1010
#

# Local Variables
length1 = 0     # Length of rectangle 1
width1 = 0      # Width of rectangle 1
length2 = 0     # Length of rectangle 2
width2 = 0      # Width of rectangle 2
area1 = 0       # Area of rectangle 1
area2 = 0       # Area of rectangle 2

# Get the length of rectangle 1.
length1 = int(input('Enter the length of rectangle 1: '))

# Get the width of rectangle 1.
width1 = int(input('Enter the width of Rectangle 1: '))

# Get the length of rectangle 2.
length2 = int(input('\nEnter the length of rectangle 2: '))

# Get the width of rectangle 2.
width2 = int(input('Enter the width of Rectangle 2: '))

# Calculate the area of rectangles 1.
area1 = length1 * width1

# Calculate the area of rectangle 2.
area2 = length2 * width2

# Determine which has the greater area.
if area1 > area2:
    # Print that rectangle 1 has the greatest area.
    print('Rectagle 1 has the greater area.')
elif area2 > area1:
    # Print that rectangle 2 has the greatest area.
    print('Rectangle 2 has the greater area.')
else:
    # Print that both rectangles are the same.
    print('Both have the same area.')
