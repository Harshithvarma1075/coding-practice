'1.Dictionary is a datatype that is used to store the data in the form of key,value pairs'
'we create dict like d={"name":"varma", "age":21} , we can access elements in dict with the help of their keys d['name'] =varma , d['age'] =21'

'2.var -- variable can not be numbers , variables can not have gaps , variables without defination can not be used , we can use symbols like _ '

'3.and   if both conditions are true then and will give true ,or  if anyone of the two conditions is true then we get true'
'if a>3 and  a<5   , if a>3 or a<5 '

'4. continue-skips iteration
'''ex for i in range(1,10):
        if i==5:
            continue
        print(i)

        o/p 1,2,3,4,6,7,8,9'''
'break - exit loop
 '''ex for i in range(1,10):
        if i==5:
            break
        print(i)

        o/p 1,2,3,4'''
'range -generates sequence of numbers'

'''palindrome
  num=input("enter string: ")
  empty=""
  for i in num:
      empty = i+empty
 if empty == num:
     print("palindrome")
else:
    print("not palindrome")
'''
'''prime
     num=int(input("enter the number: "))
     count =0
     for i in range(1,num+1):
          if num%i == 0:
            count += 1
    if count == 0:
       print("prime")
    else:
      print("not prime")
'''

'''fibbanocci
num=int(input("enter number: "))
num1=0
num2=1
print(num1,num2,end = " ")
for i in range(1,num):
   num3=num1+num2
   num1=num2
   num2=num3
   print(num3,end= " ")
'''
