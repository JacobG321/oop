class Product:
    def __init__(self, name_of_item, price, category):
        self.name_of_item = name_of_item
        self.price = price
        self.category = category

    def update_price(self, percent_change, is_increased):
        if is_increased == True:
            self.price += percent_change * self.price
        else:
            self.price -= percent_change * self.price
    
    def print_info(self):
        print(self.name_of_item, self.price, self.category)