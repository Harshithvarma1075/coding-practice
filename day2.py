''' number = int(input("enter a number: "))
count = 0
for i in range(1,number+1):
    if number%i == 0:
        count += 1
if (count==2):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")
'''

'prime number generator'

'''for i in range(2,100):
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count +=1
    if (count==2):
        print(f"{i} is a prime number")
    else:
        print(f"{i} is not a prime number")
 '''   

'''a=[1057,197,9,86,17673]
for i in a:
    count = 0
    for j in range(1,i+1):
        if i%j == 0:
            count += 1
    if count == 2:
        print(f"{i} is a prime number")
    else:
        print(f"{i} is not a prime number")
    '''


'''
a=[2,356,8,6,3,2,8]
empty=[]
for i in a:
    if i not in empty:
        empty.append(i)
print(empty) 
'''

me=153
arm =0
length=len(str(me))
for i in str(me):
    arm += int(i) ** length
if(arm == me):
    print(f"{me} is amstrong number")
else:
    print(f"{me} is not amstrong number")
              
        
