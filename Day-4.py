'''Today's topic
Operators
different type of operators
conditional statements --> if,elif,else,nested if '''
''' Operators --> An operator is a symbol that performs one or more values (operand) and produces a result

Operators are primarily used:
-->Calculate values
-->Compare values / inputs
-->Make decisions
-->Control the program flow

There are major seven categories of Operators iin python
-->Arithmetic Operators
-->Assignment Operators
-->Comparision Operators
-->Membership Operators(in,not in)
-->Identify Operators(is,is not)
-->Bitwise Operators
-->Logical Operators(and,or,not)

#Arithmetic Operators --> Arithmetic Operators perform mathematical operations:
# + --> Addition , - -->Subtraction, * --> Multiplication, / --> Division
# ** --> Exponent , % --> Modulus , // --> Integer Division

a = 5
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b) #return the result in float values--> return quotient 
print(a ** b) #return the exponential values
print(a % b) # Modules division --> return remainder
print(a // b)   # Flooring / Integer division --> returns Quotient discards

# f-string notation
num1 = int(input("Enter the first value"))
num2 = float(input("Enter the second value"))
result = (num1+num2) *4
print("The result is",result) # Standard notation
#f-string notation
print(f'The result is {result}')
print(f'The result of {num1} and {num2} is {result},{num1*num2}')

#Assignment Operators
# --> = Assign, += Addition Assigment
# -= --> Subtract Assigment,  *= , /= , %= , //= , ** =

#They are majorly used for code repetitions in application usage

a = 4
b = 3
a += 2 # --> a = a+2
print(a)
b += a
print(b)
# In a similar way check for -=,*=,**=,/=, %=, //=

b -= 3 #b = b-3
print(b)
print(f'The updated values of a and b are {a} and {b}')
b *= a # b = b*a
print(b)
b **= a
print(b)


#Relational or Comparision Operators --> where they always return the boolean
#values (True/False)

# == is equal to , != not equal to
# < less than, > greater than, >= greater than or equal to, <= Less than or equal to

a = int(input("Enter the value: "))
b = int(input("Enter another value: "))
print(a == b)
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)


#MemberShip Operators --> They check for the existance of an object in a
# collection --> in, not in

a = "codegnan"
print(type(a))
print('a' in a)
print('z' in 'saketh')
print('z' not in 'codegnan')

b = [12,6,3,4]
c = int(input("Enter the value"))
print(c)
print(c in b)
print(c not in b)



#Logical operator --> They are used to combine multiple conditions
#and, or, not

age = int(input("Enter the Age: "))
vote_right = True
print(age>=18 and vote_right,)#both condition to be True then only True
print(age>18 or vote_right)#any one condition is True then result is True
print(not vote_right)


#Identify Operators --> They check the memory location and validate we used
#(id) function it is different form == operator -> is, is not

a = [1,2,4]
b = [1,2,4]
print(a == b)
print(id(a))# return the identity of an object
print(id(b))
print(a is b)# here it will check the memory location of the data 
print(b is not b)

c = b
print(c)
print(id(c))
print(c is b)

#Bitwise Operstors --> Bitwise AND &, Bitwise OR | perform bitwise operation
# we get the result (remainder the binary conversion)
print(5&3)
print(bin(5)) #returns binary number
'''

#Task --> Now you have all operators create a Checker Task
#git add .
#git commit -m"operators usage"
#git push -u origin main 





















