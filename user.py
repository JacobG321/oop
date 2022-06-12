
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
        self.account = BankAccount(int_rate=0.02, balance=0)
    
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



bob = User("Bobbert", "Harvery", "bobbertharvery@yahoo.com", 27)
amber = User("Amber", "Harvy", "ambylambs@yahoo.com", 300)

# bob.enroll().display_info().spend_points(300).display_info()


bob.make_deposit(100)
bob.make_withdraw(200)
bob.make_withdraw(100).make_deposit(500).display_user_balance()


