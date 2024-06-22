import unittest
from test_base import captured_output, captured_io
from io import StringIO
from logic.game_logic import rock_paper_scissors, result, main as game
from main import *
import random

class TestGameLogic(unittest.TestCase):

    def test_rock(self):
        data = "player_one R"
        user, result = rock_paper_scissors(data)
        self.assertEqual("player_one",user)
        self.assertEqual("R",result)

    def test_paper(self):
        data = "player_two P"
        user, result = rock_paper_scissors(data)
        self.assertEqual("player_two",user)
        self.assertEqual("P",result)

    def test_scissor(self):
        data = "user S"
        user, result = rock_paper_scissors(data)
        self.assertEqual("user",user)
        self.assertEqual("S",result)


    def test_main_user_wins(self):
        player_one = "R"
        player_two = "S"
        result = game(player_one,player_two)
        self.assertEqual("player_one",result)

    def test_main_computer_wins(self):
        player_one = "R"
        player_two = "P"
        result = game(player_one,player_two)
        self.assertEqual("player_two",result)

    def test_main_draw(self):
        player_one = "R"
        player_two = "R"
        result = game(player_one,player_two)
        self.assertEqual("draw",result)

    def test_result_p_two(self):
        players = ["player_one","player_two"]
        choices = ["R","P"]
        actual_result = result(players,choices)
        self.assertEqual("player_two",actual_result)

    def test_result_p_one(self):
        players = ["player_one","player_two"]
        choices = ["S","P"]
        actual_result = result(players,choices)
        self.assertEqual("player_one",actual_result)

    def test_result_draw(self):
        players = ["player_one","player_two"]
        choices = ["P","P"]
        actual_result = result(players,choices)
        self.assertEqual("draw",actual_result)


class TestMain(unittest.TestCase):

    def test_scoreboard(self):
        expected = "test - 1\ncomputer - 2\nDraws - 2"
        with captured_output() as (out,err):
            scoreboard("test","computer",1,2,2,False)
            actual = out.getvalue().strip()
        self.assertEqual(expected,actual)

    def test_choice_conversion(self):
        rock = get_choice("ROCK")
        paper = get_choice("PAPER")
        scissors = get_choice("SCISSORS")
        self.assertEqual("R",rock)
        self.assertEqual("S",scissors)
        self.assertEqual("P",paper)

    def test_prompt(self):
        expected = "Tommy's turn.\nChoose Rock, Paper or Scissors:"

        with captured_io(StringIO("R")) as (out,err):
            choice = prompt("Tommy").strip()
            actual = out.getvalue().strip()
        self.assertEqual(expected,actual)
        self.assertEqual("R",choice)

    def test_prompt_incorrect_choice(self):
        expected = "Tommy's turn.\nChoose Rock, Paper or Scissors: Enter R, P or S\n\nChoose Rock, Paper or Scissors:"

        with captured_io(StringIO("H\nP\no\n")) as (out,err):
            prompt("Tommy").strip()
            actual = out.getvalue().strip()
        self.assertEqual(expected,actual)

    def test_game_logic_vs_computer_win(self):
        random.choice = lambda a: "S"
        expected ="""Mode

1) Play against the Computer.
2) Play against a Human.
0) Exit

Choose a mode: \nEnter your name: \x1bcScoreboard:
Tommy - 0
Computer - 0
Draws - 0
\t\t\tRound 1:

Tommy's turn.
Choose Rock, Paper or Scissors: You won! You chose ROCK and the Computer chose SCISSORS.

Would you like to play again (Yes/No): 
Thank you for playing. 
Final result:
Tommy - 1
Computer - 0
Draws - 0

Played 1 round(s). Won 1 - Lost 0
The winner is: Tommy"""

        with captured_io(StringIO("1\nTommy\nR\nNo\n")) as (out,err):
            main()
            actual = out.getvalue().strip()
        self.assertEqual(expected,actual)


    def test_game_logic_vs_computer_lose(self):
        random.choice = lambda a: "S"
        expected ="""Mode

1) Play against the Computer.
2) Play against a Human.
0) Exit

Choose a mode: \nEnter your name: \x1bcScoreboard:
Tommy - 0
Computer - 0
Draws - 0
\t\t\tRound 1:

Tommy's turn.
Choose Rock, Paper or Scissors: You lost! You chose PAPER and the Computer chose SCISSORS.

Would you like to play again (Yes/No): 
Thank you for playing. 
Final result:
Tommy - 0
Computer - 1
Draws - 0

Played 1 round(s). Won 0 - Lost 1
The winner is: The Computer."""

        with captured_io(StringIO("1\nTommy\nP\nNo\n")) as (out,err):
            main()
            actual = out.getvalue().strip()
        self.assertEqual(expected,actual)


    def test_game_logic_vs_computer_draw(self):
        random.choice = lambda a: "S"
        expected ="""Mode

1) Play against the Computer.
2) Play against a Human.
0) Exit

Choose a mode: \nEnter your name: \x1bcScoreboard:
Tommy - 0
Computer - 0
Draws - 0
\t\t\tRound 1:

Tommy's turn.
Choose Rock, Paper or Scissors: This round was a draw. You chose SCISSORS and the Computer chose SCISSORS.

Would you like to play again (Yes/No): 
Thank you for playing. 
Final result:
Tommy - 0
Computer - 0
Draws - 1

Played 1 round(s). Won 0 - Lost 0
The game was a draw!"""

        with captured_io(StringIO("1\nTommy\nS\nNo\n")) as (out,err):
            main()
            actual = out.getvalue().strip()
        self.assertEqual(expected,actual)

    def test_game_logic_rematch(self):
        random.choice = lambda a: "S"
        expected ="""Mode

1) Play against the Computer.
2) Play against a Human.
0) Exit

Choose a mode: \nEnter your name: \x1bcScoreboard:
Tommy - 0
Computer - 0
Draws - 0
\t\t\tRound 1:

Tommy's turn.
Choose Rock, Paper or Scissors: This round was a draw. You chose SCISSORS and the Computer chose SCISSORS.

Would you like to play again (Yes/No): \x1bcScoreboard:
Tommy - 0
Computer - 0
Draws - 1
\t\t\tRound 2:

Tommy's turn.
Choose Rock, Paper or Scissors: You won! You chose ROCK and the Computer chose SCISSORS.

Would you like to play again (Yes/No): 
Thank you for playing. 
Final result:
Tommy - 1
Computer - 0
Draws - 1

Played 2 round(s). Won 1 - Lost 0
The winner is: Tommy"""

        with captured_io(StringIO("1\nTommy\nS\ny\nR\nNo\n")) as (out,err):
            main()
            actual = out.getvalue().strip()
        self.assertEqual(expected,actual)

    def test_game_logic_multiplayer(self):
        random.choice = lambda a: "S"
        expected ="""Mode

1) Play against the Computer.
2) Play against a Human.
0) Exit

Choose a mode: \nPlayer one, Enter your name: \nPlayer two, Enter your name: \x1bcScoreboard:
Tommy - 0
Josh - 0
Draws - 0
\t\t\tRound 1:

Tommy's turn.
Choose Rock, Paper or Scissors: Josh's turn.
Choose Rock, Paper or Scissors: This round was a draw. Tommy chose SCISSORS and Josh chose SCISSORS.

Would you like to play again (Yes/No): \x1bcScoreboard:
Tommy - 0
Josh - 0
Draws - 1
\t\t\tRound 2:

Tommy's turn.
Choose Rock, Paper or Scissors: Josh's turn.
Choose Rock, Paper or Scissors: Tommy won! Tommy chose ROCK and Josh chose SCISSORS.

Would you like to play again (Yes/No): 
Thank you for playing. 
Final result:
Tommy - 1
Josh - 0
Draws - 1

Played 2 round(s). Tommy 1 - Josh 0
The winner is: Tommy"""

        with captured_io(StringIO("2\nTommy\nJosh\nS\nS\ny\nR\nS\nNo\n")) as (out,err):
            main()
            actual = out.getvalue().strip()
        self.assertEqual(expected,actual)








if __name__ == "__main__":
    unittest.main()