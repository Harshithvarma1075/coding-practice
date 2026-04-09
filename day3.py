'''
'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::TABLE::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'   
a=int(input("enter a number: "))
for i in range(1,11):
    print(f"{a} X {i} = {a*i}")
'''
':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::COUNT OF CAPITALS AND SMALL::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'''
an = "Python Is a Programming Language"
countu=0
countl=0
for ch in an:
    if ch.isupper():
        countu += 1
    elif ch.islower():
        countl += 1
print(f"there are total {countu} capitals letters")
print(f"there are total {countl} small letters")'''

':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::FINDING CAPITALS AND SMALL IN STRING::::::::::::::::::::::::::::;'
'''
an ="Python Is a Programming Language"
capitals=[]
small=[]
for ch in an:
    if ch.isupper():
        capitals.append(ch)
    elif ch.islower():
        small.append(ch)
print(capitals)
print(small)'''

'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::VALIDATING BANK PIN:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'''
hdfc_details={"name" : "varma", "pin" : "1075"}
print("welcome to hdfc bank")
print("enter the atm card")
hdfc_pin=input("enter the 4 digit pin: ")
if len(hdfc_pin) == 4:
    if hdfc_pin in hdfc_details["pin"]:
        print("correct pin")
    else:
        print("you have entered wrong pin")
else:
    print("invalid pin , enter 4 digit pin")
'''
':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::PERFECT NUMBER:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'

per=int(input("enter a number: "))
fact=0
for i in range(1,per):
    if per % i == 0:
        fact += i
if fact == per:
    print(f"{per} is a perfect number")
else:
    print(f"{per} is not a perfect number")












