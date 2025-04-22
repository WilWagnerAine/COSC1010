#
# Name: Wil Wagner
# Date: 19 April 2025
# File Decryption
# COSC 1010
#

# Comment
def main():
    # Initialize the decryption codes.
    dc = decryption()

    # Call decrypt_file to decrypt and save file.
    decrypt_file('encrypted.txt', 'decrypted_file.txt', dc)

# deccrypt_file function
def decrypt_file(encrypted_file, decrypted_file, codes):
    try:
        # Open the input_file in read only.
        file = open(encrypted_file, 'r')

        # Read the file into encrypted_text.
        encrypted_text = file.read()
        
        # Create the decrypted_text.
        decrypted_text = ''

        # Iterate thru the text and substitute the decrypted
        # char for the encrypted text.
        for char in encrypted_text:
            decrypted_text += codes.get(char, char)

        # Open decrypted_file.txt in write more.
        decrypted_file = open('decrypted_file.txt', 'w')

        # Write the decrypted text to the file.
        decrypted_file.write(decrypted_text)

        # Notify the user that the process is complete.
        print('Your file has been decrypted successfully!')

    # Inform user that the file was not found.
    except FileNotFoundError:
        print('Encrypted file not found.')

# decryption key function
def decryption():
    decrypt_codes = {
        'A' : ')', 'a' : '0', 'B' : '(', 'b' : '9', 'C' : '*', 'c' : '8',\
        'D' : '&', 'd' : '7', 'E' : '^', 'e' : '6', 'F' : '%', 'f' : '5',\
        'G' : '$', 'g' : '4', 'H' : '#', 'h' : '3', 'I' : '@', 'i' : '2',\
        'J' : '!', 'j' : '2', 'K' : 'Z', 'k' : 'z', 'L' : 'Y', 'l' : 'y',\
        'M' : 'x', 'm' : 'x', 'N' : 'W', 'n' : 'w', 'O' : 'V', 'o' : 'v',\
        'P' : 'U', 'p' : 'u', 'Q' : 'T', 'q' : 't', 'R' : 'S', 'r' : 's',\
        'S' : 'R', 's' : 'r', 'T' : 'Q', 't' : 'q', 'U' : 'P', 'u' : 'p',\
        'V' : 'O', 'v' : 'o', 'W' : 'N', 'w' : 'n', 'X' : 'M', 'x' : 'm',\
        'Y' : 'L', 'y' : 'l', 'Z' : 'K', 'z' : 'k', '!' : 'J', '1' : 'j',\
        '@' : 'I', '2' : 'i', '#' : 'H', '3' : 'h', '$' : 'G', '4' : 'g',\
        '%' : 'F', '5' : 'f', '^' : 'E', '6' : 'e', '&' : 'D', '7' : 'd',\
        '*' : 'C', '8' : 'c', '(' : 'B', '9' : 'b', ')' : 'A', '0' : 'a',\
        ':' : ',', ',' : ':', '?' : '.', '.' : '?', '<' : '>', '>' : '<',\
        "'" : '"', '"' : "'", '+' : '-', '-' : '+', '=' : ';', ';' : '=',\
        '{' : '[', '[' : '{', '}' : ']', ']' : '}'
            }

    # Return the decrypt_codes to main function.
    return decrypt_codes

#Call the main function.
if  __name__  == '__main__':
    main()
