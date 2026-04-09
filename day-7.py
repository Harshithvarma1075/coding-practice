'''list_1 = ["Kartheek","surya",["kumar",["raju","varun"],"akash","shyam"]]
print(list_1[2][1][0][3])'''
'''
print(9+8)
print("Pyhton"+''Language")
print([1,2]+[3,4])

concatenation ------>
This is nothing but,  a (+) behavior....
--------------------------------------
case-1
-------
Integers ---- this will act as addition for the int
print(9+8)
---------------------------------------
case - 2
for the other data types(we have to use same types ) this (+) act as concatenation
if we access concat between two different data types it will give error.
print("Teja" + [1,2]) #TypeError: can only concatenate str (not "list") to str
print(23.5+"kartheek") #TypeError: unsupported operand type(s) for +: 'float' and 'str'
<--------------------------------------------------------------------------------------------------------------------------->
Tuple() ------> It is a collection of different datatypes and this represented by () and seperated by (,)
Thing = (1,"Teja",[2,4],(7,8))
print(Thing)
print(Thing[3][0])
<--------------------------------------------------------------------------------------------------------------------------->
Thing = (12,89,"Pyhton",(23,"Kartheek",[67,"Pyhton is a Language",(7,8)],[8,("Pyhton",[34,9])]))
print(Thing)
print(Thing[3][2][1][9])
<--------------------------------------------------------------------------------------------------------------------------->
num = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print(f"Before swapping num = {num} and num2 = {num2}")

num , num2 = num2 , num

print(f"After swapping num = {num} and num2 = {num2}")
<--------------------------------------------------------------------------------------------------------------------------->
leap_year = int(input("Enter any year: "))
if (leap_year % 4 == 0 and leap_year % 100 != 0) or leap_year % 400 == 0:
    print(f" Yes, {leap_year} is a Leap Year ")
else:
    print(f"No, {leap_year} is not a Leap Year")
'''
