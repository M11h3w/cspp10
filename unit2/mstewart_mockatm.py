bank_account = 10000
print(bank_account)
print("1. Withdraw \n2. Deposit \n3. Exit")
choice = input("Welcome to ATM! Pick from above [1|2|3]:")
while(bank_account >= 0):
    if choice == "1":
        amount = input("How much to withdraw: ")
        bank_account = bank_account - int(amount)
        print(bank_account)
    elif choice == "2":
        amount = input("How much to deposit: ")
        bank_account = bank_account + int(amount)
        print(bank_account)
    elif choice == "3":
        print(bank_account)
        break
    print("1. Withdraw \n2. Deposit \n3. Exit")
    choice = input("Pick from above [1|2|3]:")