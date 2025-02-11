#
# Name: Wil Wagner
# Date: 2/11/2025
# Bug Collector
# COSC 1010
#

# Set accumulator (total) to 0
total = 0

# Set day to 0
day = 0

# Set bugs to 0
bugs = 0

# For each of 7 days:
for day in range(1, 8):
    # Get number of bugs collected that day.
    bugs = int(input(f'How many bugs did you collect day {day}: '))
    # Add bugs collected to the total
    total += bugs

# Print total amount of bugs
print(f'\nYou have collected a grand total of {total} bugs')
