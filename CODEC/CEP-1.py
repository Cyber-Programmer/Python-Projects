import random

encrypt_dict = {"a": "j", "b": "e", "c": "x", "d": "q", "e": "a", "f": "t", "g": "z", "h": "w", "i": "b", "j": "r", "k": "s", "l": "c", "m": "u", "n": "d", "o": "h", "p": "f", "q": "k", "r": "v", "s": "m", "t": "y", "u": "o", "v": "i", "w": "g", "x": "n", "y": "p", "z": "l", 'A': 'J', 'B': 'E', 'C': 'X', 'D': 'Q', 'E': 'A', 'F': 'T', 'G': 'Z', 'H': 'W', 'I': 'B', 'J': 'R', 'K': 'S', 'L': 'C', 'M': 'U', 'N': 'D', 'O': 'H', 'P': 'F', 'Q': 'K', 'R': 'V', 'S': 'M', 'T': 'Y', 'U': 'O', 'V': 'I', 'W': 'G', 'X': 'N', 'Y': 'P', 'Z': 'L', '.': '`', ',':'='}
decrypt_dict = {'j': 'a', 'e': 'b', 'x': 'c', 'q': 'd', 'a': 'e', 't': 'f', 'z': 'g', 'w': 'h', 'b': 'i', 'r': 'j', 's': 'k', 'c': 'l', 'u': 'm', 'd': 'n', 'h': 'o', 'f': 'p', 'k': 'q', 'v': 'r', 'm': 's', 'y': 't', 'o': 'u', 'i': 'v', 'g': 'w', 'n': 'x', 'p': 'y', 'l': 'z', 'J': 'A', 'E': 'B', 'X': 'C', 'Q': 'D', 'A': 'E', 'T': 'F', 'Z': 'G', 'W': 'H', 'B': 'I', 'R': 'J', 'S': 'K', 'C': 'L', 'U': 'M', 'D': 'N', 'H': 'O', 'F': 'P', 'K': 'Q', 'V': 'R', 'M': 'S', 'Y': 'T', 'O': 'U', 'I': 'V', 'G': 'W', 'N': 'X', 'P': 'Y', 'L': 'Z', '`': '.', '=':','}
main_input = input("Do you want to 1)encrypt or 2)decrypt?(enter digit) ")


def random_alpha(string):
    for m in range(2):
        for j in range(3):
            ran = random.choice("abcdefghijklmnopqrstuvwxyz!@#$%^&*")
            string = string + ran
        string = string[::-1]
    return string


def codec(inp1, inp2):
    diction = inp1
    lis = inp2
    for o in range(len(lis)):
        words = list(lis[o])
        for k in range(len(words)):
            for j in diction:
                if words[k] == j:
                    x = diction[j]
                    words[k] = x
                    break
        words = ''.join(words)
        lis[o] = words
    return lis


if main_input == "1":
    user_input = input("Enter Input: ")

    list1 = user_input.split()
    for i in range(len(list1)):
        list1[i] = list1[i][::-1]

    list1 = codec(encrypt_dict, list1)

    for i in range(len(list1)):
        z = random_alpha(list1[i])
        list1[i] = z

    user_input = '&'.join(list1)
    print(f"The Encrypted Word is {user_input}")


elif main_input == "2":
    user_input1 = input("Enter for decryption:")
    list1 = user_input1.split('&')
    for i in range(len(list1)):
        word = list(list1[i])
        del(word[0:3])
        del(word[-3:])
        word = ''.join(word)
        list1[i] = word
    list1 = codec(decrypt_dict, list1)

    for i in range(len(list1)):
        list1[i] = list1[i][::-1]

    user_input = ' '.join(list1)

    print(f"The Decrypted Word is: {user_input}")

