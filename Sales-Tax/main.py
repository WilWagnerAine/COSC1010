#
# Name: Wil Wagner
# Date: 1/29/2025
# Sales_Tax
# COSC 1010
#

# Set tax rates
state_sales_tax_rate = 0.05
county_sales_tax_rate = 0.025

# Get amount of purchase
purchase_amount = float(input('What is the amount of your purchase: '))

# Calculate State sales tax at 5%
state_tax = purchase_amount * state_sales_tax_rate

# Calculate County sales tax at 2.5%
county_tax = purchase_amount * county_sales_tax_rate

# Calculate the total tax
total_tax = state_tax + county_tax

# Calculate full total of sale
total = purchase_amount + total_tax

# Print the amount of sale
print('Amount of purchase: $\t', format(purchase_amount, ',.2f'))

# Print bothe the State and County tax
print('State sales tax: $\t', format(state_tax, ',.2f'))
print('County sales tax: $\t', format(county_tax, ',.2f'))

# Print Total sales tax
print('Total sales tax: $\t', format(total_tax, ',.2f'))

# Print total amount due at purchase
print('Sales Total: $\t\t', format(total, ',.2f'))
