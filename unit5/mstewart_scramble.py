import random
word = input()
first = word[0]
last = word[-1]
if len(word) == 4:
    word = word[1:3]
    word = list(word)
    s = random.shuffle(word)
    print(s)