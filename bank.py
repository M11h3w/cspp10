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
        print("You have {}".format(person1))
        
elif entry == 2:
    print("Hello Person 2!")
    password2 = input("Please enter the pssword: ")
elif entry == 3:
    print("Hello Person 3!")
    password3 = input("Please enter the pssword: ")
elif entry == 4:
    print("Hello Person 4!")
    password4 = input("Please enter the pssword: ")
elif entry == 5:
    print("Hello Person 5!")
    password5 = input("Please enter the pssword: ")