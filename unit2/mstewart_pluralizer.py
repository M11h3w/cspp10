num = input("Enter a number: ")
word = input("Enter a noun: ")
space = " "
if num == "1":
    print(num + space + word)
elif num == "0" or num > "1":
    if word[-2:] == "fe":
        word2 = word[:-2]
        ves = "ves"
        print(num + space + word2 + ves)
    elif word[-2:] == "uy" or word[-2:] == "oy" or word[-2:] == "ey" or word[-2:] == "ay":
        s = "s"
        print(num + space + word + s)
    elif word[-1:] == "y":
        word2 = word[:-1]
        ies = "ies"
        print(num + space + word2 + ies)
    elif word[-2:] == "us":
        word2 = word[:-2]
        i = "i"
        print(num + space + word2 + i)
    elif word[-2:] == "sh" or word[-2:] == "ch":
        es = "es"
        print(num + space + word + es)
    else:
        s = "s"
        print(num + space + word + s)