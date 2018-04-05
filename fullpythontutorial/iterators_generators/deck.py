from random import shuffle

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck(Card):
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.cards = [Card(value, suit) for suit in suits for value in values]

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, num):
        count = self.count()
        actual = min([count, num])
        if count == 0:
            raise ValueError("All card have been dealt")
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, hand_size):
        return self._deal(hand_size)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("All card have been dealt")

        shuffle(self.cards)
        return self

my_deck = Deck()
for c in my_deck:
    print(c)
