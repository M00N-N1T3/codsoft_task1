CHOICES = {"R":"ROCK", "P":"PAPER", "S":"SCISSORS"}

def main(player_one,player_two):

    player_one = player_one # users input
    player_two = player_two # computers choice

    # a snapshot of the function. All the data in the function
    # will be stored in a dict()
    local = locals()

    # a dictionary to store the key:value pairs that contains R,S or P
    data = []   # there are only two valid keys. user and computer

    while len(data)!= 2:

        for key, value in local.items():

            # checking whether the current key is in the list keys.
            if key not in data:
                # checking whether the key contains R,P,S
                if value == "R":
                    pair = f"{key} {value}"
                elif value == "S":
                    pair= f"{key} {value}"
                else:
                    pair = f"{key} {value}"

            data.append(pair) # appending the key:value pair

    # used for storing the user/computer and their choice
    players, choices = [],[]

    # users choice
    player_one_data = data[0]
    player_one_name, player_one_choice = rock_paper_scissors(player_one_data)

    # appending the user and the users choice
    players.append(player_one_name)
    choices.append(player_one_choice)

    # computers choice
    player_two_data = data[1]
    player_two_name,player_two_choice = rock_paper_scissors(player_two_data)

    # adding computers choice
    players.append(player_two_name)
    choices.append(player_two_choice)

    return result(players,choices)


def result(players:list ,choices:list):
    """
    Determines the game result based off of the given data
    Args:
        players (list): all the available players
        choices (list): the players choice

    Return:
        string : result (draw/player_name)
    """
        # checking if its draw
    if choices[0] == choices[1]:
        return "draw"

    # calculating winners
    if "R" in choices and "S" in choices:
        return players[choices.index("R")]
    elif "R" in choices and "P" in choices:
        return players[choices.index("P")]
    # elif "S" in choices and "P" in choices:
    else:
        return players[choices.index("S")]


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
