import re

def validate_name(name):
    pattern = r'^[A-Za-z]{3,}$'   # only letters, min 3 chars
    return re.fullmatch(pattern, name)

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.fullmatch(pattern, email)

def validate_phone(phone):
    pattern = r'^[0-9]{10}$'
    return re.fullmatch(pattern, phone)

def validate_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$'
    return re.fullmatch(pattern, password)


def main():
    # taking all inputs
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    password = input("Enter password: ")

    # validation checks
    if not validate_name(name):
        print("Invalid Name")

    if not validate_email(email):
        print("Invalid Email")

    if not validate_phone(phone):
        print("Invalid Phone Number")

    if not validate_password(password):
        print("Invalid Password")


if __name__ == "__main__":
    main()
