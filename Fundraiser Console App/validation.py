import re
import datetime

def is_valid_name(name):
    return re.fullmatch(r"[a-zA-Z]+", name)

def is_valid_phone(phone):
    return re.fullmatch(r"^(\+20|0)1[0-9]{9}$", phone)

def is_valid_email(email):
    return re.fullmatch(r"^[\w\.-]+@[\w\.-]+\.\w{2,}$", email) is not None

def is_valid_password(password, confirm_password):
    return password == confirm_password

def is_valid_date(date_str):
    try:
        return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

def is_end_date_valid(start_date, end_date):
    return start_date < end_date

def replay():
    replay = input("Do you want to do another operation? (y/n) ").lower()
    if replay == 'y':
        return
    else:
        print("Goodbye!")
        exit()