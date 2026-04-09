''' String ---> String is a collection (or) sequence of characters which represented by " " or ' '. we can access the using indexing
(String) can also alllow negative indexing)and also slicing.
This also immutable, where i could not able to modify on that paticular vari......
Note:- we can convert  string into integer, if the xontain only integer values.
<--------------------------------------------------------------------------------------------------------------->
any = "Welcome to Codegnan" #String
print(any)
<--------------------------------------------------------------------------------------------------------------->
any = "Welcome to Codegnan" #String
print(any[7])
<--------------------------------------------------------------------------------------------------------------->
any = "Welcome to Codegnan" #String
print(any[7,8,9]) #TypeError: string indices must be integers, not 'tuple'
<--------------------------------------------------------------------------------------------------------------->
any = "Pyhton Programming" #String
print(any[7:13])
<--------------------------------------------------------------------------------------------------------------->
any = "Pyhton Programming"
so = any.replace("Pyhton","Java")
print(any)
print(so)
<--------------------------------------------------------------------------------------------------------------->
any = "Pyhton Programming"
print(any[20])
<--------------------------------------------------------------------------------------------------------------->
details = "i am kartheek form vizag, i am a fresher as a full stack developer"
print(f'My name is {details[5:14]}')
print(f'I am form {details[19:24]}')
print(f'I am {details[-20:]}')
<--------------------------------------------------------------------------------------------------------------->
details = "i am kartheek form vizag, i am a fresher as a full stack developer"
print(f'My name is {details[5:14]}')
print(f'I am form {details[19:24]}')
print(f'I am {details[-20:]}')#counting from back side
print(details[::-1]) #reverse of a string
<--------------------------------------------------------------------------------------------------------------->
name = 'kartheek'
print(f'Reversing my Name {name[::-1]}')
print(f'Reversing my Name {name[::-2]}')
<--------------------------------------------------------------------------------------------------------------->
#len()---> len() method is used to get char present in the string or find the length of the string
name = "i am kartheek form vizag, i am a fresher as a full stack developer"
it = 1234567899
print(len(name))
print(len(it))# this is give a error
<--------------------------------------------------------------------------------------------------------------->
some = "123"
num = int(some) #here we have converted into int.
print(type(num)) # here we can convert a string into int when there are only numbers if there are any alphabets then we cannot.
'''
'''
Methods of String
-------------------------
split()----> removes space, and this is in the list[] it will give the seperated thing in each index
Syntax = variable_name.split("substring")

some = "Pyhton is a programming language"
print(some.split())
print(some.split(" "))
print(some.split("programming"))
-------------------------
lower()----> This is used to convert all Letters into lower case
Syntax = variable_name.lower()

some = "This IS a CLass "
print(some.lower())
-------------------------
upper()----> This is used to convert all letters into upper case
Syntax = variable_name.upper()

some = "This IS a CLass "
print(some.upper())
-------------------------
replace-----> This is used to replace old str with the new str
Syntax = variable_name.replace("old string","new string")

some = "Pyhton is a programming language"
print(some.replace("programming","nrml"))

some = "Pyhton is a programing language"
if "is" in some:
    print("yes")
else:
    print("no")
#print(some.replace("programing","nrml"))

some  = input("Enter the Alphabet: ")
if some in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")
'''




































