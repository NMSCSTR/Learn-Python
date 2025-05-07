class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Unsufficient amount!")


    def view_account(self):
        print(self.__balance)


# named mangled
rhondelAccount = BankAccount("Rhondel", 2000)
rhondelAccount.view_account()
rhondelAccount.deposit(200)
rhondelAccount.view_account()
rhondelAccount.withdraw(300)
rhondelAccount.view_account()