


def menu():

    print("\t\tmain menu\t\n")

    choices = ["0","1","2","3","4"]

    choice = input("""Choose an operation (1-4):
1) Addition
2) Subtraction
3) Multiplication
4) Division
0) Exit\n\n""")

    while True:

        choice = input("Choose an operation (1-4): " )

        if choice == "0":
            exit("Thank you. Goodbye!")
        elif choice in choices and not choice == "0":
            return choice
        else:
            print("Please select a number between 0-5")


def values():

    while True:
        number_of_values = input("How many numbers you want to insert")

        if number_of_values.isdigit():
            return int(number_of_values)

        print("please enter real numbers only.\n")



def logic():
    operation = menu()
    loop = values()



def addition(num1, num2):
    return sum(num1,num2)








if __name__ == "__main__":
    menu()