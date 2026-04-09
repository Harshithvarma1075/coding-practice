'''a=[1,2]
b=[1,2]
c=a
print(a is c)
print(id(a))
print(id(c))
'''
'''
number=int(input("enter the number: "))
count=0
for i in range(1,number+1 ):
    if number%i == 0:
        count +=1
if count == 2:
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
    
me=input("enter the string: ")
empty=""
for i in me:
    empty = i+empty
if empty == me:
    print("palindrome")
else:
    print("not palindrome")
'''

number = int(input("enter the limit: "))
num1=0
num2=1
print(num1,num2,end=" ")
for i in range(1,number):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3,end=" ")
