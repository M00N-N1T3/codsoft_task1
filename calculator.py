from calculators.GUI.calculator import main as GUI
import sys

def app():
    print("\t\t\tSelect a Mode")
    print("1) Simple Calculator \n2) Advanced Calculator (multiple-value operation) \n0) Exit\n")
    choice = input("Choose an operation 1-2: ")

    while choice not in ["1","2","0"]:
        print("\nSelect only 0,1 or 2")
        choice = input("Choose an operation 1-2: ")

    if choice == "1":
        from calculators.simple.calculator import main
    elif choice == "2":
        from calculators.advanced.calculator import main
    else:
        print("Goodbye!")
        exit()

    print("\033c")
    main()
    return



def help():
    print(""""Help: Flags [-n]

calculator.py -n [--no-gui] to run the cli version of the calculator""")



if __name__ == "__main__":

    args = sys.argv

    args = [arg.lower() for arg in args]

    if "--no-gui" in args or "-n" in args:
        app()
    elif "-h" in args or "--help" in args:
        help()
    else:
        GUI()
