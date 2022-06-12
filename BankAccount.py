
class BankAccount:
    balance = 0
    int_rate = .01
    all_accounts = []

    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insuffecient Funds")
        else:
            self.balance -= amount
        return self
    
    def display_account_info(self):
        print("Account Balance:", self.balance)
        print("Interest Rate is", self.int_rate)
        return self
    
    def yield_interest(self, int_rate):
        self.balance = self.balance + self.balance * self.int_rate
        return self

    @classmethod
    def all_balances(cls):
        sum = 0
        for account in cls.all_accounts:
            sum += account.balance
        return sum
        


bob = BankAccount(.01, 100)
lois = BankAccount(.02, 10)
bob.deposit(25).deposit(25).deposit(25).withdraw(15).yield_interest(.01).display_account_info()
lois.deposit(15).deposit(15).withdraw(5).withdraw(5).withdraw(10).withdraw(5).yield_interest(.02).display_account_info()

print(BankAccount.all_balances())
