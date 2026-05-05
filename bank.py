# hdfc_details = {"name": "varma", "pin": "1075", "balance": 12000,"transaction_history":[ ]}

# print("welcome to hdfc bank")
# print("enter the atm card")

# hdfc_pin = input("enter the 4 digit pin: ")

# if len(hdfc_pin) == 4:
#     if hdfc_pin == hdfc_details["pin"]:
        
#         while True:
#             user_choice = int(input("Enter \n1.withdraw: \n2.deposite : \n3.pin change: \n4.exit: \n5.transaction history: "))

#             if user_choice == 1:
#                 amount_w = int(input("Enter the amount you want to withdraw: "))
#                 if amount_w <= hdfc_details['balance']:
#                     hdfc_details['balance'] -= amount_w
#                     hdfc_details['transaction_history'].append(f"withdraw: {amount_w}")
#                     print(f"money withdrawn ,your balance is {hdfc_details['balance']}")
#                 else:
#                     print("insufficient funds")

#             elif user_choice == 2:
#                 depositemoney = int(input("enter the amount you want to deposite: "))
#                 if depositemoney % 100 == 0 and depositemoney >= 5000:
#                     hdfc_details['balance'] += depositemoney
#                     hdfc_details['transaction_history'].append(f"deposited:{depositemoney}")
#                     print(f"you have deposited {depositemoney} so the balance is {hdfc_details['balance']}")
#                 else:
#                     print("invalid deposit (must be multiple of 100 and >= 5000)")

#             elif user_choice == 3:
#                 hdfc_old_pin = input("enter your old pin: ")
#                 if hdfc_old_pin == hdfc_details['pin']:
#                     new_pin = input("enter your new pin: ")
#                     if new_pin != hdfc_details['pin']:
#                         hdfc_details['pin'] = new_pin
#                         print("new pin updated")
#                     else:
#                         print("new pin cannot be same as old pin")
#                 else:
#                     print("enter your correct old pin")

#             elif user_choice == 4:
#                 print("thank you for associating with hdfc")
#                 break
#             elif user_choice == 5:
#                 print(hdfc_details['transaction_history'])
                

#             else:
#                 print("invalid choice , try again")

#     else:
#         print("you have entered wrong pin")
# else:
#     print("invalid pin , enter 4 digit pin")

class BankAccount:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def check_pin(self, entered_pin):
        return entered_pin == self.pin

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw: {amount}")
            print(f"Withdraw successful. Balance: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif amount % 100 != 0:
            print("Amount must be multiple of 100")
        else:
            self.balance += amount
            self.transaction_history.append(f"Deposit: {amount}")
            print(f"Deposit successful. Balance: {self.balance}")

    def change_pin(self, old_pin, new_pin):
        if old_pin != self.pin:
            print("Incorrect old PIN")
        elif len(new_pin) != 4 or not new_pin.isdigit():
            print("PIN must be 4 digits")
        elif new_pin == self.pin:
            print("New PIN cannot be same as old PIN")
        else:
            self.pin = new_pin
            print("PIN updated successfully")

    def show_transactions(self):
        if not self.transaction_history:
            print("No transactions yet")
        else:
            print("Transaction History:")
            for t in self.transaction_history:
                print("-", t)


# -------- MAIN PROGRAM --------
account = BankAccount("varma", "1075", 12000)

print("Welcome to HDFC Bank")
entered_pin = input("Enter your 4-digit PIN: ")

if len(entered_pin) == 4 and entered_pin.isdigit():
    if account.check_pin(entered_pin):

        while True:
            try:
                choice = int(input("""
1. Withdraw
2. Deposit
3. Change PIN
4. Transaction History
5. Exit
Enter choice: """))

                if choice == 1:
                    amt = int(input("Enter amount to withdraw: "))
                    account.withdraw(amt)

                elif choice == 2:
                    amt = int(input("Enter amount to deposit: "))
                    account.deposit(amt)

                elif choice == 3:
                    old = input("Enter old PIN: ")
                    new = input("Enter new PIN: ")
                    account.change_pin(old, new)

                elif choice == 4:
                    account.show_transactions()

                elif choice == 5:
                    print("Thank you for banking with us!")
                    break

                else:
                    print("Invalid choice")

            except ValueError:
                print("Please enter valid input")

    else:
        print("Incorrect PIN")
else:
    print("Invalid PIN format")