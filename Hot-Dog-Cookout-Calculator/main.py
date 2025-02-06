#
# Wil Wagner
# 2/5/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Named Constants
HOT_DOGS_PER_PACKAGE = 10
HOT_DOG_BUNS_PER_PACKAGE = 8

# Local Variables
num_attending = 0       # Number of attendees
num_per_person = 0      # Number of hot dogs and buns per person
total_ = 0              # Total number of hot dogs and buns given
min_dogs = 0            # Minimum number of packages of hot dogs
min_buns = 0            # Minimum number of packages of hot dogs buns
dogs_left = 0           # Number of hot dogs left over from a package
buns_left = 0           # Number of hot dog buns left over from a package

# Get the number of people attending the cookout.
num_attending = int(input('Please enter the number of people attending: '))

# Get the number of hot dogs given to attendees.
num_per_person = int(input('Please enter the number of hot dogs per person: '))


# Calculated the total number of hot dogs and buns required.
total = num_attending * num_per_person

# Calculate the minimum number of packages of hot dogs required.
min_dogs = total // HOT_DOGS_PER_PACKAGE

# Determine if the number of people attending is is large enough to require more than one package of hot dogs.
if min_dogs > 0:
    # Calculate the number of hot dogs left over from a package, if any.
    dogs_left = total % HOT_DOGS_PER_PACKAGE

    # If there will be left overs, add an additional package of hot dogs.
    if dogs_left != 0:
        min_dogs = min_dogs + 1

# Set the minimum number of packages of hot dogs to one because the number of people attending is small enough to require only one package of hotdogs.
else:
    min_dogs = 1

# Determine the number of leftover hotdogs, if any.
dogs_left = HOT_DOGS_PER_PACKAGE * min_dogs - total

# Calculate the minimum number of packages of hot dog buns required.
min_buns = total // HOT_DOG_BUNS_PER_PACKAGE

# Determine if the number of people attending is is large enough to require more than one package of hot dogs buns.
if min_buns > 0:
    # Calculate the number of hot dogs buns left over from a package, if any.
    buns_left = total % HOT_DOG_BUNS_PER_PACKAGE

    # If there will be left overs, add an additional package of hot dog buns.
    if buns_left != 0:
        min_buns = min_buns + 1

# Set the minimum number of packages of hot dog buns to one because the number of people attending is small enough to require only one package of hot dog buns.
else:
    min_buns = 1

# Determine the number of leftover hot dogs buns, if any.
buns_left = HOT_DOG_BUNS_PER_PACKAGE * min_buns - total

# Display a minimum number of hot dogs reguired.
print('\nMinimum packages of hot dogs needed: ', min_dogs)

# Display a minimum number of hot dog buns required.
print('Minimum packages of hot dog buns needed: ', min_buns)

# Display the number of hot dog left over.
print('Hot dogs left over: ', dogs_left)

# Display the number of hot dog buns left over.
print('Hot dog buns left over: ', buns_left)
