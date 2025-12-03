class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Market:
    def __init__(self):
        self.objects = []
        self.budget = 0.0

    def add_product(self, name, price, quantity):
        if name in self.objects:
            self.objects[name].quantity += quantity
        else:
            self.objects[name] = Product(name, price, quantity)

    def display_market(self):
        if not self.objects:
            print("Market is empty.")
        else:
            for item in self.objects.values():
                print(item)
        print(f" Shop Budget: {self.budget}")

class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.cart = []



