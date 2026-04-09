#Customer Details
name = input("Enter customer name: ")
customer_id = input("Enter customer ID: ")
phone = input("Enter phone number: ")
cylinders = int(input("Enter number of cylinders: "))
days = int(input("Enter delivery days: "))

#Calculation Part
price_per_cylinder = 800
delivery_charge = 50
is_valid = (len(phone) == 10) and (cylinders > 0)
total_cost = cylinders * price_per_cylinder
urgent_charge = (days <= 2) * 100
normal_charge = (days > 2) * delivery_charge
total_cost = total_cost + urgent_charge + normal_charge

# Output 
print("\n----- Booking Details -----")
print("Name:", name)
print("Customer ID:", customer_id)
print("Phone:", phone)
print("Cylinders:", cylinders)
print("Delivery Days:", days)
print("Valid Details:", is_valid)
print("Total Cost:", total_cost)
