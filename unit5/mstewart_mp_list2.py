a_list = []





command = 1
while command != "exit":
    command = input("Enter a command: ")
    if command == "sum":
        print(sum(a_list))
        print("")
    elif command == "clear":
        a_list = []
    elif int(command) >= 0 or int(command) <= 0:
        a_list.append(int(command))
        print(a_list)
        print("")
    elif command == "print":
        print(a_list)
    elif command == "length":
        print(len(a_list))
    elif command == "exit":
        break