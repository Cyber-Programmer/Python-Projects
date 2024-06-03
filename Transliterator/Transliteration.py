
while True:
    print("What Do You Want To Do? \n 1. Transliterate from English to Urdu \n 2. Transliterate from Urdu to English \n 3. End Program")
    Answer = int(input("Choose: "))
    if Answer == 1:
        h = input("Enter something in English: ")
        g = ""
        a = {"a": "ا", "b": "ب", "c": "ک", "d": "د", "e": "ع", "f": "ف", "g": "گ", "h": "ح", "i": "ی", "j": "ج", "k": "ک", "l": "ل", "m": "م", "n": "ن", "o": "اُ", "p": "پ", "q": "ق", "r": "ر", "s": "ص", "t": "ت", "u": "ؤ", "v": "و", "w": "و", "x": "ش", "y": "ے", "z": "ز"," ": " "}

        for i in h:
            g += a[i]

        print("Transliterated: ", g)

    elif Answer == 2:
        h = input("Enter something in Urdu: ")
        g = ""
        a = {"ا": "a", "ب": "b", "پ": "p", "ت": "t", "ٹ": "s", "ث": "t", "ج": "j", "چ": "ch", "ح": "h", "خ": "kh", "د": "d", "ڈ": "d", "ذ": "z", "ر": "r", "ڑ": "r", "ز": "z", "ژ": "z", "س": "s", "ش": "sh", "ص": "s", "ض": "z", "ط": "t", "ظ": "z", "ع": "e", "غ": "gh", "ف": "f", "ق": "ca", "ک": "k", "گ": "g", "ل": "l", "م": "m", "ن": "n", "و": "w", "ہ": "h", "ی": "i", "ے": "y"," ": " "}

        for i in h:
            g += a[i]

        print("Transliterated: ", g)

    elif Answer == 3:
        tprint("End :)")
        break
