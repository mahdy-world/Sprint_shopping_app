class ShoppingCart:
    def __init__(self):
        self.items = []  # Initialize an empty list to store items in the cart

    # Method to add an item to the cart
    def add_item(self, product, quantity):
        
        self.items.append({'product': product, 'quantity': quantity})

    # Method to remove an item from the cart based on its index
    def remove_item(self, index):
      
        del self.items[index]
        
    # Method to display the items in the cart
    def display_cart(self):
        
        if not self.items:
            print("Your cart is empty.")
        else:
            for index, item in enumerate(self.items):
                product = item['product']
                quantity = item['quantity']
                print(f"{index + 1}. {product.name} - Quantity: {quantity}")

     # Method to calculate the total amount of items in the cart
    def calculate_total(self):
       
        total = 0
        for item in self.items:
            total += item['product'].price * item['quantity']
        return total
