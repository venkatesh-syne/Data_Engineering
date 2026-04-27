class BankAccount:

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
    def check_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Current Balance: {self.balance}")
acc = BankAccount("Venkatesh", 1000)
acc.deposit(500)
acc.withdraw(300)
acc.check_balance()