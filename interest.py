'''
a=input("enter the string: ").split()
count=0
for i in a:
    count += 1
print(f"the string contains {count} words")
'''

principal=int(input("Enter the principal: "))
interest =int(input("Enter the interest: "))
time_period= int(input("Enter the time period: "))
n=int(input("Enter the compound growth: "))
amount = principal * (1 + interest/(100 * n)) ** (time_period *n)
compound_interest = amount - principal
print(compound_interest)


