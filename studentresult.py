class Student:
    def __init__(self,name,marks):
        self.name = name
        self.__marks = marks
    def set_marks(self,marks):
        self.__marks = marks
    def get_grade(self):
        if self.__marks >=75:
            return 'Distinction'
        elif self.__marks >=50 and self.__marks<75:
            return 'Pass'
        else:
            return 'Fail'
    def save_result(self):
        with open('result.txt','a') as f:
            f.write(f"{self.name},{self.__marks},{self.get_grade()}\n")
    def get_result(self):
        with open('result.txt','r') as f:
            return f.read()
    def display_result(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.__marks}")
        print(f"Grade: {self.get_grade()}")

name=input("enter the name: ")
marks=int(input("enter the marks: "))
obj=Student(name,marks)
obj.save_result()
obj.display_result()
print(obj.get_result())

        