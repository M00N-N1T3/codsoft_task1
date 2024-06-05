


def menu():
    """The main menu of teh calculator app
    """

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
    """The number of values you (the user) would like to operate with.

    Returns:
        int:
    """

    while True:
        number_of_values = input("How many numbers you want to insert")

        if number_of_values.isdigit():
            return int(number_of_values)

        print("please enter real numbers only.\n")


def add(numbers : list):
    """Returns the sum of all the numbers in the list

    Args:
        numbers (list): numbers to add

    Returns:
        int : the sum of the values in the list
    """
    return sum(numbers),"";


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
        return

    if len(numbers) == 1:
        return numbers[0], ""

    if len(numbers) == 2:
        return numbers[0] * numbers[1], ""

    num1 = numbers.pop(0)
    num2 = numbers.pop(1)

    total = num1 * num2
    while (len(numbers) != 0):
        total = total * numbers.pop()

    return total,""



def logic():
    operation = menu()
    loop = values()



def addition(num1, num2):
    return sum(num1,num2)








if __name__ == "__main__":
    menu()