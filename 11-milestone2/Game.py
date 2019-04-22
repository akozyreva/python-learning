from Cards import Cards
import os


class Game(Cards):

    def __init__(self, dealer_cards=[], player_cards=[], player_score=0,dealer_score=0):
        self.dealer_cards = dealer_cards
        self.player_cards = player_cards
        self.player_score = player_score
        self.dealer_score = dealer_score

    count_dict = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        'jack': 10,
        'king': 10,
        'queen': 10
    }

    # the number of counts in game

    counts = 1

    def new_count(self, player):
        '''
        method for generating new card and counting
        '''
        # 1 step - recive a new card
        result = self.random_card()
        # 2 step - wrtie the results
        if player == 'player':
            self.player_cards.append(result)
        else:
            self.dealer_cards.append(result)
        # 3 step - count the score and write it
        self.total_score(result[0], player)
        # 4 step - paint the results
        if self.counts >= 3:
            self.print_whole_game()
        Game.counts += 1
        # exeucute check winner function

    def total_score(self, card_number, player):
        #print(card_number)
        if card_number == 'ace':
            if player == 'player':
                if self.player_score + 11 <= 21:
                    self.player_score += 11
                else:
                    self.player_score += 1
            else:
                if self.dealer_score + 11 <= 21:
                    self.dealer_score += 11
                else:
                    self.dealer_score += 1
            pass
        else:
            if player == 'player':
                #print(Game.count_dict[card_number])
                self.player_score += int(Game.count_dict[card_number])
            else:
                self.dealer_score += int(Game.count_dict[card_number])

    def print_whole_game(self):
        os.system('clear')
        print("===================")
        print("Dealers Cards")
        for i in self.dealer_cards:
            # TODO - decide, when open card
            if len(self.dealer_cards) == 1:
                print("Hidden Card")
            print(i)
        print(f"Total score: {self.dealer_score}")
        print("===================")
        print("Players cards")
        for i in self.player_cards:
            print(i)
        print(f"Total score: {self.player_score}")
        print("===================")

    def initialize_game(self):
        # create cards_deck
        self.cards_deck()
        # make two moves as player
        self.new_count('player')
        self.new_count('player')
        # mae one move as dealer
        self.new_count('dealer')


    def hit(self, player):
        self.new_count(player)
