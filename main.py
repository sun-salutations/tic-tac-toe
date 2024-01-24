from files.game import Game
from files.player import Player

new_game = Game()
player1, player2 = new_game.game_set_up()

#print the game instructions
new_game.instructions()

#print board
new_game.print_board()

whos_turn = 1
count_of_turns = 0

while count_of_turns != 9 and not new_game.game_over()[0]:
    if whos_turn == 1:
        move = player1.make_move(new_game)
        while not new_game.check_board(move): #there must be a better way to do this than copying same lines of code for player 1 and 2
            move = player1.make_move(new_game)
        new_game.update_board(move, whos_turn)
        whos_turn = 2
    else:
        move = player2.make_move(new_game)
        while not new_game.check_board(move):
            move = player2.make_move(new_game)
        new_game.update_board(move, whos_turn)
        whos_turn = 1

    new_game.started = True
    count_of_turns += 1  # can only have 9 max turns since there are 9 spots
    new_game.print_board()


#announce winner
if new_game.game_over()[0] == True:
    if new_game.game_over()[1] == 1:
        print ("Congrats!",player1.name, "won!" )
    else:
        print ("Congrats!",player2.name, "won!")

elif count_of_turns == 9:
    print("We have a stalemate here! No one won.")




