class Player:

    def __init__(self, user_name):
        self.name = user_name

    def make_move(self, game):
        move = input(self.name + ", which move would you like to make? ")
        return move
