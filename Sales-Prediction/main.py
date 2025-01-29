#
# Name: Wil Wagner
# Date: 1/29/2025
# Sales_Prediction
# COSC 1010
#

# Get the total projected sales and calculate the profits

# Get the projected profits
total_sales = float(input('Enter projected sales: '))

# Calculate the projected profits as 23% of total sales.
projected_profit = total_sales * 0.23

# Display the projected profit
print('Your projected profit is $', format(projected_profit, ',.2f'))
