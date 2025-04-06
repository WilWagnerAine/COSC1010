#
# Name: Wil Wagner
# Date: 6 Apr 2025
# Vowels and Consonants
# COSC 1010
#

# main function
def main():
    # Get a string from the user.
    user_str = input('Enter a string of Characters: ')

    # Report the vowels and consonants.
    print('The string has', num_vowels(user_str), 'vowels and', num_consonants(user_str), 'consonants.')

# num_vowels function returns the number of vowels in the string.
def num_vowels(s):
    # make a list containing vowels.
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Initialize an accumulator.
    v_count = 0

    # Count the number of vowels in s.
    for ch in s:
        if ch.lower() in vowels:
            v_count += 1

    # Return the vowel count.
    return v_count

# num_consonants function returns the number of consonants in the string.
def num_consonants(s):
    # make a list containing vowels.
    vowels = ['a', 'e', 'i', 'o', 'u']

    # Initialize an accumulator.
    c_count = 0

    # Count the number of consonants in s.
    for ch in s:
        if ch.isalpha() and ch.lower() not in vowels:
            c_count += 1

    # Return the consonant count.
    return c_count

#Call the main function.
if  __name__  == '__main__':
    main()
