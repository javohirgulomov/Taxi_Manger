class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def info(self):
        return f"{self.title} | ${self.price}"

class TV(Product):
    def __init__(self, title, price, display):
        super().__init__(title, price)
        self.display = display

    def info(self):
        return f"{self.title} | ${self.price} | Display: {self.display}\""


class PC(Product):
    def __init__(self, title, price, ram):
        super().__init__(title, price)
        self.ram = ram

    def info(self):
        return f"{self.title} | ${self.price} | RAM: {self.ram}GB"


class Phone(Product):
    def __init__(self, title, price, camera):
        super().__init__(title, price)
        self.camera = camera

    def info(self):
        return f"{self.title} | ${self.price} | Camera: {self.camera}MP"


class Market(Product):
    def __init__(self):
        self.products = []

    def view_prodcuts(self):
        if not self.products:
            print("No products")
        else:
            for product in self.products:
                print(product.info())
    def add_tv(self):
        title = input("title:")
        price = input("price:")
        display = input("display:")
        tv = TV(title, price, display)
        self.products.append(tv)
        print("TV added")

    def add_pc(self):
        title = input("PC title:")
        price = input("PC price:")
        ram = input("PC RAM:")
        pc = PC(title, price, ram)
        self.products.append(pc)
        print("PC added")

    def add_phone(self):
        title = input("Phone title:")
        price = input("Phone price:")
        camera = input("Phone camera:")
        phone = Phone(title, price, camera)
        self.products.append(phone)
        print("Phone added")

    def remove_prodcuts(self):
        self.view_prodcuts()
        if not self.products:
            return
        index = int(input("index:"))-1
        if 0<=index<len(self.products):
            removed = self.products.pop(index)
            print("Removed")
        else:
            print("Invalid")

def shop_manager():
    market = Market()
    while True:
        choice = input("\n1. View all products\n2. Add TV\n3. Add PC\n4. Add Phone\n5. Remove product\n6. Exit\n ")
        if choice == "1":
            market.view_prodcuts()
        elif choice == "2":
            market.add_tv()
        elif choice == "3":
            market.add_pc()
        elif choice == "4":
            market.add_phone()
        elif choice == "5":
            market.remove_prodcuts()
        elif choice == "6":
            print("Goodbye")
            break
        else:
            print("Invalid")

shop_manager()

