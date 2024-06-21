CHOICES = {"R":"ROCK", "P":"PAPER", "S":"SCISSORS"}

def main(user,computer):

    user = user # users input
    computer = computer # computers choice

    # a snapshot of the function. All the data in the function
    # will be stored in a dict()
    local = locals()

    # a dictionary to store the key:value pairs that contains R,S or P
    keys = []   # there are only two valid keys. user and computer

    while len(keys)!= 2:

        for key, value in local.items():

            # checking whether the current key is in the list keys.
            if key not in keys:
                # checking whether the key contains R,P,S
                if value == "R":
                    data = f"{key} {value}"
                elif value == "S":
                    data = f"{key} {value}"
                else:
                    data = f"{key} {value}"

            keys.append(data) # appending the key:value pair

    # used for storing the user/computer and their choice
    victors, choices = [],[]

    # users choice
    user_data = keys[0]
    user_name, user_choice = rock_paper_scissors(user_data)

    # appending the user and the users choice
    victors.append(user_name)
    choices.append(user_choice)

    # computers choice
    computer_data = keys[1]
    user_name, user_choice = rock_paper_scissors(computer_data)

    # adding computers choice
    victors.append(user_name)
    choices.append(user_choice)

    # checking if its draw
    if choices[0] == choices[1]:
        return "draw"

    # calculating winners
    if "R" in choices and "S" in choices:
        return victors[choices.index("R")]
    elif "R" in choices and "P" in choices:
        return victors[choices.index("P")]
    # elif "S" in choices and "P" in choices:
    else:
        return victors[choices.index("S")]

def rock_paper_scissors(data: str):
    """
    Returns the appropriate symbol representing the users choice
    Args:
        data (str): the user and their choice

    Returns:
        list: user,choice
    """
    temp = []
    if 'R' in data:
        temp = data.split()
    elif 'S' in data:
        temp = data.split()
    else:
        temp = data.split()

    return temp[0],temp[1]
