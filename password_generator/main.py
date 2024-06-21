from random import choice, randint
from string import ascii_lowercase, ascii_uppercase

str_numbers = "1234567890"
str_symbols = "!@#$&_?"


# password_length = input("Specify the length of the password: ")
# password_length = 32
# symbol_num = 9
# up = 10
# up = input("up: ")
# low = input("low: ")

# symbol_num , up, low = int(symbol_num), int(up), int(low)
# symbol_num = int(symbol_num)

# if password_length.isdigit():
#     password_length = int(password_length)
# else:
#     print("Please enter a real number between 0 and 32")



def generate_password(password_length: int):
    salt = ascii_uppercase + str_numbers + str_symbols + ascii_lowercase
    password = ""
    while True:
        if len(password) != password_length:
            password += choice(salt)
        else:
            break
    return password



def char_count(password,salt,):
    count = 0
    for char in password:
        if char in salt:
            count +=1

    return count




# password = list(password)
# print("old " + "".join(password))

# for sm in password:
#     if sm in symbols:
#         s+=1

# for ul in password:
#     if ul in ascii_uppercase:
#         u+=1

# while u!=up:
#     char = password[randint(0,password_length-1)]
#     if char not in symbols or char not in ascii_uppercase:
#         i = choice(ascii_uppercase)
#         password[password.index(char)] = i
#         u+=1


# while s!=symbol_num:
#     char = password[randint(0,password_length-1)]
#     if char not in symbols:
#         i = choice(symbols)
#         password[password.index(char)] = i
#         s+=1

# print("new " + "".join(password))

def built_around_upperCase(n:int, upper_case:tuple, lower_case:tuple, numbers: tuple, symbols = tuple):
    uFlag, upperCase_count = upper_case
    lFlag, lowerCase_count = lower_case
    sFlag, symbols_count = symbols
    nFlag, numbers_count = numbers

    password = generate_password(n)
    # if no number was specified for all of them, then we assume that they just want a random one containing all
    if upperCase_count == "" and lowerCase_count == "" and numbers_count =="" and symbols_count=="":
        return password

    Up = char_count(password,ascii_uppercase)
    Low = char_count(password,ascii_lowercase)
    Sym = char_count(password,str_symbols)
    Num = char_count(password,str_numbers)

    # converting password to a list for mutability
    password = list(password)

    # if only specified how many uppercase characters we want and its greater than current count
    if uFlag and not lFlag and not sFlag and not nFlag:

        salt = ascii_lowercase + str_numbers + str_symbols
        while int(upperCase_count) != Up:
            char = password[randint(0,len(password)-1)]

            if Up < int(upperCase_count):
                if char not in ascii_uppercase:
                    new_char = choice(ascii_uppercase) # getting a random uppercase value
                    password[password.index(char)] = new_char
                    Up +=1
            else:
                if char in ascii_uppercase:
                    new_char = choice(salt)
                    password[password.index(char)] = new_char
                    Up -=1

        return "".join(password)

    # if they specified low
    elif lFlag and not uFlag and not sFlag and not nFlag:
        salt = ascii_uppercase + str_numbers + str_symbols
        while int(lowerCase_count) != Low:
            char = password[randint(0,len(password)-1)]

            if Low < int(lowerCase_count):
                if char not in ascii_lowercase:
                    new_char = choice(ascii_lowercase) # getting a random uppercase value
                    password[password.index(char)] = new_char
                    Low +=1
            else:
                if char in ascii_lowercase:
                    new_char = choice(salt)
                    password[password.index(char)] = new_char
                    Low -=1

        return "".join(password)

    # if they just specified symbols
    elif sFlag and not uFlag and not lFlag and not nFlag:
        salt = ascii_uppercase + str_numbers + ascii_lowercase
        while int(symbols_count) != Sym:
            char = password[randint(0,len(password)-1)]

            if  Sym < int(symbols_count):
                if char not in str_symbols:
                    new_char = choice(str_symbols) # getting a random uppercase value
                    password[password.index(char)] = new_char
                    Sym +=1
            else:
                if char in str_symbols:
                    new_char = choice(salt)
                    password[password.index(char)] = new_char
                    Sym -=1

        return "".join(password)

    # if they just specified the numbers
    elif nFlag and not uFlag and not lFlag and not sFlag:
        salt = ascii_uppercase + str_symbols + ascii_lowercase
        while int(numbers_count) != Num:
            char = password[randint(0,len(password)-1)]

            if  Num < int(numbers_count):
                if char not in str_numbers:
                    new_char = choice(str_numbers) # getting a random uppercase value
                    password[password.index(char)] = new_char
                    Sym +=1

            else:
                if char in str_numbers:
                    new_char = choice(salt)
                    password[password.index(char)] = new_char
                    Sym -=1

        return "".join(password)


# def all_the_chars(n: int):
#     password=""
#     salt = ascii_lowercase + ascii_uppercase + str_symbols
#     while (len(password) != n):
#         password += choice(salt)
#     return password

u = (True,9)
s = (False,"")
n = (False,"")
l = (False,"")

result = built_around_upperCase(20,u,l,n,s)
print(result)
# if __name__ == "__main__":
#     pass

