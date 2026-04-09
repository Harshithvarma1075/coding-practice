':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::RIGHT TRIANGLE::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'''
num=int(input("enter number: "))
for j in range(num):
    for i in range(j):
        print("*", end =" ")
    print()
'''
':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::RIGHT NUMBER TRIANGLE::::::::::::::::::::::::::::::::::::::::::::::'
'''
num=int(input("enter the number: "))
for j in range(num):
        for i in range(1,j):
            print(i,end = " ")
        print( )
'''
'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::SQUARE::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'''
num=int(input("enter the number: "))
for j in range(num):
        for i in range(num):
                print("*", end=" ")
        print( )
'''
':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::REVERSE:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'''
num=int(input("enter the number: "))
for i in range(num):
    for j in range(num-i):
        print("*", end = " ")
    print( )
'''
':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::PYRAMID::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'''
num=int(input("enter the number: "))
for i in range(num):
        print(" "  * (num-i) , end =  "" )
        for j in range(i+1):
              print("*",end ="")
        print( )
'''



hdfc_details={"name" : "varma", "pin" : "1075","balance":12000}
print("welcome to hdfc bank")
print("enter the atm card")
hdfc_pin=input("enter the 4 digit pin: ")
if len(hdfc_pin) == 4:
    if hdfc_pin in hdfc_details["pin"]:
        user_choice=int(input("Enter \n1.withdraw: "))
        if user_choice == 1:
            amount_w= int(input("Enter the amount you want to withdraw: "))
            if amount_w <= hdfc_details['balance']: 
               hdfc_details['balance'] -= amount_w
               print(f"money withdrawn ,your balance is {hdfc_details['balance']}")
    else:
        print("you have entered wrong pin")
else:
    print("invalid pin , enter 4 digit pin")
