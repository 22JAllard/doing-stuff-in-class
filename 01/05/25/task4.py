# Order = Class
#   Private
#     OrderNumber: String
#     OrderDate: Date
#     ProductsOrdered: Array Of Product
#     NumberOfItemsOrdered: Integer
#     Status: OrderStatus
# End Class
# OrderStatus = Class
#   Private
#     HasShipped: Boolean
# End Class
# Product = Class
#   Private
#     ProductID: String
#     ProductPrice: Currency
# End Class

# product1 🡨 new Product("beans", 0.45)
# product2 🡨 new Product("eggs", 1.25)

# myOrder 🡨 new Order(1, "1/1/17")
# myOrder.OrderItem(product1)
# myOrder.OrderItem(product2)
# Output(myOrder.getOrderStatus())
# Output(myOrder.getOrderItemID(1))
# Output(myOrder.getOrderItemPrice(1))

# Output(myOrder.getOrderItemID(2))
# Output(myOrder.getOrderItemPrice(2))

# class Order():
#     def __init__(self, ordernumber, orderdate, productsordered, numberofitemsordered, status):
#         self.ordernumber = ordernumber
#         self.orderdate = orderdate
#         self.productsordered = productsordered
#         self.numberofitemsordered = numberofitemsordered
#         self.status = status

#     def orderitem():


#     def getorderstatus():


#     def getorderitemid():


#     def getorderID():
        

#     def getorderitemprice():
        

# class OrderStatus():
#     def __init__(self, hasshipped):
#         self.hasshipped = hasshipped

# class Product():
#     def __init__(self, productID, productprice):
#         self.productID = productID
#         self.productprice = productprice

# product1 = Product("beans", 0.45)
# product2 = Product("eggs", 1.25)

# myorder = Order(1,"1/1/17")
# myorder.orderitem(product1)
# myorder.orderitem(product2)
# print(myorder.getorderstatus())
# print(myorder.getorderID(1))
# print(myorder.getorderitemprice(1))

# print(myorder.getorderitemid(2))
# print(myorder.getorderitemprice(2))

#correct version
class Order:       
  def __init__(self, s, d):
    self.__orderNumber = s
    self.__orderDate = d
    self.__numberOfItemsOrdered = 0
    self.__productsOrdered = [Product("",0.0)] 
    self.__status = OrderStatus()

  def orderItem(self, p):
    self.__numberOfItemsOrdered += 1
    i = self.__numberOfItemsOrdered
    self.__productsOrdered.append(p)

  def getOrderStatus(self):
    return self.__status.getHasShipped()

  def getOrderItemID(self, i):
    return self.__productsOrdered[i].getProductID()

  def getOrderItemPrice(self, i):
    return self.__productsOrdered[i].getProductPrice()
    
class OrderStatus:
  def __init__(self):
    self._hasShipped = False

  def getHasShipped(self):
    return self._hasShipped
      
class Product:
  def __init__(self, ID, Price):
    self.__productID = ID
    self.__productPrice = Price
    
  def getProductID(self):
    return self.__productID

  def getProductPrice(self):
    return self.__productPrice

product1 = Product("beans", 0.45)
product2 = Product("eggs", 1.25)

myOrder = Order(1,"1/1/17")
myOrder.orderItem(product1)
myOrder.orderItem(product2)
print(myOrder.getOrderStatus())
print(myOrder.getOrderItemID(1))
print(myOrder.getOrderItemPrice(1))

print(myOrder.getOrderItemID(2))
print(myOrder.getOrderItemPrice(2))