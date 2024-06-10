


def menu():
    """The main menu of the calculator app
    """

    print("\t\tmain menu\t\n")


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


def number_of_values():
    """The number of values you (the user) would like to operate with.

    Returns:
        int:
    """

    while True:
        number_of_values = input("How many values would you like to insert? (min 2 - max 10): ")

        if not number_of_values.isdigit():
            print("Please enter real numbers only [e.g. 1,2,10].\n")
        elif number_of_values.isdigit() and int(number_of_values) < 2:
            print("Minium value is 2! \n")
        else:
            return int(number_of_values)



def add(numbers : list):
    """Returns the sum of all the numbers in the list

    Args:
        numbers (list): numbers to add

    Returns:
        int : the sum of the values in the list
    """
    return sum(numbers),""


def subs(numbers : list):
    """
    performs a subtraction operation across all values in a given list

    Args:
        numbers (list): numbers to subtract

    Returns:
        int : the calculated total
    """

    if len(numbers) == 1:
        return numbers[0],""

    if len(numbers) == 2:
        return numbers[0] - numbers[1],""

    num1 = numbers.pop(0)
    num2 = numbers.pop(1)

    total = num1 - num2
    while (len(numbers) != 0):
        total = total - numbers.pop()

    return total,""


def multiplication(numbers : list):
    """
    performs a multiplication operation across all values in a given list

    Args:
        numbers (list): numbers to multiply

    Returns:
        int : the calculated total
    """

    if len(numbers) == 1:
        return numbers[0],""

    if len(numbers) == 2:
        return numbers[0] * numbers[1],""

    num1 = numbers.pop(0)
    num2 = numbers.pop(1)

    total = num1 * num2
    while (len(numbers) != 0):
        total = total * numbers.pop()

    return total,""


def division(numbers : list):
    """
    performs a multiplication operation across all values in a given list

    Args:
        numbers (list): numbers to multiply

    Returns:
        int : the calculated total
    """

    if 0 in numbers:
        message = "Error, can not divide by zero!"
        return 0, message

    if len(numbers) == 1:
        return numbers[0],""

    if len(numbers) == 2:
        return numbers[0] / numbers[1],""

    num1 = numbers.pop(0)
    num2 = numbers.pop(1)

    total = num1 / num2
    while (len(numbers) != 0):
        total = total / numbers.pop()

    return total,""

def generate_list_of_values(loop_length : int):
    """
    Generates the list of numbers we will operate on. The length of the loop is
    is determined by the user. Max = 10;

    Args:
        loop_length (int): amount of values to be inserted as determined by user

    Returns:
        list : the collection of numbers to operate on.
    """

    numbers = []

    while (len(numbers) != loop_length):

        if (len(numbers) == 0):
            number = input("Enter the 1st value: ").lower().strip()
        elif (len(numbers) == 1):
            number = input("Enter the 2nd value: ").lower().strip()
        elif (len(numbers) == 2):
            number = input("Enter the 3rd value: ").lower().strip()
        else:
            number = input(f"Enter the {len(numbers)+1}th value: ").lower().strip()

        if (number == "q"):
            break
        elif (not number.isdigit()):
            print("please enter real numbers only [e.g. 1,25,10] or q to quit.")
        else:
            numbers.append(int(number))
        print()
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

        loop_control = number_of_values()
        print()
        values = generate_list_of_values(loop_control)
        print()

        show_case_values = []
        show_case_values.extend(values)

        if operation == 1:
            total = add(values)
            print(f"The sum of {show_case_values} is: {total[0]}")

        elif operation == 2:
            total = subs(values)
            print(f"The subtraction of {show_case_values} is: {total[0]}")

        elif operation == 3:
            total = multiplication(values)
            print(f"The multiplication of {show_case_values} is: {total[0]}")
        elif operation == 4:
            total = division(values)

            if total[0] != 0:
                print(f"The division of {show_case_values} is: {total[0]}")
            else:
                print(total[1])




        choice = input("\nWould you like to do another operation? (Y/N): ").lower().strip()
        if choice not in choices:
            exit("Thank you. Goodbye!")
        print("---------------------------------------------------------------------------------------")


if __name__ == "__main__":
    logic()
