**Text Encryption and Decryption Script**

This Python script is designed to encrypt and decrypt text using a substitution cipher with added complexity for obfuscation. The script can transform text into an encoded format and decode it back to its original form.

Key Features
Substitution Cipher:

The script uses predefined dictionaries (encrypt_dict and decrypt_dict) for substituting characters during the encryption and decryption processes.
Random Obfuscation:

During encryption, additional random characters are appended to the start and end of each word to further obscure the text. These characters are removed during decryption.
Reversing Strings:

The script reverses the characters in each word during both encryption and decryption to add another layer of complexity.
Input and Output:

The user is prompted to choose between encryption and decryption.
For encryption, the user provides the text to be encrypted.
For decryption, the user provides the encoded text, which is then decoded.
Functions
random_alpha(string)
Takes a string as input and appends random characters to the start and end. The string is reversed twice with new characters added each time.
Parameters:
string (str): The string to which random characters are added.
Returns:
string (str): The modified string with random characters and reversed content.
codec(diction, lis)
Substitutes characters in each word of a list based on the provided dictionary.
Parameters:
diction (dict): Dictionary used for character substitution.
lis (list): List of words to be encoded or decoded.
Returns:
lis (list): List with characters substituted according to the dictionary.
Usage
Encryption:

When prompted, enter 1 to select encryption.
Input the text you want to encrypt.
The script processes the input, obfuscates it, and displays the encrypted text.
Decryption:

When prompted, enter 2 to select decryption.
Input the encrypted text.
The script processes the encrypted text, removes obfuscation, and displays the decrypted text.
