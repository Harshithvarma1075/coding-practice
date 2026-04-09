':::::::::::EVEN NUMBER::::::::::::::::::::::::::::'
'''
number=int(input("Enter the number: "))
def even(number):
    if number%2 == 0:
        print(f"{number} is a even number")
    else:
        print(f"{number} is odd number")
even(number)
'''
':::::::::::::::::::PRIME NUMBER::::::::::::::::::'
'''
number=int(input("enter the number: "))
count=0
def prime(number,count):
    for i in range(1,number+1):
        if number%i ==0:
            count += 1
    if count == 2:
        print(f"{number} is prime")
    else:
        print(f"{number} is not prime")
prime(number,count)
'''
':::::::::::::::::::::::FIBBANOCCI::::::::::::::::::::::::::::::'
'''
number=int(input("Enter the number: "))
num1=0
num2=1
def fib(number,num1,num2):
    print(num1,num2,end = " ")
    for i in range(1,number-1):
        num3=num1+num2
        num1=num2
        num2=num3
        print(num3,end=" ")
fib(number,num1,num2)
'''
'::::::::::::::::::::::::::::::::::PALINDROME:::::::::::::::::::::::::::::::::::'
'''
me = input("enter the string: ")
empty=""
def palindrome(me,empty):
    for i in me:
        empty = i + empty
    if empty == me:
        print(f"{me} is a palindrome")
    else:
        print(f"{me} is not a palindrome")
palindrome(me,empty)
'''
'::::::::::::::::::::::::::::::::::::::::::::::::::* pattern::::::::::::::::::::::::::::::"'
'''
number=int(input("enter the number: "))
def star(number):
    for i in range(1,number+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print( )
star(number)
'''
'::::::::::::::::::::::::::::::::::::::::::::::::::number of words in a string:::::::::::::::::::::::::'
''' 
word=input("Enter the string: ").split()
number=0
def count(word,number):
    for i in word:
        number += 1
    print(f"the string contains {number} of words")
count(word,number)
'''
