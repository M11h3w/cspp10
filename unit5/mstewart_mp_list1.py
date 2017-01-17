num_list = []
print("Entering a positive number will add it to the list")
print("Entering a negative number will remove that number from the list")
print("Entering 'replace' will allow you to replace anumber in the list with a new number")
print("Entering 0 will end the program")
num_input = 1
while num_input != 0:
    num_input = input("Enter a number or 'replace': ")
    if num_input == "replace":
        replace1 = int(input("What do want to replace? "))
        if replace1 in num_list:
            replace2 = int(input("What would you like to replace it with? "))
            index = num_list.index(replace1)
            num_list.insert(index, replace2)
            num_list.remove(replace1)
            print(num_list)
            print("")
        else:
            print("That number isn't in the list")
    elif int(num_input) > 0:
        num_list.append(int(num_input))
        print(num_list)
        print("")
    elif int(num_input) < 0:
        num_list.remove(-1 * int(num_input))
        print(num_list)
        print("")
    elif int(num_input) == 0:
        break
    # elif num_input == "replace":
    #     replace1 = int(input("What do want to replace? "))
    #     if replace1 in num_list:
    #         print("True")
    #     else:
    #         print("False")
    #     replace2 = int(input("What would you like to replace it with? "))