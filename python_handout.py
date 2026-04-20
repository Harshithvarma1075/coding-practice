#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::PRACTICE QUESTIONS WEEK1::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

'''
length=int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: ")) #AREA OF RECTANGLE
area = length * width
print(f"Area of triangle is {area}")
--------------------------------------------------------------------------------------------------------------------------
'''
'''
name=input("enter the name: ")
age=int(input("enter the age: ")) #TAKING NAME AND AGE
print(f"greetings {name} ,your age is {age}")
-------------------------------------------------------------------------------------------------------------------------------
'''
'''
number=int(input("enter the number: "))
if number%2 == 0:
    print(f"{number} is even")   #EVEN OR ODD
else:
    print(f"{number} is odd")
----------------------------------------------------------------------------------------------------------------------------------
'''
'''
numbers=eval(input("enter the list: "))
numbers=numbers.sort()
print(f"the maximum number is {numbers[-1]} ,and minimum number is {numbers[0]}")  #PRINTING MAX AND MIN IN LIST
------------------------------------------------------------------------------------------------------------------------------------
'''
'''
number=input("enter the number: ")
empty=""
def palindrome(number,empty):
    for i in str(number):
        empty= i + empty
    if empty == number:
        print(f"the number {number} is palindrome")  #PALINDROME
    else:
        print(f"the number {number} is not palindrome")
palindrome(number,empty)
------------------------------------------------------------------------------------------------------------------------------------
'''
'''
principal=int(input("Enter the principal: "))
interest =int(input("Enter the interest: "))
time_period= int(input("Enter the time period: "))
n=int(input("Enter the compound growth: "))
amount = principal * (1 + interest/(100 * n)) ** (time_period *n)  #INTEREST
compound_interest = amount - principal
print(compound_interest)
-------------------------------------------------------------------------------------------------------------------------------------
'''
'''
days = int(input("Enter number of days: "))
years = days // 365
remaining_days = days % 365
weeks = remaining_days // 7 
days_left = remaining_days % 7               #NUMBER OF DAYS , YEARS ,WEEKS
print("Years:", years)
print("Weeks:", weeks)
print("Days:", days_left)
--------------------------------------------------------------------------------------------------------------------------------------
'''
'''
numbers=eval(input("enter the list of numbers: "))
sum=0
for i in numbers:
    if i>0:
        sum += i                              #SUM OF POSITIVE NUMBERS IN A LIST
    else:
        pass
print(f"the sum of positive numbers in the list is {sum}")
--------------------------------------------------------------------------------------------------------------------------------------
'''
'''
sentence=input("enter the sentence: ").split()
length =len(sentence)
print(f"there are {length} number of words in the sentence")         #NUMBER OF WORDS IN A SENTENCE
-----------------------------------------------------------------------------------------------------------------------------------------
'''
'''
a=int(input("enter the number1: "))
b=int(input("enter the number2: "))
a,b=b,a                                              #SWAPPING THE NUMBERS
print(a)
print(b)
------------------------------------------------------------------------------------------------------------------------------------------------------
'''
#:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::PRACTICE QUSTIONS WEEK2::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
