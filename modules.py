#::::::::::::::::::::::::::::::::::::::::::;MODULES:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::;

#a module in python is simply file that contains python code (functions) which contains the logic along with variables and calsses, we use them when we need without writing entire knowledge and use import statement

#to use modules we have to use the keyword "import" import module_name

#types of modules:
#1.user defined , 2.built in functions

#user defined -- here we write our own module and then import in other file to avoid again writing the logic 
'''
import product as a
print(f"product of two numbers is: {a.multiply(56,78)}")
print(f"the sum of two numbers is: {a.add(34,44)}")
print(f"the difference of two numbers is: {a.sub(765,99)}")
print(f"the quotient of two numbers is: {a.divide(100,2)}")
print(f"the result of two numbers is: {a.result(56,2)}")
print(f"the power of a number is: {a.power(55,2)}")
'''
'''
import function as f
print(f.prime(1075,0))
'''

#built in functions -- these are modules that we get at the time of installing python , they contain several functions that can make our job easy , we can simply call and use them
'''
import math
print(math.sqrt(225))
'''
import random
number=3
while number>=1:
    number=number-1
    n=int(input("enter your number: "))
    m=random.randint(1,250)
    print(m)
    if m==n:
        print("congratulations you have gussed correct number")
    else:
        print(f"you gussed wrong number , still {number} attempts remaining")
else:
    print("Better luck next time")



