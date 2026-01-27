# Encapsulation in Python: Hide Your Data Like a Pro! 🔒

class BankAccount:

    def __init__(self,owner,balance):
        self.owner = owner

        # private varibale: cannot be accessed directly from oustside
        self.__balance = balance

    
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("deposite amount is invalid")

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdraean. Remaining: {self.__balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        # private variable
        return self.__balance

# encapsulation

account = BankAccount("Sir",1000)

# try access __balance directly
# print(account.__balance)

print(f"Account owner : {account.owner}")
account.deposit(500)
account.withdraw(200)

print(f"Final Balance: {account.get_balance()}")