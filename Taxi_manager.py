class User:
    def __init__(self, name, phone, seria, age, password):
        self.username = name
        self.phone = phone
        self.seria = seria
        self.age = age
        self.password = password
        self.is_active = True
        self.is_admin = False
        self.car_taken = None


class Car:
    def __init__(self, model, brand, year, seria):
        self.model = model
        self.brand = brand
        self.year = year
        self.seria = seria
        self.is_taken = False


class Order:
    def __init__(self, user_id, car_id, date_start, date_end):
        self.user_id = user_id
        self.car_id = car_id
        self.date_start = date_start
        self.date_end = date_end
        self.is_active = True


class Park:
    def __init__(self, title):
        self.title = title
        self.users = []
        self.cars = []
        self.orders = []

    def login(self):
        name = input("Username: ")
        password = input("Password: ")

        for user in self.users:
            if user.username == name and user.password == password:
                print(f"Welcome, {user.username}")
                return user

        print("Login failed")
        return None

    def admin_menu(self, admin):
        while True:
            print("""
=== ADMIN MENU ===
1. View free cars
2. View taken cars
3. View free employees
4. View busy employees
5. Add employee
6. Add car
7. Logout
""")
            k = input("Choose: ")

            if k == "1":
                self.show_free_cars()
            elif k == "2":
                self.show_taken_cars()
            elif k == "3":
                self.show_free_employees()
            elif k == "4":
                self.show_busy_employees()
            elif k == "5":
                self.add_employee()
            elif k == "6":
                self.add_car()
            elif k == "7":
                break
            else:
                print("Invalid")

    def driver_menu(self, driver):
        while True:
            print("""
=== DRIVER MENU ===
1. View free cars
2. Take car
3. Return car
4. View my car
5. Edit my profile
6. Logout
""")
            k = input("Choose: ")

            if k == "1":
                self.show_free_cars()
            elif k == "2":
                self.take_car(driver)
            elif k == "3":
                self.return_car(driver)
            elif k == "4":
                self.show_my_car(driver)
            elif k == "5":
                self.edit_profile(driver)
            elif k == "6":
                break
            else:
                print("Invalid")

    def show_free_cars(self):
        print("\nFree cars:")
        for c in self.cars:
            if not c.is_taken:
                print(f"{c.model} | {c.brand} | {c.year} | ID:{c.seria}")
        print()

    def show_taken_cars(self):
        print("\nTaken cars:")
        for c in self.cars:
            if c.is_taken:
                print(f"{c.model} | Taken")
        print()

    def show_free_employees(self):
        print("\nFree employees:")
        for u in self.users:
            if not u.is_admin and u.car_taken is None:
                print(u.username)
        print()

    def show_busy_employees(self):
        print("\nBusy employees:")
        for u in self.users:
            if not u.is_admin and u.car_taken is not None:
                print(f"{u.username} -> {u.car_taken.model}")
        print()

    def add_employee(self):
        name = input("Name: ")
        phone = input("Phone: ")
        seria = input("Seria: ")
        age = input("Age: ")
        password = input("Password: ")
        u = User(name, phone, seria, age, password)
        self.users.append(u)
        print("Employee added.")

    def add_car(self):
        model = input("Model: ")
        brand = input("Brand: ")
        year = input("Year: ")
        seria = input("Seria: ")
        c = Car(model, brand, year, seria)
        self.cars.append(c)
        print("Car added.")

    def take_car(self, driver):
        if driver.car_taken:
            print("You already have a car.")
            return

        self.show_free_cars()
        seria = input("Enter car seria: ")

        for c in self.cars:
            if c.seria == seria and not c.is_taken:
                c.is_taken = True
                driver.car_taken = c
                print("Car taken.")
                return

        print("Car not available.")

    def return_car(self, driver):
        if not driver.car_taken:
            print("You have no car.")
            return

        driver.car_taken.is_taken = False
        driver.car_taken = None
        print("Car returned.")

    def show_my_car(self, driver):
        if driver.car_taken:
            print("Your car:", driver.car_taken.model)
        else:
            print("You have no car.")

    def edit_profile(self, driver):
        driver.username = input("New username: ")
        driver.password = input("New password: ")
        print("Profile updated.")


park = Park("Park1")

admin = User("Admin", "123", "AA001", 25, "admin123")
admin.is_admin = True
park.users.append(admin)


def park_manager(p: Park):
    while True:
        print("\n=== LOGIN ===")
        user = p.login()

        if not user:
            continue

        if user.is_admin:
            p.admin_menu(user)
        else:
            p.driver_menu(user)


park_manager(park)
