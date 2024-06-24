def menu():
    """The main menu of the calculator app
    """

    print("\t\tSimple Calculator\t\n")


    print("""Available operations:
1) Addition
2) Subtraction
3) Multiplication
4) Division
0) Exit\n\n""")

    choices = ["0","1","2","3","4"]
    while True:

        choice = input("Choose an operation (0-4): " ).strip()

        if choice in choices:
            return int(choice)

        print("Please select a number between 0-4\n")



def add(num1: int, num2: int):
    """Returns the sum of all the numbers in the list

    Args:
        numbers (list): numbers to add

    Returns:
        int : the sum of the values in the list
    """
    return num1 + num2,""


def subs(num1: int, num2: int):
    """
    performs a subtraction operation across all values in a given list

    Args:
        numbers (list): numbers to subtract

    Returns:
        int : the calculated total
    """

    return num1 - num2,""


def multiplication(num1: int, num2: int):
    """
    performs a multiplication operation across all values in a given list

    Args:
        numbers (list): numbers to multiply

    Returns:
        int : the calculated total
    """

    return num1 * num2,""


def division(num1: int, num2: int):
    """
    performs a multiplication operation across all values in a given list

    Args:
        numbers (list): numbers to multiply

    Returns:
        int : the calculated total
    """

    if 0 in [num1,num2]:
        message = "Error, can not divide by zero!"
        return 0, message

    return num1/num2,""

def generate_list_of_values(loop_length : int = 0):
    """
    Generates the list of numbers we will operate on. The length of the loop is
    is determined by the user. Max = 10;

    Args:
        loop_length (int): amount of values to be inserted as determined by user

    Returns:
        list : the collection of numbers to operate on.
    """

    numbers = []

    while True:
        num = input("Enter the 1st number: ")

        if num.isdigit():
            numbers.append(int(num))
            break
        print("Enter real numbers only")


    while True:
        num = input("Enter the 2nd number: ")

        if num.isdigit():
            numbers.append(int(num))
            break
        print("Enter real numbers only")

    return numbers


def logic():

    total = 0

    choices = ["y","yes"]

    while True:

        print()
        operation = menu()
        print()

        if operation == 0:
            exit("Thank you. Goodbye!")
        print()
        values = generate_list_of_values()
        print()


        if operation == 1:
            total = add(values[0],values[1])
            print(f"The sum of {values[0]} and {values[1]} is: {total[0]}")

        elif operation == 2:
            total = subs(values[0],values[1])
            print(f"The subtraction of {values[0]} and {values[1]} is: {total[0]}")

        elif operation == 3:
            total = multiplication(values[0],values[1])
            print(f"The multiplication of {values[0]} and {values[1]} is: {total[0]}")
        elif operation == 4:
            total = division(values[0],values[1])

            if total[0] != 0:
                print(f"The division of {values[0]} and {values[1]} is: {total[0]}")
            else:
                print(total[1])

        choice = input("\nWould you like to do another operation? (Y/N): ").lower().strip()
        if choice not in choices:
            print("Thank you. Goodbye!")
            return
        print("\033c")
