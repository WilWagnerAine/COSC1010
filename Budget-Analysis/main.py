#
# Name: Wil Wagner
# Date: 2/11/2025
# Budget Analysis Programming Project
# COSC 1010
#

# Declare variables
budget = 0          # Set budget to 0
expense = 1         # Set expense to other than 0, it changes after first request.
total = 0           # Set total_expense to 0

# Get users monthly budget
budget = float(input('Enter how much you have budgeted for the month: '))

# Begin while loop to get users monthly expenses and continue as long as user does not enter 0.
while expense != 0:
    # Get an expense
    expense = float(input('Enter an expense: [0 to end]: '))
    # Add user_expense to total expense
    total += expense

# Use an if-elif-else to determine if the user is over or under budget.
if total > budget:
    # Display if user is over budget and by how much.
    print('\nYour budget is: $', format(budget, ',.2f'), 'You have exceeded it by: $', format(total - budget, ',.2f'))
    # Display if user is under budget and by how much.
elif total < budget:
    print('\nYour budget is: $', format(budget, ',.2f'), 'You are under by: $', format(budget - total, ',.2f'))
else:
    print('\nYou are exactly on your budget of $', format(budget, ',.2f'))
