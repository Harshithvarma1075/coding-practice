num=int(input("Enter the number: "))
num1=0
num2=1
print(num1,num2,end=" ")
for i in range(num+1):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3,end=" ")
