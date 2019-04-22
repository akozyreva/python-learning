from Game import Game


class Player(Game):
    def __init__(self):
         super(Game, self).__init__()

    def show_cards(self):
        print(self.player_cards)
