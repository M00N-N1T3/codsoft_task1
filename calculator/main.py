
def main():
    print("\t\t\tSelect a Mode")
    print("1) Simple Calculator \n2) Advanced Calculator (multiple-value operation) \n0) Exit\n")
    choice = input("Choose an operation 1-2: ")

    while choice not in ["1","2"]:
        print("\nSelect only 0,1 or 2")
        choice = input("Choose an operation 1-2: ")

    if choice == "1":
        from calculators.simple.calculator import logic
    elif choice == "2":
        from calculators.advanced.calculator import logic

    print("\033c")
    logic()
    return


if __name__ == "__main__":
    print(__import__("tkinter"))
    main()