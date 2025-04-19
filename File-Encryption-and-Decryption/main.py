#
# Name: Wil Wagner
# Date: 19 April 2025
# File Encryption
# COSC 1010
#

# The Decryption program is located in decyption.py. 
# The instruction said make a new program so I did.

# main function
def main():
    # Inititalize the encryption codes.
    ec = encryption()

    # Call encrypt_file to encrypt and save file.
    encrypt_file('text.txt', 'encrypted.txt', ec)

# encrypt_file function
def encrypt_file(input_file, output_file, codes):
    try:
        # Open the input_file in read only.
        file = open(input_file, 'r')
        
        # Read the file into original_text.
        original_text = file.read()
        
        # Create the encrypted_text.
        encrypted_text = ''
        
        # Iterate thru the text and substitute the encrypted
        # char for the original text.
        for char in original_text:
            encrypted_text += codes.get(char, char)
            
        # Open encrypted.txt in write more.
        encrypted_file = open(output_file, 'w')
        
        # Write the encrypted text to the file.
        encrypted_file.write(encrypted_text)
        
        # Notify the user that the process is complete.
        print('Your file has been encrypted successfully!')

    # Inform user that the file was not found.
    except FileNotFoundError:
        print('Input file not found.')

# encryption key function
def encryption():
    encrypt_codes = {
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

    # Return the encrypt_codes to main function
    return encrypt_codes

#Call the main function.
if  __name__  == '__main__':
    main()
