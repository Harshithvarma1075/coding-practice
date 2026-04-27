#REGULAR EXPRESSIONS
#This regular expression or regex is a sequence of character that forms a searching pattern.
#To use this we have to import "re" , which will unlock the package.
'''==============================================================================='''

#FUNCTIONS
#1.findall
#2.search
'''
#by using findall, it will find all the sequence in the string -----the syntax is ----->re.findall("metachar",var)
import re
hi="this is regex concept"
print(re.findall("e",hi))
'''
'''
#by using search, it will only find the first sequence in the string --------the syntax is -------->re.search("metachar",var)
import re
hi="this is regex concept"
print(re.search("e",hi))
'''

#metacharacters----symbols used to form the searching pattern,we have many metacharacters
#1.[ ]-------in this meta char we can search for a-z, A-Z,0-9
'''
import re
var="this is my entire list"
hi=re.findall("[ael]",var) #we will get the output in the form of a list containing the char within that range
print(hi)

import re
some="it will only find the first sequence in the string"
he=re.search("[ael]",some)
print(he)
'''

#2.dot(.) ----[.] itself is a metachar
'''
import re
we="hello"
v=re.findall("h...o",we) #gives any sequence starting and ending with h and o having exactly three char in between them from the string
print(v)
'''
'''
import re
we="hello"
m=re.search("h...o",we)
print(m)
'''
#3.^ --------- this is used to find the string is starting with the sequence or not , syntax------------>re.findall("^metachar",var)
'''
import re
j="this is used to find the string is starting with the sequence or not"
m=re.findall("^this",j)
print(m)

import re
j="this is used to find the string is starting with the sequence or not"
m=re.search("^this",j)
print(m)
'''
#4.$----------- this is used to find the string is ending with the sequence or not , syntax---------------->re.findall("metachar$",var)
'''
import re
l="this is python class"
m=re.findall("class$",l)
print(m)
'''
'''
import re
l="this is python class"
m=re.search("class$",l)
print(m)
'''
#5.*------------this is used to find the string that starts and ends with specified chars but contains any number of occurences in between,syntax------->re.findall("metachar.*",var)
'''
import re
name="this is used to find the string that starts and ends"
n=re.findall("th.*i",name)
print(n)
'''
'''
import re
name="this is used to find the string that starts and ends"
n=re.search("th.*i",name)
print(n)
'''

#6.+-----------------Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o": syntax--->re.findall("he.+o",var)
'''
import re
name="Search for a sequence that starts with "
k=re.findall("n.+t",name)
print(k)
'''
#there is diff between * and + , it is in * it can have zero char between spcified ones but here in + it should have atleast 1 or more chars in between specified range
'''
import re
name="Search for a sequence that starts with "
k=re.search("n.+t",name)
print(k)
'''



























