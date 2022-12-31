from classes import Board, HumanPlayer, ComputerPlayer, O, X
import random


class Game:
    """Contains the Game Playing Logic"""

    def __init__(self):
        self.board = Board()
        self.human = HumanPlayer(self.board)
        self.computer = ComputerPlayer(self.board)
        self.next_player = None
        self.winner = None

    def select_player_counter(self):
        """Let the player select their counter"""
        counter = ""
        while not (counter == "X" or counter == "O"):
            print("Do you want to be X or O?")
            counter = input().upper()
            if counter != "X" and counter != "O":
                print("Input must be X or O")
            if counter == "X":
                self.human.counter = X
                self.computer.counter = O

            else:
                self.human.counter = O
                self.computer.counter = X

    def select_player_to_go_first(self):
        """Randomly selects who will play first -
        the human or the computer."""
        if random.randint(0, 1) == 0:
            self.next_player = self.human
        else:
            self.next_player = self.computer

    def play(self):
        """Main game playing loop"""
        print("Welcome to TicTacToe")
        self.select_player_counter()
        self.select_player_to_go_first()
        print(self.next_player, "will play first first")
        while self.winner is None:
            # Human players move
            if self.next_player == self.human:
                print(self.board)
                print("Your move")
                move = self.human.get_move()
                self.board.add_move(move)
                if self.board.check_for_winner(self.human):
                    self.winner = self.human
                else:
                    self.next_player = self.computer
            # Computers move
            else:
                print("Computers move")
                move = self.computer.get_move()
                self.board.add_move(move)
                if self.board.check_for_winner(self.computer):
                    self.winner = self.computer
                else:
                    self.next_player = self.human
            # Check for a winner or a draw
            if self.winner is not None:
                print("The Winner is the " + str(self.winner))
            elif self.board.is_full():
                print("Game is a Tie")
                break
        print(self.board)


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
