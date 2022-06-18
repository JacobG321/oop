
from product_class import Product

class Store:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, new_product):
        self.products.append(new_product)
    
    def sell_product(self, id):
        self.products.pop(id)

    def inflation(self, percent_increase):
        Product.update_price(percent_increase, True)

    def set_clearance(self, category, percent_discount):
        for item in self.products:
            if item.category == category:
                item.update_price(percent_discount, False)

        # if categori == Product.category:
        #     Product.update_price(percent_discount, False)


        #iterate through the list of products
        #check each product to see if it is in the category
        #update price