
number=int(input())
def star(number):
    for i in range(1,number+1):
        print(" "*(number-i) , end=" ")
        for j in range(i):
             print("*",end=" ")
        print()
star(number)


'''
number=int(input())
def star(number):
    for i in range(number):
        for j in range(i):
            print("*",end=" ")
        print()
star(number)
'''
'''
string_1 = input("Normal_str = ")
def remove_o(string_1):
    for ch in string_1:
        if ch in "aeiou":
            string_1 = string_1.replace(ch, "")
    print(f"Modified_str = {string_1}")
remove_o(string_1)
'''
