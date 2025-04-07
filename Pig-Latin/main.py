#
# Name: Wil Wagner
# Date: 6 Apr 2025
# Pig Latin Translator Programming Project
# COSC 1010
#

# This version of a Pig Latin Translator does not deal with capitalization,
# punctuation or even moving only the consonents to the end.

# main function
def main():

    # Variable to pass to get_sentence function and handle return
    request = ''

    # The loop variable
    again = 'y'
    
    # Welcome message
    print('Welcome to the Pig Latin Translator!')
    print()

    # Continue to get translations.
    while again.lower() == 'y':

        # Get sentence to convert
        sentence = get_sentence(request)

        # Print translation to screen
        print(f'Pig Latin translation: {pig_latin_translator(sentence)}')
        print()

        # Ask if the user wishes to continue
        print('Would you like to translate another sentence:')
        again = input('y for yes / any other for no: ')
        print()


    # Good-bye message
    print('Good-bye!')

# get_sentence function
def get_sentence(request):
    
    # Request user to enter a sentence
    sentence = input('Enter a sentence to translate to pig latin: ')
    print()

    # Return to main function passing sentence
    return (sentence)

# pig_latin_translator converts each 
def pig_latin_translator(split_sentence):
    
    # Split split_sentence in to a list of words in words variable
    words = split_sentence.split()

    # Assign the tuple pig_latin_words and pig_latin_sentence
    pig_latin_words = []
    pig_latin_sentence = []

    # For loop for each word in the variable words to slice and ice
    # the first letter to the end and add 'ay'
    for word in words:
        
        # Assign to pig_latin_word from word the  second letter to end
        # + first letter + 'ay'
        pig_latin_word = word[1:] + word[0] + 'ay'
        
        # Append pig_latin_word to pig_latin_words
        pig_latin_words.append(pig_latin_word)

        # Join the words in pig_latin_words to pig_latin_sentence with a space
        pig_latin_sentence = ' '.join(pig_latin_words)

    # Return pig_latin_sentence to the main function
    return pig_latin_sentence

#Call the main function.
if  __name__  == '__main__':
    main()
