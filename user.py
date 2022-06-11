
from typing_extensions import Self


class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
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



bob = User("Bobbert", "Harvery", "bobbertharvery@yahoo.com", 27)
amber = User("Amber", "Harvy", "ambylambs@yahoo.com", 300)

bob.enroll().display_info().spend_points(300).display_info()



