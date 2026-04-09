#A simple case study on Price calculator

#Detalis of the Customers
print("<---------------------------------------------------------------->")
Customer_name = (input("\nEnter your Name: "))
Price = float(input("\nEnter the Price of the Product: "))
Quantity = int(input("\nEnter the Quantity: "))
Discount = float(input("\nEnter the Discount: "))
#Calculation Part
Total_Price = Price*Quantity
Discount_amount = (Discount / 100)*Total_Price
Total_amount = Total_Price - Discount_amount
#Ouput
print("<---------------------------------------------------------------->")
print("\nCustomer_name: ",Customer_name)
print("\nPrice: ",Price)
print("\nQuantity: ",Quantity)
print("\nDiscount Given: ",Discount)
print("\nTotal_amount: ",Total_amount)
print("\n<-------------------------------------------------------------->")






