import random


class Cards:
    suits = ['lubs', 'diamonds', 'hearts', 'spades']
    suit = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'king',
            'queen', 'ace']
    card_deck = {}
    # list with 4 card decks
    list_card_deck = []

    def cards_deck(self):
        # create 4 card deck
        for i in self.suits:
            list_suit = []
            for card in self.suit:
                list_suit.append(card)
            self.card_deck.update({i: list_suit})
            self.list_card_deck.append(self.card_deck)
        # it  has the following structure
        # card_deck = {'lubs': [2, 3, 4.... 'ace'],
        # 'diamonds': ['2', '3', ....'ace']}
        # list_card_deck = [card_deck, card_deck, card_deck, card_deck]

    def random_card(self):
        # 1 step - choose random number of deck
        number_deck = random.randint(0, 3)
        # 2 step - choose the suit
        number_suit = random.randint(0, 3)
        number_suit = self.suits[number_suit]
        # 3 step - choose the card, depeneds on len of suit
        len_of_deck_suit = len(self.list_card_deck[number_deck][number_suit])
        number_card = random.randint(0, len_of_deck_suit - 1)
        #print(number_deck, number_suit, number_card)
        random_card = self.list_card_deck[number_deck][number_suit][number_card]
        #print(random_card, number_suit)
        # 4 step - remove the card
        self.list_card_deck[number_deck][number_suit].remove(self.suit[number_card])
        #print(self.list_card_deck[number_deck][number_suit])
        return random_card, number_suit

#card = Cards()
#card.cards_deck()
#result = card.random_card()
#print(result)
