class ShoppingCart:
    def __init__(self):
        self.items = []  # Initialize an empty list to store items in the cart

    def add_item(self, product, quantity):
        # Method to add an item to the cart
        self.items.append({'product': product, 'quantity': quantity})

    def remove_item(self, index):
        # Method to remove an item from the cart based on its index
        del self.items[index]

    def display_cart(self):
        # Method to display the items in the cart
        if not self.items:
            print("Your cart is empty.")
        else:
            for index, item in enumerate(self.items):
                product = item['product']
                quantity = item['quantity']
                print(f"{index + 1}. {product.name} - Quantity: {quantity}")

    def calculate_total(self):
        # Method to calculate the total amount of items in the cart
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total
