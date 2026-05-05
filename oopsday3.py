#ENCAPSULATION
#the principle of binding data such as attributes,methods and variables into a single unit which is a class is called encapsulation , it provides data security by giving abstraction 

'''
class BankAc:
    def __init__(self,balance):
        self.__balance = balance

    def deposite(self,amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
Acc=BankAc(15000)
Acc.deposite(7000)
print(Acc.get_balance())
'''
'''
class Aadhar:
    def __init__(self, id):
        self.__id = id

    def phonenumber(self,number):
        self.number = number

    def address(self,det):
        self.det = det
        
    def dob(self,date):
        self.date = date

    def get_details(self):
         print(self.__id)
         print(self.number)
         print(self.det)
         print(self.date)
ad=Aadhar(234567890)
ad.phonenumber(9392716822)
ad.address("vizag")
ad.dob("20-4-2026")
print(ad.get_details())
'''

#INHERITANCE
#this allows child class to aquire the attributes and methods of a parent class ,this is called inheritence
'''1.SINGLE INHERITANCE   2.MULTIPLE INHERITANCE'''
''' SUPER() method is used to call methods of the parent class from the child class 

class parent:
    def display(self):
        print("this is parent method")
class child(parent):
    def display(self):
        super().display()
        print("this is child method")

hi=child()
hi.display()
'''
'''
class Bike:
    def display(self):
        print("this is the car")
        
class Engine:
    def display(Self):
        print("this is the engine")      #id method names are same then we get the latest one 
        
class wheel(Bike,Engine):
    def display(self):
        super().display()
        print("this is the wheel")
        

zui = wheel()
zui.display()
'''






















