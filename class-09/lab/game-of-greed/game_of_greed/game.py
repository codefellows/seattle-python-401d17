import sys

from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker


class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):

        self.banker = Banker()
        self.num_rounds = num_rounds
        self.round_num = 0

    def play(self, roller=None):
        """Entry point for playing (or declining) a game

        Args:
            roller (function, optional): Allows passing in a custom dice roller function.
                Defaults to None.
        """

        self._roller = roller or GameLogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")
        response = input("> ")

        if response == "n":
            print("OK. Maybe another time")
        else:
            for round_num in range(1, self.num_rounds + 1):
                self.start_round(round_num)

            self.end_game()

    def end_game(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()

    def start_round(self, round_num):
        num_dice = 6
        print(f"Starting round {round_num}")
        round_score = 0

        while True:
            print(f"Rolling {num_dice} dice...")

            roll = self._roller(num_dice)
            roll_string = " ".join([str(value) for value in roll])
            print(f"*** {roll_string} ***")

            preliminary_score = GameLogic.calculate_score(roll)

            if preliminary_score == 0:
                self.zilch(round_num)
                return

            keeper_values = self.validate_keepers(roll, roll_string)

            keeper_score = GameLogic.calculate_score(keeper_values)

            round_score += keeper_score

            num_dice -= len(keeper_values)

            print(
                f"You have {round_score} unbanked points and {num_dice} dice remaining"
            )
            print("(r)oll again, (b)ank your points or (q)uit:")
            response = input("> ")

            if response == "b":
                self.banker.shelf(round_score)
                banked_points = self.banker.bank()
                self.end_round(round_num, banked_points)
                break
            elif response == "r":
                if num_dice == 0:
                    num_dice = 6
            elif response == "q":
                self.end_game()

    def zilch(self, round_num):
        """Zero scoring dice were rolled so end round with 0 points"""
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")

        self.end_round(round_num, 0)

    def end_round(self, round_num, banked_points):
        """bank points and finish round"""
        print(f"You banked {banked_points} points in round {round_num}")
        print(f"Total score is {self.banker.balance} points")

    def validate_keepers(self, roll, roll_string):
        """ensures that kept dice are valid for the roll

        Args:
            roll
            roll_string

        Returns:
            valid keeper values
        """
        while True:
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")
            if response == "q":
                self.end_game()
                break

            keeper_values = []
            for char in response:
                if char.isnumeric():
                    keeper_values.append(int(char))

            if GameLogic.validate_keepers(roll, keeper_values):
                return keeper_values
            else:
                print("Cheater!!! Or possibly made a typo...")
                print(f"*** {roll_string} ***")


if __name__ == "__main__":
    game = Game()
    game.play()
