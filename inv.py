class Product:
    def __init__(self, product_id, name, details, price, quantity):
        self.product_id = product_id
        self.name = name
        self.details = details
        self.price = price
        self.quantity = quantity

    def display_details(self):
        """Display details of the product."""
        print("Product Details:")
        print("ID:", self.product_id)
        print("Name:", self.name)
        print("Details:", self.details)
        print("Price: $", self.price)
        print("Quantity in Store:", self.quantity)


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_inventory(self):
        print("Shop Inventory:")
        for product in self.products:
            print(product.name)

    def find_product(self, product_name):
        for product in self.products:
            if product.name.lower() == product_name.lower():
                return product
        return None

    def add_to_cart(self, product_name, quantity):
        product = self.find_product(product_name)
        if product:
            if product.quantity >= quantity:
                print("Product added to cart successfully.")
                # Here we  implement the logic to add the product to the cart
            else:
                print("Insufficient quantity in store.")
        else:
            print("Product not found in inventory.")


def inventory_module():
    print("Welcome to the Inventory Module")
    inventory = Inventory()

    #  inventory  samples 
    inventory.add_product(Product(1, 'T-shirt', 'Cotton T-shirt', 15.99, 50))
    inventory.add_product(Product(2, 'Jeans', 'Blue denim jeans', 29.99, 30))
    inventory.add_product(Product(3, 'Sneakers', 'White canvas sneakers', 39.99, 20))

    while True:
        print("\nMenu:")
        print("1. Check Shop Inventory")
        print("2. View Product Details")
        print("3. Add Product to Cart")
        print("4. Sign Out")
        choice = input("Enter your choice: ")
        if choice == '1':
            inventory.display_inventory()
        elif choice == '2':
            product_name = input("Enter the name of the product: ")
            product = inventory.find_product(product_name)
            if product:
                product.display_details()
            else:
                print("Product not found in inventory.")
        elif choice == '3':
            product_name = input("Enter the name of the product: ")
            quantity = int(input("Enter the quantity: "))
            inventory.add_to_cart(product_name, quantity)
        elif choice == '4':
            print("Signing out...")
            break
        else:
            print("Invalid choice. Please try again.")


# Test the inventory module
inventory_module()
