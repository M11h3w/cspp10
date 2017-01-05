person1 = 1058
person2 = 160
person3 = 15034590
person4 = 4
person5 = 21506
person6 = 2650
person7 = 1000000
person8 = 200000000000
person9 = 579
person10 = 437

print("Welcome to Stewart Bank")
print("")
entry = int(input("Who are you, Person 1-10? "))
print("")
if entry == 1:
    print("Hello Person 1!")
    password1 = input("Please enter the pssword: ")
    if password1 == "person1":
        print("Thank You")
        print("")
        print("You have {}".format(person1))
        print("")
        print("1. Withdraw \n2. Deposit \n3. Exit")
        choice = input("Welcome to ATM! Pick from above [1|2|3]:")
        if choice == "1":
            amount = input("How much to withdraw: ")
            person1 = person1 - int(amount)
            print("You have {}".format(person1))
        elif choice == "2":
            amount = input("How much to deposit: ")
            person1 = person1 + int(amount)
            print("You have {}".format(person1))
        elif choice == "3":
            print("Bye. You have {}".format(person1))
    elif password1 != "person1":
        print("Wrong password!")
elif entry == 2:
    print("Hello Person 2!")
    password2 = input("Please enter the pssword: ")
    if password2 == "person2":
        print("Thank You")
        print("")
        print("You have {}".format(person2))
        print("")
        print("1. Withdraw \n2. Deposit \n3. Exit")
        choice = input("Welcome to ATM! Pick from above [1|2|3]:")
        if choice == "1":
            amount = input("How much to withdraw: ")
            person2 = person2 - int(amount)
            print("You have {}".format(person2))
        elif choice == "2":
            amount = input("How much to deposit: ")
            person2 = person2 + int(amount)
            print("You have {}".format(person2))
        elif choice == "3":
            print("Bye. You have {}".format(person2))
    elif password2 != "person2":
        print("Wrong password!")
elif entry == 3:
    print("Hello Person 3!")
    password3 = input("Please enter the pssword: ")
    if password3 == "person3":
        print("Thank You")
        print("")
        print("You have {}".format(person3))
        print("")
        print("1. Withdraw \n2. Deposit \n3. Exit")
        choice = input("Welcome to ATM! Pick from above [1|2|3]:")
        if choice == "1":
            amount = input("How much to withdraw: ")
            person3 = person3 - int(amount)
            print("You have {}".format(person3))
        elif choice == "2":
            amount = input("How much to deposit: ")
            person3 = person3 + int(amount)
            print("You have {}".format(person3))
        elif choice == "3":
            print("Bye. You have {}".format(person3))
    elif password3 != "person3":
        print("Wrong password!")
elif entry == 4:
    print("Hello Person 4!")
    password4 = input("Please enter the pssword: ")
    if password4 == "person4":
        print("Thank You")
        print("")
        print("You have {}".format(person4))
        print("")
        print("1. Withdraw \n2. Deposit \n3. Exit")
        choice = input("Welcome to ATM! Pick from above [1|2|3]:")
        if choice == "1":
            amount = input("How much to withdraw: ")
            person4 = person4 - int(amount)
            print("You have {}".format(person4))
        elif choice == "2":
            amount = input("How much to deposit: ")
            person4 = person4 + int(amount)
            print("You have {}".format(person4))
        elif choice == "3":
            print("Bye. You have {}".format(person4))
    elif password4 != "person4":
        print("Wrong password!")
elif entry == 5:
    print("Hello Person 5!")
    password5 = input("Please enter the pssword: ")
    if password5 == "person5":
        print("Thank You")
        print("")
        print("You have {}".format(person5))
        print("")
        print("1. Withdraw \n2. Deposit \n3. Exit")
        choice = input("Welcome to ATM! Pick from above [1|2|3]:")
        if choice == "1":
            amount = input("How much to withdraw: ")
            person5 = person5 - int(amount)
            print("You have {}".format(person5))
        elif choice == "2":
            amount = input("How much to deposit: ")
            person5 = person5 + int(amount)
            print("You have {}".format(person5))
        elif choice == "3":
            print("Bye. You have {}".format(person5))
    elif password5 != "person5":
        print("Wrong password!")