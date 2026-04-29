#REGEX CONTINUTION
#7.?
'''
import re
any="this is the continution of the previous regex class"
d=re.findall("th.?",any) #it will search only for 0 or 1 occurence
print(d)
'''
'''
import re
any="this is the continution of the previous regex class"
d=re.search("th.?",any) #it will search only for 0 or 1 occurence
print(d)
'''

#8.{} used to get char by mentioning size
'''
import re
hi="this is meta char"
d=re.findall("th.{6}",hi)
print(d)
'''
'''
import re
hi="this is meta char"
d=re.search(".{6}r",hi)
print(d)
'''
#9.| used to specify either this or that exist
'''
import re
hi="pipe is used to give this or that"
d=re.findall("is | am",hi)
print(d)
'''
'''
import re
hi="pipe is used to give this or that"
d=re.findall("is | am",hi)
print(d)
'''

#10.\A search for starting sequence
'''
import re
txt="the book is on the table"
x=re.findall("\Athe",txt)
if x:
    print(f"match found: {x}")
else:
    print(f"match not found: {X}")

'''


#11.\b search for last sequence
'''
import re
txt="the book is on the table"
x=re.findall(r"\btable",txt)
print(x)
'''

#12\d returns match where the string contains digits
'''
import re
txt="the rain is 75 spain"
r=re.findall("\d",txt)
print(r)
'''

#13\D return a match where the string does not contains digits
'''
import re
txt="the rain 68 is spain"
r=re.findall("\D",txt)
print(r)
if r:
    print("yes there is one digit")
else:
    print("no match")
'''
#14 \s returns where string contains white space characters
'''
import re
txt="the rain is spain"
r=re.findall("\s",txt)
print(r)
'''
#15 \S returns match where the string does not contain a white space
'''
import re
txt="the rain is spain"
r=re.findall("\S",txt)
print(r)
'''

#TIME AND DATE
'============='
'''
%d--->day
%m--->month
%Y----->year
%H----->hours
%M------>minutes
%S-------->seconds
%p----->AM/PM
%A-----> Day name
%B------> month name

import datetime as dt
hi= dt.datetime.now()
print(hi)

import datetime as dt
today=dt.date.today()
print(today.strftime("%d-%m-%Y"))
print(today.strftime("%A"))
print(today.strftime("%B"))

'''












































