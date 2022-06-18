from store_class import Store
from product_class import Product



apple = Product("Apple", 1.5, "Fruit")
banana = Product("Banana", 1, "Fruit")
socks = Product("Socks", 10, "Clothing")

Giant = Store("Giant")

Giant.add_product(apple)
Giant.add_product(socks)
Giant.add_product(banana)

Giant.set_clearance("Fruit", .1)

print(Giant.products[0].price)




