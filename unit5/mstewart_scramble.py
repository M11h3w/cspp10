import random
word = input()
# if len(word) == 4:
#     dont_scarmble1 = word[0]
#     dont_scramble2 = word[3]
# elif len(word) > 4:
#     word_l(word)
#     word.split(" ")
#     print(word)
word.split(" ")
random.shuffle(list(word))
print(word)