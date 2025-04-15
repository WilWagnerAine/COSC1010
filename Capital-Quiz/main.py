#
# Name: Wil Wagner
# Date: 15 April 2025
# Capital Quiz Problem
# COSC 1010
#

# Constant for the number of states to quiz the user on.
NUM_QUEST = 5

# main function
def main():
    # Initialize the state_caps_dict.
    state_caps = state_caps_dict()

    # The repeat variable
    again = 'y'

    # Correct and incorrect variables
    correct = 0
    incorrect = 0

     # Continue to repeat quiz.
    while again.lower() == 'y':

        # Quiz the user.
        for count in range(NUM_QUEST):
            # Get a random entry from the dictionary.
            state, capital = state_caps.popitem()

            # Quiz the user.
            print()
            print('What is the capital of ', state, '? ', end='')
            response = input()

            # Check answer.
            if response.lower() == capital.lower():
                correct += 1
                print('Correct!')
            else:
                incorrect += 1
                print('Incorrect, sorry! The correct answer is: ', capital, '.')

        # Results.
        print()
        print('Correct results:\t', correct)
        print('Incorrect results:\t', incorrect)

        # Ask if user wishes to take the quiz again.
        print()
        print('Would you like to take the quiz again?')
        again = input('y for yes / any other for no: ')
        print()

# Build a dictionary of states and capitals.
def state_caps_dict():
    sc = {'Alabama' : 'Montgomery', 'Alaska' : 'Juneau',
          'Arizona' : 'Phoenix', 'Arkansas' : 'Little Rock',
          'California' : 'Sacramento', 'Colorado' : 'Denver',
          'Connecticut' : 'Hartford', 'Delaware' : 'Dover',
          'Florida' : 'Tallahassee', 'Georgia' : 'Atlanta',
          'Hawaii' : 'Honolulu', 'Idaho' : 'Boise',
          'Illinois' : 'Springfield', 'Indiana' : 'Indianapolis',
          'Iowa' : 'Des Moines', 'Kansas' : 'Topeka',
          'Kentucky' : 'Frankfort', 'Louisiana' : 'Baton Rouge',
          'Maine': 'Augusta', 'Maryland' : 'Annapolis',
          'Massachusetts' : 'Boston', 'Michigan' : 'Lansing',
          'Minnesota' : 'Saint Paul', 'Mississippi' : 'Jackson',
          'Missouri' : 'Jefferson City', 'Montana' : 'Helena',
          'Nebraska' : 'Lincoln', 'Nevada' : 'Carson City',
          'New Hampshire' : 'Concord', 'New Jersey' : 'Trenton',
          'New Mexico' : 'Santa Fe', 'New York' : 'Albany',
          'North Carolina' : 'Raleigh', 'North Dakota' : 'Bismarck',
          'Ohio' : 'Columbus', 'Oklahoma' : 'Oklahoma City',
          'Oregon' : 'Salem', 'Pennsylvania' : 'Harrisburg',
          'Rhode Island' : 'Providence', 'South Carolina' : 'Columbia',
          'South Dakota' : 'Pierre', 'Tennessee' : 'Nashville',
          'Texas' : 'Austin', 'Utah' : 'Salt Lake City',
          'Vermont' : 'Montpelier', 'Virginia' : 'Richmond',
          'Washington' : 'Olympia', 'West Virginia' : 'Charleston',
          'Wisconsin' : 'Madison', 'Wyoming' : 'Cheyenne'}

    return sc

#Call the main function.
if  __name__  == '__main__':
    main()