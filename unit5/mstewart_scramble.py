import random
word = input()
first = word[0]
last = word[-1]
if len(word) == 4:
    word2 = word[1:3]
    s = list(word2)
    s2 = s
    while s2 == s:
        s2 = random.shuffle(s)
    # print(word2)
    print(s2)
