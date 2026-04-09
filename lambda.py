':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::LAMBDA:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'

'It is an anonymus function , it can take n number of arguments but have only one expression and can be written in a single line'
'SYNTAX: lambda args : expression'
'''
number= lambda so : so + 10
print(number(10))
'''
'''
numbers=lambda x,y : x>y 
print(numbers(10,1))
'''
'''
number=lambda x,y,z : x+y+z
print(number(10,9,8))
'''
'''
difference = lambda a,b : a-b
print(difference(20,18))
 '''
'''
product = lambda h,k : h * k
print(product(23,84))
'''
'''
result = lambda l,m: l/m
print(result(15,5))
'''
'::::::::::::::::::::::::::::::::::::::::::::::LIST COMPREHENSION:::::::::::::::::::::::::::::::::::::::::::::::::::'
'this offers the shortest syntax when you want to create a new list from the exsisting list '
'SYNTAX  :   var_name = [expression loop and condition]'
'''
my_list=[1,5,23,4,35,5777,356,5]
derived_list=[j for j in my_list if j%2 !=0]
print(derived_list)
'''



