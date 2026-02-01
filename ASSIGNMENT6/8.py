class Product:
    total_products_sold = 0

    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

    def sell_product(self, amount):
        if amount <= self.qty:
            self.qty -= amount
            Product.total_products_sold += amount
        else:
            print("Not enough stock!")

    @classmethod
    def get_total_products_sold(cls):
        return cls.total_products_sold


p1 = Product("Mobile", 10000, 5)
p1.sell_product(2)

p2 = Product("Laptop", 50000, 3)
p2.sell_product(1)

print("Total Products Sold:", Product.get_total_products_sold())
