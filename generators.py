':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::GENERATORS:::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'THIS IS A SPECIAL TYPE OF FUNCTION THAT GENERATES OR RETURN AN ITERATOR WHICH ONE AT A TIME'
'''
def my_gen():
    yield 1
    yield 2
    yield 3
an = my_gen()
print(next(an))  'NEXT : this is used to get next value from a generator and when the value is finished it will stop the iterator'
print(next(an))
print(next(an))

'''
':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::SQUARE GEN::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'''
def squares(n):
    for i in range(n):
        yield i*i
for num in squares(10):
    print(num)
'''
'YIELD GIVES THE OUTPUT WITH A PAUSE OF MILLI SECOND  , IT IS SIMILAR TO RETURN BUT RETURN GIVES OUTPUT AT A TIME '

'::::::::::::::::::::::::::::::::::::::::::::::::POWER GEN::::::::::::::::::::::::::::::::::::::::::'
'''
def power_gen(n):
    for i in range(1,n+1):
        yield i**i
for num in power_gen(10):
    print(num)
'''
':::::::::::::::::::::::::::::::::::::::::::::::::'
import time
def countdown(n):
    while n>0:
        yield n
        n -= 1
for u in countdown(10):
    print(u)
    time.sleep(1)
