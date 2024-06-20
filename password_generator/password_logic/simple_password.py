from random import choice, randint
from string import ascii_lowercase, ascii_uppercase

numbers = "1234567890"
symbols = "!@#$&_?"

# lowercase
def only_lower_case(n: int):
    password = ""
    while (len(password) != n):
        password += choice(ascii_lowercase)
    return password

def lower_case_and_upper_case(n: int):
    password=""
    salt = ascii_lowercase + ascii_uppercase
    while (len(password) != n):
        password += choice(salt)
    return password

def lower_case_and_symbols(n: int):
    password=""
    salt = ascii_lowercase + symbols
    while (len(password) != n):
        password += choice(salt)
    return password

def lower_case_and_numbers(n: int):
    password=""
    salt = ascii_lowercase + numbers
    while (len(password) != n):
        password += choice(salt)
    return password


# upper case
def only_upper_case(n: int):
    password = ""
    while (len(password) != n):
        password += choice(ascii_uppercase)
    return password

def upper_case_and_symbols(n: int):
    password=""
    salt = ascii_lowercase + symbols
    while (len(password) != n):
        password += choice(salt)
    return password


def upper_case_and_numbers(n: int):
    password=""
    salt = ascii_lowercase + numbers
    while (len(password) != n):
        password += choice(salt)
    return password


def numbers_and_symbols(n):
    password=""
    salt = numbers + symbols
    while (len(password) != n):
        password += choice(salt)
    return password

def all_the_chars(n: int):
    password=""
    salt = ascii_lowercase + ascii_uppercase + symbols
    while (len(password) != n):
        password += choice(salt)
    return password

def numbers_only(n:int):
    password=""
    while (len(password) != n):
        password += choice(numbers)
    return password


def only_symbols(n: int):
    password = ""
    while (len(password) != n):
        password += choice(symbols)
    return password
