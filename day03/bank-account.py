class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount < 0:
            print("We cannot deposit negative amounts")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print("We cannot withdraw negative amounts")
        elif self.__balance < amount:
            print("Insufficient balance")
        else:
            self.__balance -= amount

    def print_balance(self):
        print(f"Balance: {self.__balance}")

account = BankAccount()
account.print_balance()
account.withdraw(100)
account.deposit(1000)
account.print_balance()
account.withdraw(100)
account.print_balance()
print(account.__balance)
