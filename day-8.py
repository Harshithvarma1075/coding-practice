'''
we can store data as key : value
keys are unique and then immutable
values-----> can be all data types(immutable amd mutable)
{}

sbi_teja = {"name":"Teja","name": "kartheek",45:89,(4,7):0}
kartheek = {[kumar]:[kum]}
print(sbi_teja)

Methods ------>
------------------------
Keys(): This method is used to get all keys from the dict.
Values(): This method is used to get all the values form the dict.
clear(): This method is used to delete the both keys and values inside the tuple.

a = {"name":"kumar","role":"student","id":"45"}
print(a.keys()) #here it prints all the key values.
print(a.values()) #here it print all the values inside the dict.
print(a.clear())

set{}-----> set data type is a unordered collection and it never allow duplicates.

Methods
-----------------
union: This is used add or get 2 different sets without duplicated values.

any = {1,2,3,4}
so = {4,5,6}
print(any.union(so)) #union

intersection: this method id used to get the common elements in the sets.

any = {1,2,3,4}
so = {4,5,6}
print(any.intersection(so)) #intersection

difference: this method is used to give difference between two sets.

any = {1,2,3,4}
so = {4,5,6}
print(any.difference(so)) #difference

any = {1,2,3,4}
so = {4,5,6}
any.pop()
print(any)
any.remove(2)
print(any)

User = {"Name":"Karteek","Age":"21","Pin":"2005"}
us_pin = input("Enter the PIN: ")
if us_pin == 4:
    if us_pin in User["Pin"]:
        print("Valid")
    else:
        print("Not Valid")
else:  
    print("Enter only 4 digit Pin")
'''
