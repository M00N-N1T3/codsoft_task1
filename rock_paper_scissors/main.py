import random
from logic import game_logic as logic

CHOICES = logic.CHOICES

def modes():
    print("""\tMode

1) Play against the Computer.
2) Play against a Human.
0) Exit
""")

def main():

    modes()
    breaker = 0
    while breaker < 3:
        mode = input("Choose a mode: ").strip()

        if mode == "0":
            exit("Goodbye...")
        elif mode == "1":
            run_game()
            break
        elif mode == "2":
            run_game(False)
            break

        if breaker == 3:
            exit("\nToo many incorrect entries. Exiting game.\nGoodbye.")


def run_game(computer:bool = True):
    player_one_name = input("\nEnter your name: ") if computer else input("\nPlayer one, Enter your name: ")
    player_two_name = "Computer" if computer else input("\nPlayer two, Enter your name: ")
    player_one_score = 0
    player_two_score = 0
    draw = 0
    rounds = 1

    while True:
        scoreboard(player_one_name,player_two_name,player_one_score,player_two_score,draw)

        print(f"\t\t\tRound {rounds}:\n")
        player_one_choice = prompt(player_one_name)
        player_one_choice = get_choice(player_one_choice)
        player_two_choice = random.choice(["R","S","P"]) if computer else prompt(player_two_name)
        player_two_choice = get_choice(player_two_choice)

        result = logic.main(player_one_choice,player_two_choice)
        phrase = process_result(result,player_one_name,player_two_name,computer)

        if result == "player_one":
            player_one_score +=1
        elif result == "player_two":
            player_two_score +=1
        else:
            draw +=1

        # keeping track of player data
        player_one =  [player_one_name,player_one_choice,player_one_score]
        player_two = [player_two_name, player_two_choice,player_two_score]

        message = show_choices(phrase,player_one,player_two,computer)
        print(message)

        rematch = input("\nWould you like to play again (Yes/No): ").lower().strip()

        if rematch in ["y","yes"]:
            rounds +=1
        else:
            print("\nThank you for playing. \nFinal result:")
            scoreboard(player_one_name,player_two_name,player_one_score,player_two_score,draw,False)
            summary = rounds_summary(rounds,player_one,player_two,computer)
            print(summary)

            if player_one[2] == player_two[2]:
                winner = f"The game was a draw!"
            elif player_one[2] > player_two[2]:
                winner = f"The winner is: {player_one[0]}"
            else:
                winner = f"The winner is: The Computer." if computer else f"The winner is: {player_two[0]}"

            print(winner)
            return


def rounds_summary(rounds:int,p_one:list, p_two:list,computer: bool = True):
    """
    A custom round summary based off whether your are playing pc or human.

    Args:
        rounds (int): number of rounds played
        p_one (list): player one's name and score
        p_two (list): player two's name and score
        computer (bool, optional): trigger for whether we playing human or bot. Defaults to True.

    Returns:
        str : custom message
    """
    p_one_score = p_one[2]
    p_two_score = p_two[2]


    if computer:
        if p_two_score != 0:
            p_two_score = abs(p_one[2] - p_two[2])

        message = (f"\nPlayed {rounds} round(s). Won {abs(p_one_score)} - Lost {p_two_score}")
    else:
        message = f"\nPlayed {rounds} round(s). {p_one[0]} {p_one[2]} - {p_two[0]} {p_two[2]}"

    return message

def show_choices(phrase: str,p_one:list,p_two:list,computer:bool=True):
    """
    Returns the appropriate message based off whether you playing the PC or human

    Args:
        phrase (str): _description_
        p_one (list): _description_
        p_two (list): _description_
        computer (bool, optional): _description_. Defaults to True.

    Returns:
        str : custom message
    """

    player_one_name = p_one[0]
    player_two_name = p_two[0]
    player_one = CHOICES.get(p_one[1])
    player_two = CHOICES.get(p_two[1])

    if computer:
        message = (f"{phrase} You chose {player_one} and the Computer chose {player_two}.")
    else:
        message = (f"{phrase} {player_one_name} chose {player_one} and {player_two_name} chose {player_two}.")

    return message

def process_result(result:str ,p_one_name:str, p_two_name:str,computer:bool =True):
    """
    Processes the result and returns the appropriate phrase based off the result
    as well as the appropriate scores

    Args:
        result (str): the player that one
        p_one_name (str): the name of the player
        p_two_name (str): the name of the player
        computer (bool, optional): trigger tha checks whether its user vs PC
        or user vs user. Defaults to True.

    Returns:
        tuple: phrase, player_one_score, player_two_score
    """

    phrase = ""
    if result == "player_one":
        phrase = "You won!" if computer else f"{p_one_name} won!"
    elif result == "player_two":
        phrase = "You lost!" if computer else f"{p_two_name} won!"
    else:
        phrase = "This round was a draw."

    return phrase

def scoreboard(name_one,name_two, score_one,score_two,draw,clear=True):
        if clear:
            print("\033c",end="Scoreboard:\n")
        print(f'{name_one} - {score_one}')
        print(f"{name_two} - {score_two}")
        print(f"Draws - {draw}")


def get_choice(choice: str):

    for key, values in CHOICES.items():
        if choice == key:
            return key

        if choice == values:
            return key


def prompt(player_name):
    print(f"{player_name}'s turn.")
    while True:
        user_choice = input(f"Choose Rock, Paper or Scissors: ").upper()

        if user_choice in CHOICES.values() or user_choice in CHOICES.keys():
            return user_choice
        print("Enter R, P or S\n")


if __name__ == "__main__":
    main()
