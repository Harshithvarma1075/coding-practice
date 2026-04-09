':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::WAYS TO PASS ARGUMENTS IN A CALLING FUNCTION::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'''
num1 = 75
num2=10
def sum_num(a,b):
    print(a+b)
sum_num(num1,num2)   'in calling function the number of arguments should match with the keyword arguments , or else we will get error'

'''
'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::DEFAULT ARGUMENTS::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
''' it will take the default valuses from the arguments
name="varma"
def sum_num(name):
    print(name)
sum_num(name="harshith")
sum_num(name="rama")   'these are used for reusability , if we use the calling fuction after n number of lines still we get the output '
'''
'''
a=127
def even(a):
    if a%2 == 0:
        print(f"{a} is even number")
    else:
        print(f"{a} is odd number")
even(a= 178)
'''

'''
def prime(num,count):
    for i in range(1,num+1):
        if num%i == 0:
            count += 1
    if count == 0:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
prime(num=1075,count=0)
'''
'''
def any(num,num1,num2):
    print(f"num ={num} , num2={num2}, num1 ={num1}")
any(num2=92,num=88,num1=134)
'''
def age(*years):
    print(years)
age(18,32,55)


















