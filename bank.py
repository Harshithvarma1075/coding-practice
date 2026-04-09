hdfc_details = {"name": "varma", "pin": "1075", "balance": 12000}

print("welcome to hdfc bank")
print("enter the atm card")

hdfc_pin = input("enter the 4 digit pin: ")

if len(hdfc_pin) == 4:
    if hdfc_pin == hdfc_details["pin"]:
        
        while True:
            user_choice = int(input("Enter \n1.withdraw: \n2.deposite : \n3.pin change \n4.exit: "))

            if user_choice == 1:
                amount_w = int(input("Enter the amount you want to withdraw: "))
                if amount_w <= hdfc_details['balance']:
                    hdfc_details['balance'] -= amount_w
                    print(f"money withdrawn ,your balance is {hdfc_details['balance']}")
                else:
                    print("insufficient funds")

            elif user_choice == 2:
                depositemoney = int(input("enter the amount you want to deposite: "))
                if depositemoney % 100 == 0 and depositemoney >= 5000:
                    hdfc_details['balance'] += depositemoney
                    print(f"you have deposited {depositemoney} so the balance is {hdfc_details['balance']}")
                else:
                    print("invalid deposit (must be multiple of 100 and >= 5000)")

            elif user_choice == 3:
                hdfc_old_pin = input("enter your old pin: ")
                if hdfc_old_pin == hdfc_details['pin']:
                    new_pin = input("enter your new pin: ")
                    if new_pin != hdfc_details['pin']:
                        hdfc_details['pin'] = new_pin
                        print("new pin updated")
                    else:
                        print("new pin cannot be same as old pin")
                else:
                    print("enter your correct old pin")

            elif user_choice == 4:
                print("thank you for associating with hdfc")
                break

            else:
                print("invalid choice , try again")

    else:
        print("you have entered wrong pin")
else:
    print("invalid pin , enter 4 digit pin")
