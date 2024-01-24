from files.player import Player
from collections import defaultdict


class Game:
    def __init__(self):
        self.board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.selected_moves = defaultdict(int)

    def game_set_up(self):
        print("Welcome to your favorite game, Tic,Tac,Toe!")
        print("You will be player 1")
        player1_name = input("Enter username:")
        while not player1_name.isalpha():
            print("That is not a valid username. Please try again!")
            player1_name = input("Enter username:")

        print("You will be player 2")
        player2_name = input("Enter username:")
        while not player2_name.isalpha() or player1_name == player2_name:
            print("That is not a valid username. Please try again!")
            player2_name = input("Enter username:")

        p1 = Player(player1_name)
        p2 = Player(player2_name)

        return p1, p2

    def print_board(self):
        print("Here's the current board:")
        print(" ", self.board[0][0], " | ", self.board[0][1], " | ", self.board[0][2])
        print(" ----  ----  ----")
        print(" ", self.board[1][0], " | ", self.board[1][1], " | ", self.board[1][2])
        print(" ----  ----  ----")
        print(" ", self.board[2][0], " | ", self.board[2][1], " | ", self.board[2][2], "\n")
        return

    def instructions(self):
        print("In this game of tic-tac-toe, each player will take turns choosing a spot on the board.")
        print("Each spot on the board can only be claimed once, first-come-first-serve.")
        print("We've labeled each position of the board with numbers to make it easier for you to select which position you want.")

        print("  1   |   2   |  3 ")
        print(" ----   ----   ----")
        print("  4   |   5   |  6 ")
        print(" ----   ----   ----")
        print("  7   |   8   |  9 ")

        print("When it's your turn, select one of the available spots!\n")
        return

    def check_board(self, move):
        if move in self.selected_moves.keys():
            print("That was an invalid move because that spot is already taken")
            return False
        elif move.isnumeric() and (int(move) >= 1 and int(move) <= 9):
            return True
        else:
            print("That was an invalid move because your move is not a legal option")
            return False

    def update_board(self, move, whos_turn):
        adjusted_move = int(move) - 1  # bc of zero indexing but to make it easier for users, we start at 1
        row = adjusted_move // 3
        position = adjusted_move % 3

        # update the board array
        if whos_turn == 1:
            self.board[row][position] = 'X'
        else:
            self.board[row][position] = 'O'

        # update the dictionary - do i need both? i guess the array is more for printing and the dictionary is to quickly see if claimed
        self.selected_moves[move] = whos_turn

    def game_over(self):
        for i in range(0,2):
            if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                # all the same column
                if self.board[0][i] == 'X':
                    return (True, 1)
                else:
                    return (True, 2)
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                # all the same row
                if self.board[i][0] == 'X':
                   return (True, 1)
                else:
                   return (True, 2)
        # diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            if self.board[0][0] == 'X':
                return (True, 1)
            else:
                return (True, 2)
        # diagonal
        elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
            if self.board[0][2] == 'X':
                return (True, 1)
            else:
                return (True, 2)
        else:
            return (False, 0)
