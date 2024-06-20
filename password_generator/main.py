from random import choice, randint
from string import ascii_lowercase, ascii_uppercase

numbers = "1234567890"
symbols = "!@#$&_?"


# password_length = input("Specify the length of the password: ")
password_length = 32
symbol_num = 9
up = 10
# up = input("up: ")
# low = input("low: ")

# symbol_num , up, low = int(symbol_num), int(up), int(low)
# symbol_num = int(symbol_num)

# if password_length.isdigit():
#     password_length = int(password_length)
# else:
#     print("Please enter a real number between 0 and 32")

salt = ascii_uppercase + numbers + symbols + ascii_lowercase
s, u , l = 0, 0, 0
password = ""
while True:

    # if len(password) != password_length and s!=symbol_num:
    #     char = choice(salt)

    #     if char in symbols and s != symbol_num:
    #         password[randint(1,password_length)] = char
    #         s+=1
    # elif len(password) == password and s!=symbol_num:
    #     # remove random char that is not a symbol
    #     pass
    # else:
    #     break

    if len(password) != password_length:
        password += choice(salt)
    else:
        break

password = list(password)
print("old " + "".join(password))

for sm in password:
    if sm in symbols:
        s+=1

for ul in password:
    if ul in ascii_uppercase:
        u+=1

while u!=up:
    char = password[randint(0,password_length-1)]
    if char not in symbols or char not in ascii_uppercase:
        i = choice(ascii_uppercase)
        password[password.index(char)] = i
        u+=1


while s!=symbol_num:
    char = password[randint(0,password_length-1)]
    if char not in symbols:
        i = choice(symbols)
        password[password.index(char)] = i
        s+=1

print("new " + "".join(password))




# we can have symbols / no symbols / no of symbols
# we can have uppercase/no uppercase / no of uppercase
# print(password)

# if __name__ == "__main__":
#     pass

