"""
AP Computer Science Principles Performance Task
Title: Shopping Cart Simulator
"""

class ShoppingCart:
    # Initializes an empty cart
    def __init__(self):
        self.cart = []

    # Places an item in the cart
    def place_mult_items(self, list):
        for item in list:
            self.cart.append(item)
            print(f"Item: {item}, added to cart!")
        print("\nFinished adding all items!")

    def print_contents(self):
        print("Items on cart:")
        for item in self.cart:
            print(item)
