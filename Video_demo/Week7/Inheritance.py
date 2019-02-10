class Account:
        interest = 0.02
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

class CheckAcccount(Account):
        withdraw_fee = 1
        interest = 0.01
        def withdraw(self, amount):
                return Account.withdraw(self, amount + self.withdraw_fee)

class Bank:
    '''
    >>> bank =Bank()
    >>> jim = bank.open_account('jim', 10)
    >>> tom = bank.open_account('tom', 5, CheckAcccount)
    >>> jim.interest
    0.02
    >>> tom.interest
    0.01
    >>> bank.pay_interest()
    >>> jim.balance
    '''
    def __init__(self):
            self.accounts = []
    def open_account(self, holder, amount, kind=Account):
        account  = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account
    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)
    def to_big_to_fail(self):
        return len(self.accounts) > 1
