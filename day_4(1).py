'''
if statement --> This (if statement)is used to check any condition, if the condition becomes true
 then it will enter inside the (is statement)
 <------------------------------------------------------------------------------------------------------------------------------->
age = int(input("Enter your age: "))
if age >= 18:
    print("Your age is 18 or above")
<------------------------------------------------------------------------------------------------------------------------------->
student_att = int(input("pls enter your sem attendence: "))
if student_att >= 75:
    print("you can directly sit in the sem exam")
<------------------------------------------------------------------------------------------------------------------------------->
balance_amount = int(input("Enter the balance amount: "))
if balance_amount >1000:
    print("ypu can make a payment")
<------------------------------------------------------------------------------------------------------------------------------->
age = int(input("Enter the age: "))
if age >= 18:
    print("you can vote")
<------------------------------------------------------------------------------------------------------------------------------->
'''
'''
if-else statement--> This is also called a fall back statement which only excute when the (if statement)
becomes false
<------------------------------------------------------------------------------------------------------------------------------>
age = int(input("Enter  the age: "))
if age >= 18:
    print(f"You age is {age} can vote")
else:
    print(f"you cannot vote and have to wait for {18-age} years to vote")
<------------------------------------------------------------------------------------------------------------------------------->
total_amount = int(input("Enter the Total Shopping amount: "))
if total_amount >= 149:
    print("No delivery cost")
else:
    print(f"add {149 - total_amount} more to get Free Delivery")
<------------------------------------------------------------------------------------------------------------------------------->
Phone_number = int(input("Enter the Total amount: "))
if Phone_number < 500:
    print(f"Please enter a valid Total amount. add {500 - Phone_number} number to get a offer")
else:
    print("Offer applied")
<------------------------------------------------------------------------------------------------------------------------------->
User_choice = int(input("Enter the number you want to check: "))
if User_choice % 2 == 0:
    print(f"{User_choice} is even")
else:
    print(f"{User_choice} is odd")
'''
'''
if-elif-else statement(if + else)--> in the elif part, i can check one more condition
<------------------------------------------------------------------------------------------------------------------------------->
Student_marks = int(input("Enter the student marks: "))
if Student_marks >= 90:
    print("You got A+ grade")
elif Student_marks >= 75 and Student_marks < 90:
    print("You got A grade")
elif Student_marks >= 60 and Student_marks < 75:
    print("You got B+ grade")
else:
    print("Your are Fail")
<------------------------------------------------------------------------------------------------------------------------------->
(Version 1)
First = int(input("Enter the First Number : "))
Second = int(input("Enter the Second Number : "))
Symbol = input("Enter the Calculation you want Do(+,-,*,/,%) : ")
if Symbol == "+" :
     print(f" {First + Second} is your answer")
elif Symbol == "-" :
    print(f" {First - Second} is your answer")
elif Symbol == "*" :
    print(f" {First * Second} is your answer")
elif Symbol == "/" :
    print(f"{First / Second} is your answer")
elif Symbol == "%" :
    print(f"{First % Second} is your answer")
else:
    print("Enter Valid data")
<------------------------------------------------------------------------------------------------------------------------------->
(Version 2)
num_1 = int(input("Enter the Fisrt number: "))
num_2 = int(input("Enter the Second number:"))
user_choice = int(input("Enter your choice \n1.add \n2.sub \n3.mul \n4.div \nThe Calculation you have chosen is "))
if user_choice == 1:
    print(f"The Sum of {num_1} and {num_2} is {num_1 + num_2}")
elif user_choice == 2:
    print(f"The Subtraction of {num_1} and {num_2} is {num_1 - num_2}")
elif user_choice == 3:
    print(f"The Multiplication of {num_1} and {num_2} is {num_1 * num_2}")
elif user_choice == 4:
    print(f"The Division {num_1} and {num_2} is {num_1 / num_2}")
else:
    print("Enter the valid data")
<------------------------------------------------------------------------------------------------------------------------------->
(postive number,negative number)
User_choice = int(input("Enter the Number: "))
if User_choice < 0:
    print(f"{User_choice} is Negative Number")
elif User_choice > 0:
    print(f"{User_choice} is Positive Number")
else:
    print(f"{User_choice} is 0")
<------------------------------------------------------------------------------------------------------------------------------->
'''



















    
