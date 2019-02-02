class Account :
    def __init__(self, accout_holder) :
            self.balance = 0
            self.holder = accout_holder
    def  deposit(self, amount):
            self.balance = self.balance + amount
            return self.balance
    def withdraw(self, amount):
            if amount > self.balance :
                return 'Insufficient funds'
            else :
                self.balance = self.balance - amount
            return self.balance
