import random
word_list = [
    ['Strawberry', 'Friendship', 'Motivation', 'Everything', 'Icebreaker', 'Pacemakers', 'Quadcopter', 'Yardsticks',
     'Vaccinated'],
    ['apology', 'amateur', 'analogy', 'balloon', 'bangkok', 'bizarre', 'cartoon', 'costume', 'diamond', 'dolphin',
     'fantasy', 'journey', 'kitchen'], ['high', 'good', 'luck', 'forever', 'nice', 'went', 'philosophy'],
    ['Earth', 'Eight', 'Elite', 'Space', 'Shine', 'Spark', 'Elect', 'Towel', 'Troll', 'Clown', 'Cross', 'Lunch',
     'Witch']]

for i in range(len(word_list)):

    print("This is Level", i + 1)
    word = list(random.choice(word_list[i]))

    st = []
    for i in range(len(word)):
        st += '_'
    for k in range(len(st)):
        print(st[k], end='')
    print()
    print("Guess The Word")
    for i in range(int(len(word) * 1.5)):
        f = input("Enter letter: ")
        for j in range(len(word)):
            if (word[j] == f) and not st[j] == f:
                st[j] = f
                for k in range(len(st)):
                    print(st[k], end='')
                print()
        if not '_' in st:
            del word
            break


    if '_' in st:
        print("Game Over!")
    else:
        print("The Word Was: ")
        for k in st:
            print(k, end="")


"""from art import *"""
"""tprint("WELCOME   TO   HANGMAN")"""
