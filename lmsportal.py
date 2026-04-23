class Person:
    def __init__(self, name, education,age):
        self.name = name
        self.education = education
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Education: {self.education}, Age: {age}")


class Students(Person):
    def __init__(self, name, education, age, student_id):
        super().__init__(name, education,age)
        self.age = age
        self.student_id = student_id
        self.courses=[]
    def display(self):
        super().display()
        print(f"Student ID: {self.student_id}")
    
    def enrollcourses(self,course):
        self.courses.append(course)
        print(f"{self.name} enrolled in the {course}")
    def viewcourses(self):
        print(f"{self.name}'s courses : ")
        for c in self.courses:
            print("-",c)

name=input("enter your name: ")
age=input("enter your age: ")
education =input("enter you qualification: ")
student_id=input("enter student id: ")
obj=Students(name,education,age,student_id)
number=int(input("enter number of courses you want to enroll: "))
for i in range(number):
    course=input(f"enter the course{i+1}: ")
    obj.enrollcourses(course)
obj.display()
obj.viewcourses()

            
        


'''class Professors(Person):
    def __init__(self, name, education, age, employee_id, courses_train):
        super().__init__(name, education)
        self.age = age
        self.employee_id = employee_id
        self.courses_train = courses_train

    def prodetails(self):
        print(f"Name: {self.name}, Age: {self.age}, Employee ID: {self.employee_id}, Courses Trained: {self.courses_train}")


obj = Students("Harshith", "BTech", 21, 1075, "pfs")
obj.studetails()

obj1 = Professors("Teja", "MTech", 29, 1, "pfs")
obj1.prodetails()
'''
