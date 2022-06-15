
from typing_extensions import Self
from BankAccount import BankAccount

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        # self.account = BankAccount(int_rate=0.02, balance=0) #creating one account for this user only
        self.accounts = {
            "account_1": BankAccount(int_rate = 0.02, balance = 0)
        } # can hold the accounts
    
    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.gold_card_points)
        return self
    
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points += 200
        elif self.is_rewards_member == True:
            print("User already a member")
        return self

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("insuffecient funds")
        else:
            self.gold_card_points = self.gold_card_points - amount
        return self

# these methods are calling on BankAccount Class
    def make_deposit(self, amount):
        self.account.deposit(amount)
        print(self.account.balance)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        print(self.account.balance)
        return self

    def display_user_balance(self):
        self.account.display_account_info(self)
        return self

    #creates a new account
    def new_account(self, account_name, starting_int_rate = 0.03, starting_balance = 0):
        self.accounts[account_name] = BankAccount(starting_int_rate, starting_balance)

    #targets specific account
    def make_deposit(self, amount_to_add, account_name="account_1"):
        self.accounts[account_name].deposit(amount_to_add)
        

    def make_withdraw(self, amount_to_remove, account_name="account_1"):
        self.accounts[account_name].withdraw(amount_to_remove)

    def transfer_money(self, amount, other_user, withdraw_from = "account_1", deposit_to = "account_1"):
        self.make_withdraw(amount, withdraw_from)
        other_user.make_deposit(amount, deposit_to)


bob = User("Bob", "bob", "bobby@gmail.com", 23)
# print(bob.accounts["account_1"].balance)
bob.new_account("account_2",0.03,500)
# print(bob.accounts["account_2"].balance)

susie = User("Bob", "bob", "bobby@gmail.com", 24)
bob.transfer_money(500, susie, "account_2", "account_1")
#needs to specify which account
print(susie.accounts["account_1"].balance)

