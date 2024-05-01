from Cart import ShoppingCart
from Inventory import inventory
def display_menu():
    # Function to display the main menu options
    print("\n===== MENU =====")
    print("1. Browse Products")
    print("2. View Cart")
    print("3. Place Order")
    print("4. Exit")


def main():
    # Create an instance of Inventory to manage products
    cart = ShoppingCart()    # Create an instance of ShoppingCart to manage the cart
    # # Sample products
    # inventory.add_product(Product(1, "Laptop", 1000, 5))
    # inventory.add_product(Product(2, "Headphones", 100, 10))
    # inventory.add_product(Product(3, "Mouse", 20, 15))
    ItemID=0
   
    while True:
          # Display the main menu
        display_menu()
        choice = input("Enter your choice: ")  # Get user input for menu choice
        while choice == '1':
            inventory.display_details()
            product_create = int(input("Choose \n 1 to create new product \n 2 to update inventory \n 3 to remove product: "))
            
            if product_create == 1:
                name=input("Please Enter product Name: ")
                price=float(input("Please Enter Product Price: "))
                
                while(price<=0):
                    print("Sorry, But Products can't be listed for free \n")
                    price=float(input("Please Enter Product Price: "))
                    
                quantity=int(input("Please Enter your product quantity: "))
                
                while(quantity<=0):
                    print("Sorry, But Products can't be listed for free \n")
                    quantity=int(input("Please Enter your product quantity: "))
                    
                ItemRevenue=0
                ItemSales=0
                inventory.add_product(name,price,quantity,ItemRevenue,ItemID,ItemSales)
                ItemID+=1
                print("Item added to Sharks Inventory successfuly \n")
                choice=0
                inventory.display_details()
                
            elif product_create==2:
                id=int(input("Please Enter your product ID: "))
                flag=None
                
                for index, i in enumerate(inventory.items):
                    if i.ItemID == id:
                         NewStock=int(input("Please Enter your new Stock Quantity: "))
                         inventory.StockUpdate(index,NewStock)
                         flag=1
                if flag!=None:
                    pass
                else:
                    print("ID not Found\n")
                    
            elif product_create ==3:
                id=int(input("Please Enter your product ID: "))
                inventory.remove_product(id)
                display_menu()
                
        while choice == '2':
            print("\n===== CART =====")
            cart.display_cart()

        while choice == '3':
            print("\n===== ORDER SUMMARY =====")
            if not cart.items:
                print("Your cart is empty.")
            else:
                cart.display_cart()
                total_amount = cart.calculate_total()
                print(f"Total amount: ${total_amount}")
                print("Order placed successfully! Thank you for shopping with us.")
                cart.items = []  # Clear cart after placing order

        while choice == '4':
            print("Thank you for using our application. Goodbye!")
            break

        
        #print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()