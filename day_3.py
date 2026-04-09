#Case Study on Percentage calculator
#Student Details
print("\n<******************************************************************************>")
Student_Name = input("Enter the Student_name: ")
Student_ID = int(input("Enter the Student_ID: "))
print("\n")
Subject_1 = float(input("Enter the Subject_1 Marks: "))
Subject_2 = float(input("Enter the Subject_2 Marks: "))
Subject_3 = float(input("Enter the Subject_3 Marks: "))
Subject_4 = float(input("Enter the Subject_4 Marks: "))
Subject_5 = float(input("Enter the Subject_5 Marks: "))
#Calculation Part
Total_Marks = Subject_1+Subject_2+Subject_3+Subject_4+Subject_5
Percentage = Total_Marks / 5
#Output
print("\n<******************************************************************************>")
print("\nStudent_Name: ",Student_Name)
print("\nStudent_ID: ",Student_ID)
print("\nTotal_Marks: ",Total_Marks)
print("\nPercentage: ",Percentage)
print("\n<******************************************************************************>")
