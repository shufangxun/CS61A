class Account:
        interest = 0
        def __init__(self, account_holder) :
            self.balance = 0
            self.holder = account_holder
        def deposit(self, amount):
            self.balance += amount
            return self.balance
        def withdraw(self, amount):
            if amount > self.balance:
                return 'Insufficient'
            else:
                self.balance -= amount
            return self.balance

'''
jim = Account('jim')
tom = Account('tom')
jim.interest
'''
