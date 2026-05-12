balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Balance:", balance)

    elif choice == 2:
        amt = int(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
            print("Withdraw success")
        else:
            print("Insufficient balance")

    elif choice == 3:
        amt = int(input("Enter amount: "))
        balance += amt
        print("Deposited")

    elif choice == 4:
        break