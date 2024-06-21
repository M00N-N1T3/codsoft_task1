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
            with_computer()
            break
        elif mode == "2":
            with_human()
            break

        if breaker == 3:
            exit("\nToo many incorrect entries. Exiting game.\nGoodbye.")


def with_computer():
    name = input("\nEnter your name: ")
    user = 0
    computer = 0
    draw = 0
    round = 1
    rounds_won = 0
    rounds_lost = 0

    while True:
        scoreboard(name,"Computer",user,computer,draw)

        print(f"\t\t\tRound {round}:\n")
        user_choice = prompt()
        user_choice = get_choice(user_choice)
        computer_choice = random.choice(["R","S","P"])

        result = logic.main(user_choice,computer_choice)
        if result == "user":
            user += 1
            rounds_won += 1
            phrase = "You won"
        elif result == "computer":
            computer += 1
            rounds_lost += 1
            phrase = "You lost"
        else:
            phrase = "This round was a draw."
            draw += 1

        print(f"{phrase}. You chose {CHOICES.get(user_choice)} and the Computer chose {CHOICES.get(computer_choice)}.")
        rematch = input("\nWould you like to play again (Yes/No): ").lower().strip()

        if rematch in ["y","yes"]:
            round +=1
        else:
            print("\nThank you for playing. \nFinal result:")
            scoreboard(name,"Computer",user,computer,draw,False)
            print(f"\nPlayed {round} round(s). Won {rounds_won} - Lost {rounds_lost}")

            if rounds_won != rounds_lost:
                if rounds_won > rounds_lost:
                    print(f"The winner is: {name}")
                    return
                else:
                    exit(f"The winner is: Computer")
            else:
                exit("This game was a DRAW.")


def with_human():
    player_one_name = input("\nPlayer 1 enter your name: ")
    player_two_name = input("Player 2 enter your name: ")
    player_one_score = 0
    player_two_score = 0
    draw = 0
    round = 1
    rounds_won_player_one = 0
    rounds_won_player_two = 0

    while True:
        scoreboard(player_one_name,player_two_name,rounds_won_player_one,rounds_won_player_two,draw)

        print(f"\t\t\tRound {round}:\n")
        player_one_choice = prompt_player(player_one_name)
        player_one_choice = get_choice(player_one_choice)

        player_two_choice = prompt_player(player_two_name)
        player_two_choice = get_choice(player_two_choice)
        print()
        result = logic.main(player_one_choice,player_two_choice)
        if result == "user":
            player_one_score += 1
            rounds_won_player_one += 1
            phrase = f"{player_one_name} Won."
        elif result == "computer":
            player_two_score += 1
            rounds_won_player_two += 1
            phrase = f"{player_two_name} Won."
        else:
            phrase = "This round is a draw!"
            draw += 1

        print(f"{phrase}. {player_one_name} chose {CHOICES.get(player_one_choice)} and {player_two_name} chose {CHOICES.get(player_two_choice)}.")
        rematch = input("\nWould you like to play again (Yes/No): ").lower().strip()

        if rematch in ["y","yes"]:
            round +=1
        else:
            print("\nThank you for playing. \nFinal result:")
            scoreboard(player_one_name,player_two_name,player_one_score,player_two_score,draw,False)
            print(f"\nPlayed {round} round(s). {player_one_name} {rounds_won_player_one} - {player_two_name} {rounds_won_player_two}")

            if rounds_won_player_one != rounds_won_player_two:
                if rounds_won_player_one > rounds_won_player_two:
                    exit(f"The winner is: {player_one_name}")
                else:
                    exit(f"The winner is: {player_two_name}")
            else:
                exit("This game was a DRAW.")


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


def prompt():
    while True:
        user_choice = input("\nChoose Rock, Paper or Scissors: ").upper()

        if user_choice in CHOICES.values() or user_choice in CHOICES.keys():
            return user_choice
        print("Enter R, P or S\n")

def prompt_player(name):
    while True:
        user_choice = input(f"{name} Choose Rock, Paper or Scissors: ").upper()

        if user_choice in CHOICES.values() or user_choice in CHOICES.keys():
            return user_choice
        print("Enter R, P or S\n")


if __name__ == "__main__":
    main()
