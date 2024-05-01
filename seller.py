from product import Product

class Seller:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        for existing_product in self.inventory:
            if existing_product.product_id == product.product_id:
                print("============Product with the same ID already exists.============")
                return

        self.inventory.append(product)
        print("\n============Product added successfully.============")

    def remove_product(self, product_id):
        for product in self.inventory:
            if product.product_id == product_id:
                self.inventory.remove(product)
                print("\n============Product removed successfully.============")
                break
        else:
            print("\n============Product not found.============")

    def update_product(self, product_id, new_name, new_price, new_quantity):
        product_found = False
        for product in self.inventory:
            if product.product_id == product_id:
                product_found = True
                product.name = new_name
                product.price = new_price
                product.quantity_available = new_quantity
                print("\n============Product updated successfully.============")
                break

        if not product_found:
            print("\n===========Product not found.============")
            return

        # Update product details
        for product in self.inventory:
            if product.product_id == product_id:
                product.name = new_name
                product.price = new_price
                product.quantity_available = new_quantity
                print("\n============Product updated successfully.============")
                break

    def view_inventory(self):
        # Display product list
        print("==============================================================\n \t\t\t === Products === \n")
        for product in self.inventory:
            print(f"ID: {product.product_id}\t Name: {product.name}\t Price: {product.price}\t Quantity: {product.quantity_available}")
        print("==============================================================")
