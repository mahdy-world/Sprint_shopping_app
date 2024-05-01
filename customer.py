class Customer:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product, quantity):
        if quantity <= product.quantity_available:
            self.cart.append((product, quantity))
            product.quantity_available -= quantity
            print("\n============ Product added to cart successfully.============")
        else:
            print("\n============Insufficient quantity available. Product not added to cart.============")

    def remove_from_cart(self, product_id):
        for index, item in enumerate(self.cart):
            if item[0].product_id == product_id:
                current_quantity = item[1]
                print(f"Current quantity in cart: {current_quantity}")
                quantity_to_remove = int(input("Enter the quantity to remove: "))

                if quantity_to_remove > current_quantity:
                    print("Cannot remove more than what's in the cart.")
                elif quantity_to_remove == current_quantity:
                    self.cart.pop(index)
                    print("\n============Product removed from cart successfully.============")
                else:
                    self.cart[index] = (item[0], current_quantity - quantity_to_remove)
                    print(f"\n============{quantity_to_remove} units of product removed from cart successfully.============")
                break
        else:
            print("\n============Product not found in cart.============")

    def generate_cart_summary(self):
        # Display cart summary
        total_price = 0
        print("==============================================================\n \t\t\t === Cart Summary === \n")
        for item in self.cart:
            product, quantity = item
            total_price += product.price * quantity
            print(f"Product: {product.name}\t Quantity: {quantity}\t Price: {product.price * quantity}")
        print(f"Total Price: {total_price}")
        print("==============================================================")
