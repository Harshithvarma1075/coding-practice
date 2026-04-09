''':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;FUNCTIONS:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;;;;;'''

''' FUNCTIONS IS A BLOCK OF CODE WHICH IS REUSABLE , THESE ARE TWO TYPES
    1.IN-BUILT FUNCTIONS
    2.USER DEFINED FUNCTIONS
    
1.BUILT IN :
------------------

    THEY COMES WITH THE PROGRAM ITSELF, THEY ARE ALREADY DEFINED  EX. PRINT(), APPEND(),SORT()................

2.USER DEFINED :
--------------------

    THEY ARE DEFINED BY THE USER AS PER HIS REQUIRMENTS EX. ADD FUNCTION FOR ADDING TWO NUMBERS.

NOTE:
--------

IT STARTS WITH THE def KEYWORD FOLLOWED BY FUNCTION NAME EX,def add():
AND IT HAS CALLING FUNCTION

SYNTAX:
------------
def fun_name():
    ----------------
    ----------------
fun_name()

|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||'''
'1.EVEN NUMBERS USING FUNCTIONS'
'''
a=int(input("Enter the number: "))
def even(a):
    if a%2 == 0:
        print(f"{a} is even number")
    else:
        print(f"{a} is odd number")
even(a)

'''

'''2.PRIME NUMBER USING FUN
a=int(input("enter the number: "))
count=0
def prime(a,count):
    for i in range(1,a+1):
        if a%i ==0:
            count += 1
    if count == 2:
        print(f"{a} is prime number")
    else:
        print(f"{a} is not prime number")
prime(a,count)
'''

'''3.PALINDROME USING FUN

me=input("enter string: ")
empty = ""
def palindrome(me,empty):
    for i in me:
        empty=i+empty
    if empty == me:
        print(f"{me} is a palindrome")
    else:
        print(f"{me} is not a palindrome")
palindrome(me,empty)

'''
'''4.FIBBANOCCI USING FUNC'''
number=int(input("enter the number: "))
num1=0
num2=1
def fib(number,num1,num2):
    print(num1,num2,end=" ")
    for i in range(number):
        num3=num1+num2
        num1=num2
        num2=num3
        print(num3,end=" ")
fib(number,num1,num2)
    












