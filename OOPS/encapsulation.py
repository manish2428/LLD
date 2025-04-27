
class BankAccount:
    def __init__(self, account_holder):
        self.__balance = 0
        self.account_holder = account_holder

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited to your account. Your Current Balance is {self.__balance}")

    def withdraw(self,amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("Your current balance is ", self.__balance)

        else:
            print("Insufficient Balance ")

    def CheckBalance(self):
        print("Your current balance is ", self.__balance)

acholder1 = BankAccount("Manish")

#deposit
acholder1.deposit(18000)
acholder1.deposit(950)

#withdraw(amount<balance)
acholder1.withdraw(500)

#insufficient balance(amount>balance)
acholder1.withdraw(50000)


"""
Encapsulation means hiding internal data 
and only allowing it to be accessed or modified through methods.
This protects your data and enforces how it should be used.


- Prevents direct modification of important variables.
- Keeps internal logic hidden from the outside world.

"""
