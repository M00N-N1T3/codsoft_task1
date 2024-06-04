


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
        
        if choice in choices:
            print(choice)
        else:
            print("Please select a number between 0-5")









if __name__ == "__main__":
    menu()