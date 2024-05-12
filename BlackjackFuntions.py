import random
import json
from PIL import Image


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        if self.rank == 1:
            self.card_scores = [1, 11]
        elif self.rank >= 11 and self.rank <= 13:
            self.card_scores = [10, 10]
        else:
            self.card_scores = [self.rank, self.rank]

        if self.rank == 1:
            self.short_rank = 'A'
        elif self.rank == 11:
            self.short_rank = 'J'
        elif self.rank == 12:
            self.short_rank = 'Q'
        elif self.rank == 13:
            self.short_rank = 'K'
        else:
            self.short_rank = str(self.rank)

        if self.suit == 'Spades':
            self.short_suit = 'S'
        elif self.suit == 'Hearts':
            self.short_suit = 'H'
        elif self.suit == 'Clubs':
            self.short_suit = 'C'
        else:
            self.short_suit = 'D'

        self.image_location = 'Resources/{}{}.png'.format(self.short_rank, self.short_suit)

    # def __repr__(self):
    #     true_rank = ''
    #     if self.rank == 1:
    #         true_rank = 'Ace'
    #     elif self.rank == 11:
    #         true_rank = 'Jack'
    #     elif self.rank == 12:
    #         true_rank = 'Queen'
    #     elif self.rank == 13:
    #         true_rank = 'King'
    #     else:
    #         true_rank = str(self.rank)
    #     return '{} of {}'.format(true_rank, self.suit)

### Deck Class
### Variables
suits = ('Spades', 'Hearts', 'Clubs', 'Diamonds')

class Deck:
    def __init__(self, number_of_decks):
        self.number_of_decks = number_of_decks
        self.cards = []
        self.create(self.number_of_decks)

    def __repr__(self):
        return 'Game deck has {} cards remaining'.format(len(self.cards))

    def create(self, number_of_decks):
        decks = [Card(rank, suit) for suit in suits for rank in range(1, 14)
                 for deck in range(number_of_decks)]
        decks = random.sample(decks, len(decks))
        self.cards.extend(decks)

    def draw(self):
        drawn_card = self.cards[0]
        self.cards.remove(self.cards[0])
        return drawn_card

    def reset(self):
        self.cards = []
        self.create(self.number_of_decks)