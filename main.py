from files.game import Game
from files.player import Player

game = Game()
player1, player2 = game.game_set_up()

# print the game instructions
game.instructions()

# print board
game.print_board()

whose_turn = 1
count_of_turns = 0

while count_of_turns < 9 and not game.game_over()[0]:
    if whose_turn == 1:
        move = player1.make_move(game)
        # there must be a better way to do this than copying same lines of code for player 1 and 2
        while not game.check_board(move): 
            move = player1.make_move(game)
        game.update_board(move, whose_turn)
        whose_turn = 2
    else:
        move = player2.make_move(game)
        while not game.check_board(move):
            move = player2.make_move(game)
        game.update_board(move, whose_turn)
        whose_turn = 1

    count_of_turns += 1  # can only have 9 max turns since there are 9 spots
    game.print_board()

# announce winner
if game.game_over()[0]:
    if game.game_over()[1] == 1:
        print("Congrats!", player1.name, "won!")
    else:
        print("Congrats!", player2.name, "won!")

elif count_of_turns == 9:
    print("We have a stalemate here! No one won.")
