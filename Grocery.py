"""
AP Computer Science Principles Performance Task
Title: Shopping Cart Simulator
"""

# Basic Grocery class
class Grocery:
    # Constructor
    def __init__(self, name, price):
        self.name = name
        self.price = float(price)

    # Changes name of grocery
    def change_name(self, name):
        self.name = name

    # Changes price of grocery
    def change_price(self, price):
        self.name = float(price)

    # Return grocery name
    def get_name(self):
        return self.name
    
    # Returns grocery price
    def get_price(self):
        return self.price

    # Prints grocery description
    def item_desc(self):
        print(f"{self.name} is ${self.price}")
    
    # Prints bare grocery information
    def print_groc(self):
        print(f"Name: {self.name}\nPrice: {self.price}")

# Vegetable, type of grocery
class Vegetable(Grocery):
    # Constructor
    def __init__(self, name, price, calories):
        super().__init__(name, price)
        self.calories = float(calories)
    
    # Changes calories of vegetable
    def change_calories(self, calories):
        self.calories = float(calories)
    
    # Returns vegetable calories
    def get_calories(self):
        return self.calories

    # Prints vegetable description
    def veg_desc(self):
        print(f"The price of {self.name} is ${self.price}, and it is {self.calories} calories.")

    # Prints bare vegetable information
    def print_veg(self):
        super().print_groc()
        print(f"Calories: {self.calories}")

# Canned Good, type of grocery
class CannedGood(Grocery):
    # Constructor
    def __init__(self, name, price, brand, type):
        super().__init__(name, price)
        self.brand = brand
        self.type = type
    
    # Changes brand of canned good
    def change_brand(self, brand):
        self.brand = brand

    # Changes type of canned good
    def change_type(self, type):
        self.type = type

    # Returns brand of canned good
    def get_brand(self):
        return self.brand

    # Returns type of canned good
    def get_type(self):
        return self.type

    # Prints canned good description
    def good_desc(self):
        print(f"The price of {self.name} is ${self.price}, the brand is {self.brand}, and it is a {self.type}.")

    # Prints bare canned good information
    def print_canned_good(self):
        super().print_groc()
        print(f"Brand: {self.brand}\nType: {self.type}")

# Dairy, type of grocery
class Dairy(Grocery):
    # Constructor
    def __init__(self, name, price, month_exp, day_exp, year_exp):
        super().__init__(name, price)
        self.expiration = f"{month_exp}/{day_exp}/{year_exp}"

    # Changes expiration date of dairy product
    def change_expiration(self,month_exp, day_exp, year_exp):
        self.expiration = f"{month_exp}/{day_exp}/{year_exp}"

    # Returns expiration date
    def get_expiration(self):
        return self.expiration

    def dairy_desc(self):
        print(f"The price of {self.name} is ${self.price}, it expires on {self.expiration}")

    def print_dairy(self):
        super().print_groc()
        print(f"Expiration: {self.expiration}")
