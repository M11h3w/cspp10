person1 = 1358
person2 = 160
person3 = 15334590
person4 = 4
person5 = 21506
person6 = 2650
person7 = 1000000
person8 = 235635787981
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
        print("You have ${}".format(person1))
        print("")
        while person1 >= 0:
            print("1. Withdraw \n2. Deposit \n3. Exit")
            choice = input("Welcome to ATM! Pick from above [1|2|3]: ")
            if choice == "1":
                amount = input("How much to withdraw: ")
                person1 = person1 - int(amount)
                print("You have ${}".format(person1))
                print("")
            elif choice == "2":
                amount = input("How much to deposit: ")
                person1 = person1 + int(amount)
                print("You have ${}".format(person1))
                print("")
            elif choice == "3":
                print("Bye. You have ${}".format(person1))
                break
    elif password1 != "person1":
        print("Wrong password!")
elif entry == 2:
    print("Hello Person 2!")
    password2 = input("Please enter the pssword: ")
    if password2 == "person2":
        print("Thank You")
        print("")
        print("You have ${}".format(person2))
        print("")
        while person2 >= 0:
            print("1. Withdraw \n2. Deposit \n3. Exit")
            choice = input("Welcome to ATM! Pick from above [1|2|3]: ")
            if choice == "1":
                amount = input("How much to withdraw: ")
                person2 = person2 - int(amount)
                print("You have ${}".format(person2))
                print("")
            elif choice == "2":
                amount = input("How much to deposit: ")
                person2 = person2 + int(amount)
                print("You have ${}".format(person2))
                print("")
            elif choice == "3":
                print("Bye. You have ${}".format(person2))
                break
    elif password2 != "person2":
        print("Wrong password!")
elif entry == 3:
    print("Hello Person 3!")
    password3 = input("Please enter the pssword: ")
    if password3 == "person3":
        print("Thank You")
        print("")
        print("You have ${}".format(person3))
        print("")
        while person3 >= 0:
            print("1. Withdraw \n2. Deposit \n3. Exit")
            choice = input("Welcome to ATM! Pick from above [1|2|3]: ")
            if choice == "1":
                amount = input("How much to withdraw: ")
                person3 = person3 - int(amount)
                print("You have ${}".format(person3))
                print("")
            elif choice == "2":
                amount = input("How much to deposit: ")
                person3 = person3 + int(amount)
                print("You have ${}".format(person3))
                print("")
            elif choice == "3":
                print("Bye. You have ${}".format(person3))
                break
    elif password3 != "person3":
        print("Wrong password!")
elif entry == 4:
    print("Hello Person 4!")
    password4 = input("Please enter the pssword: ")
    if password4 == "person4":
        print("Thank You")
        print("")
        print("You have ${}".format(person4))
        print("")
        while person4 >= 0:
            print("1. Withdraw \n2. Deposit \n3. Exit")
            choice = input("Welcome to ATM! Pick from above [1|2|3]: ")
            if choice == "1":
                amount = input("How much to withdraw: ")
                person4 = person4 - int(amount)
                print("You have ${}".format(person4))
                print("")
            elif choice == "2":
                amount = input("How much to deposit: ")
                person4 = person4 + int(amount)
                print("You have ${}".format(person4))
                print("")
            elif choice == "3":
                print("Bye. You have ${}".format(person4))
                break
    elif password4 != "person4":
        print("Wrong password!")
elif entry == 5:
    print("Hello Person 5!")
    password5 = input("Please enter the pssword: ")
    if password5 == "person5":
        print("Thank You")
        print("")
        print("You have ${}".format(person5))
        print("")
        while person5 >= 0:
            print("1. Withdraw \n2. Deposit \n3. Exit")
            choice = input("Welcome to ATM! Pick from above [1|2|3]: ")
            if choice == "1":
                amount = input("How much to withdraw: ")
                person5 = person5 - int(amount)
                print("You have ${}".format(person5))
                print("")
            elif choice == "2":
                amount = input("How much to deposit: ")
                person5 = person5 + int(amount)
                print("You have ${}".format(person5))
                print("")
            elif choice == "3":
                print("Bye. You have ${}".format(person5))
                break
    elif password5 != "person5":
        print("Wrong password!")
elif entry == 6:
    print("Hello Person 6!")
    password6 = input("Please enter the pssword: ")
    if password6 == "person6":
        print("Thank You")
        print("")
        print("You have ${}".format(person6))
        print("")
        while person6 >= 0:
            print("1. Withdraw \n2. Deposit \n3. Exit")
            choice = input("Welcome to ATM! Pick from above [1|2|3]: ")
            if choice == "1":
                amount = input("How much to withdraw: ")
                person6 = person6 - int(amount)
                print("You have ${}".format(person6))
                print("")
            elif choice == "2":
                amount = input("How much to deposit: ")
                person6 = person6 + int(amount)
                print("You have ${}".format(person6))
                print("")
            elif choice == "3":
                print("Bye. You have ${}".format(person6))
                break
    elif password6 != "person6":
        print("Wrong password!")
elif entry == 7:
    print("Hello Person 7!")
    password7 = input("Please enter the pssword: ")
    if password7 == "person7":
        print("Thank You")
        print("")
        print("You have ${}".format(person7))
        print("")
        while person7 >= 0:
            print("1. Withdraw \n2. Deposit \n3. Exit")
            choice = input("Welcome to ATM! Pick from above [1|2|3]: ")
            if choice == "1":
                amount = input("How much to withdraw: ")
                person7 = person7 - int(amount)
                print("You have ${}".format(person7))
                print("")
            elif choice == "2":
                amount = input("How much to deposit: ")
                person7 = person7 + int(amount)
                print("You have ${}".format(person7))
                print("")
            elif choice == "3":
                print("Bye. You have ${}".format(person7))
                break
    elif password7 != "person7":
        print("Wrong password!")
elif entry == 8:
    print("Hello Person 8!")
    password8 = input("Please enter the pssword: ")
    if password8 == "person8":
        print("Thank You")
        print("")
        print("You have ${}".format(person8))
        print("")
        while person8 >= 0:
            print("1. Withdraw \n2. Deposit \n3. Exit")
            choice = input("Welcome to ATM! Pick from above [1|2|3]: ")
            if choice == "1":
                amount = input("How much to withdraw: ")
                person8 = person8 - int(amount)
                print("You have ${}".format(person8))
                print("")
            elif choice == "2":
                amount = input("How much to deposit: ")
                person8 = person8 + int(amount)
                print("You have ${}".format(person8))
                print("")
            elif choice == "3":
                print("Bye. You have ${}".format(person8))
                break
    elif password8 != "person8":
        print("Wrong password!")
elif entry == 9:
    print("Hello Person 9!")
    password9 = input("Please enter the pssword: ")
    if password9 == "person9":
        print("Thank You")
        print("")
        print("You have ${}".format(person9))
        print("")
        while person9 >= 0:
            print("1. Withdraw \n2. Deposit \n3. Exit")
            choice = input("Welcome to ATM! Pick from above [1|2|3]: ")
            if choice == "1":
                amount = input("How much to withdraw: ")
                person9 = person9 - int(amount)
                print("You have ${}".format(person9))
                print("")
            elif choice == "2":
                amount = input("How much to deposit: ")
                person9 = person9 + int(amount)
                print("You have ${}".format(person9))
                print("")
            elif choice == "3":
                print("Bye. You have ${}".format(person9))
                break
    elif password9 != "person9":
        print("Wrong password!")
elif entry == 10:
    print("Hello Person 10!")
    password10 = input("Please enter the pssword: ")
    if password10 == "person10":
        print("Thank You")
        print("")
        print("You have ${}".format(person10))
        print("")
        while person10 >= 0:
            print("1. Withdraw \n2. Deposit \n3. Exit")
            choice = input("Welcome to ATM! Pick from above [1|2|3]: ")
            if choice == "1":
                amount = input("How much to withdraw: ")
                person10 = person10 - int(amount)
                print("You have ${}".format(person10))
                print("")
            elif choice == "2":
                amount = input("How much to deposit: ")
                person10 = person10 + int(amount)
                print("You have ${}".format(person10))
                print("")
            elif choice == "3":
                print("Bye. You have ${}".format(person10))
                break
    elif password10 != "person10":
        print("Wrong password!")