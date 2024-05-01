class Product:
    def __init__(self,name='',price=0,Quantity=0,Revenue=0,ItemID=0,sales=0):
        self.name=name
        self.price=price
        self.ItemID=ItemID
        self.Revenue=Revenue
        self.Quantity=Quantity
        self.sales=sales
class Inventory:
    def __init__(self):
        self.items=[]
        
    # Method to display product details
    def display_details(self):
        print("\n===== PRODUCTS ===== ")
        print("ID\t \tProduct\t \t Price\t \t \t in stock \t \t sold")
        for item in self.items:
            print(item.ItemID,"\t \t",item.name,"\t\t ",item.price, " EGP\t \t",item.Quantity, "\t \t \t",item.sales)

    # Method to add new product 
    def add_product(self,name,price,Quantity,Revenue,ItemID,sales):
        item=Product(name,price,Quantity,Revenue,ItemID,sales)
        self.items.append(item)
        #print("-----",self.items[-1].ItemID)
        return item
    
    # Method to remove product 
    def remove_product(self,index):
      for i in self.items:
          if i.ItemID==index:
              self.items.remove(i)
              print("Product removed successfully\n")
        #print("-----",self.items[-1].ItemID)
        

    # Method to update product using id for product
    def StockUpdate(self,index,NewStock):
        if self.items[index].Quantity>NewStock:
            self.items[index].sales=self.items[index].Quantity-NewStock
            self.items[index].Revenue=self.items[index].sales*self.items[index].price
        self.items[index].Quantity=NewStock
    
    # Method to create sales report 
    def SalesReport(self,index):    
        print("This Product was sold for ",self.items[index].sales," and has total Revenue of ",self.items[index].Revenue," EGP")

inventory = Inventory()