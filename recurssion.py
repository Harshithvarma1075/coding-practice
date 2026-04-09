'::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::RECURSIVE FUNCTION::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
'''
it is a technique where a function calls itself either directly or indirectly to solve a problem by breaking it into smaller , simpler subproblems, it is used
when a problem can be divided into subtasks'''
'''
def validate_pin(self):
    while self.remaining_attempts >0:
        user_pin = input("enter 4 digit pin: ")
        if len(user_pin) == 4 and user_pin == self.user_info["ATM PIN"]:
            print(" welcome to the bank")
            return True
       else:
           self.remaining_attempts -=1
           if self.remaining_attempts>0:
               print(f"invalid pin, attempts left :{remaining_attempts}")
            else:
                print("❌ card blocked.please contact customer service")
                return False
'''

'::::::::::::::::::::::::::::::::::::::::::::::::::::VOWELS AND CONSONENTS IN A STRING:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::'
me=input("enter the string: ")
vowels_list=[ ]
consonents_list=[ ]
def vowels(me,vowels,consonents):
    for i in me :
        if i in "AEIOUaeiou":
            vowels.append(i)
        else:
            consonents.append(i)
    print(f"{vowels} are the vowels")
    print(f"{consonents} are the consonents")
vowels(me,vowels_list,consonents_list)
