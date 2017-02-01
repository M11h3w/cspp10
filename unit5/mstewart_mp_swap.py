a = [1,2,3,4,5,6,7,8,9,10]
command = 1
print(a)
print("")
print("")
while command != "exit":
    command = input("Enter a command(swap or exit): ")
    print("")
    if command == "swap":
        swap1 = int(input("What is the first number you want to swap? "))
        if swap1 in a:
            index1 = a.index(swap1)
            a.remove(swap1)
            swap2 = int(input("What is the second number you want to swap? "))
            if swap2 in a:
                index2 = a.index(swap2 + 1)
                a.remove(swap2)
                a.insert(index1,swap2)
                a.insert(index2,swap1)
                print("")
                print(a)
    elif command == "exit":
        break

# a = [1,2,3,4,5,6,7,8,9,10]
# print(a)
# swap1 = int(input())
# if swap1 in a:
#     index1 = a.index(swap1)
#     a.remove(swap1)
#     swap2 = int(input())
#     if swap2 in a:
#         index2 = a.index(swap2 + 1)
#         a.remove(swap2)
#         a.insert(index1,swap2)
#         a.insert(index2,swap1)
#     print(a)