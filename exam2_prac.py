'''
n = int(input("enter the number: "))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(n):
    print(fibonacci(i), end=" ")
'''
'''
n=int(input("Enter the number: "))
def fact(n):
    if n==0 or n==1:
        return n
    return n*fact(n-1)
print(fact(n))
'''
'''
number=int(input("enter the number: "))
def sum(number):
    if number ==1:
        return 1
    return number+sum(number-1)
print(sum(number))
'''

number = int(input("Enter the number: "))

def even(number):
    if number == 0:
        return "Even"
    if number == 1:
        return "Odd"
    return even(number - 2)

print(even(number))















