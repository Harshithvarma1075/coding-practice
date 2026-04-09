'''s="Pyhton Is a programming language"
print(s.lower())
print(s.upper())
print(s.title())
print(s.capitalize())
print(s.casefold())
print(s.split("-"))
'''
':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::BREAK:::::::::::::::::::::::::::::::::::::::::'
'''
for i in range(1,10):
    print(i)
    if i == 5:
        break 'used to exit from the loop when condition satisfied' '''

':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::BREAK IN LIST:::::::::::::::::::::::::::::'
'''
list=[75,101,87,112,102,103,96,74,126]
for i in list:
    print(i)
    if i == 112:
        break
'''
':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::CONTINUE::::::::::::::::::::::::::::::::::'
'''
for i in range(1,10):
    if i==5 :
        continue 'used to skip that one iteration'
    print(i)

a=[12,23,435,5]
for i in a:
    if i == 435:
        continue
    print(i)
'''
'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::PASS:::::::::::::::::::::::::::::::::::::::::::::::'
'''
for i in range(1,10):
    print(i)
    if i==9:
        pass ' this is called as space holder , used incase any statement like if , for , else, elif  are incompleted and to avoid indentation error'
'''
'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::ELSE  ----FOR:::::::::::::::::::::::::::::'
'''
for v in range(1,10):
    print(v)
else:
    print("for loop completed")'it will fallback after completion of all loops'
    '''

'::::::::::::::::::::::::::::::::::::::::::::::::::::::::WHILE:::::::::::::::::::::::::::::::::::::::::::::::::'
'''
number = 1
while number<45:
    print(number)
    number += 1
'''
':::::::::::::::::::::::::::::::::::::::::::::::::::::::FIBANOCCI::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'''
num=int(input("Enter the number: "))
num1=0
num2=1
print(num1,num2,end=" ")
for i in range(num+1):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3,end=" ")
'''

':::::::::::::::::::::::::::::::::::::::::::::::::::



















