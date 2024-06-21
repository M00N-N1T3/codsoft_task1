import unittest
from test_base import captured_output, captured_io
from io import StringIO
from logic.game_logic import rock_paper_scissors, main as game
from main import *
import random

class TestGameLogic(unittest.TestCase):

    def test_rock(self):
        data = "user R"
        user, result = rock_paper_scissors(data)
        self.assertEqual("user",user)
        self.assertEqual("R",result)

    def test_paper(self):
        data = "user P"
        user, result = rock_paper_scissors(data)
        self.assertEqual("user",user)
        self.assertEqual("P",result)

    def test_scissor(self):
        data = "user S"
        user, result = rock_paper_scissors(data)
        self.assertEqual("user",user)
        self.assertEqual("S",result)


    def test_main_user_wins(self):
        user_data = "R"
        computer = "S"
        result = game(user_data,computer)
        self.assertEqual("user",result)

    def test_main_computer_wins(self):
        user_data = "R"
        computer = "P"
        result = game(user_data,computer)
        self.assertEqual("computer",result)

    def test_main_draw(self):
        user_data = "R"
        computer = "R"
        result = game(user_data,computer)
        self.assertEqual("draw",result)


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

    def test_reg_prompt(self):
        expected = "Choose Rock, Paper or Scissors:"

        with captured_io(StringIO("R")) as (out,err):
            choice = prompt().strip()
            actual = out.getvalue().strip()
        self.assertEqual(expected,actual)
        self.assertEqual("R",choice)

    def test_prompt_player(self):
        expected = "test_name Choose Rock, Paper or Scissors:"

        with captured_io(StringIO("R")) as (out,err):
            choice = prompt_player("test_name").strip()
            actual = out.getvalue().strip()
        self.assertEqual(expected,actual)
        self.assertEqual("R",choice)

    def test_prompt(self):
        expected = "Choose Rock, Paper or Scissors: Enter R, P or S\n\n\nChoose Rock, Paper or Scissors:"

        with captured_io(StringIO("H\nP\no\n")) as (out,err):
            prompt().strip()
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


Choose Rock, Paper or Scissors: You won. You chose ROCK and the Computer chose SCISSORS.

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





if __name__ == "__main__":
    unittest.main()