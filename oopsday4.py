#MULTI LEVEL INHERITANCE=====================================================================================
#This occurs when a class inherits from a child class ,creating a grandparent -->parent -->child  in this structure
'''
class Grandparent:
    def Show_GrandParent(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def Show_Parent(Self):
        print("I am parent")
        
class Child(Parent):
    def Show_child(self):
        print("I am child")

dna = Child()
dna.Show_GrandParent()
dna.Show_Parent()
dna.Show_child()
'''
'''
class library:
    def show_books(self):
        print("we are having 2500 books in our library")

class librarian(library):
    def showdetails(self):
        print("you are have 250/- penality")

class user(librarian):
    def show(self):
        print("i will clear the penality , and i want artificial neural network book ")

book=user()
book.show_books()
book.showdetails()
book.show()
'''
#HIERARCHIAL INHERITANCE======================================================================================
#This occurs when multiple child classes inherit from a single parent class ,this process is called hierarchial
'''
class parent:
    def par(self):
        print("I am parent")
class child1(parent):
    def chi(self):
        print("I am first child")
class child2(parent):
    def chil(self):
        print("I am second child")
class child3(child1,child2):
    def dis(self):
        print("I am the child")
gene = child3()
gene.par()
gene.chi()
gene.chil()
gene.dis()
'''
#HYBRID INHERITANCE=========================================================================================
#when we use two or more types of inheritance in a single class then it is called hybrid inheritance
'''
class parent:
    def par(self):
        print("I am parent")
class child1(parent):
    def chi(self):
        print("I am first child")
class child2(parent):
    def chil(self):
        print("I am second child")
class child3(child1,child2):
    def dis(self):
        print("I am the child")
gene = child2()
llm = child1()
llm.par()
gene.par()
'''



class Grandparent:
    def Show_GrandParent(self):
        print("I am Grandparent")

class Parent(Grandparent):
    def Show_Parent(Self):
        print("I am parent")
        
class Child(Parent):
    def Show_child(self):
        print("I am child")


class library:
    def show_books(self):
        print("we are having 2500 books in our library")

class librarian(library):
    def showdetails(self):
        print("you are have 250/- penality")

class user(librarian):
    def show(self):
        print("i will clear the penality , and i want artificial neural network book ")

class hybrid(Child,user):
    def hi(self):
        print("I am hybrid class")

hello=hybrid()
hello.Show_GrandParent()
hello.Show_Parent()
hello.Show_child()
hello.show_books()
hello.showdetails()
hello.show()
hello.hi()

















