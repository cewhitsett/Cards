import random

class Card:

    def __init__(self, suite, value):
        assert (0 <= suite <= 3), "Invalid suite"
        assert (2 <= value <= 14), "Invalid value"

        self.suite = suite
        self.value = value

    def get_suite(self):
        if   self.suite == 0:
            return "hearts"
        elif self.suite == 1:
            return "diamonds"
        elif self.suite == 2:
            return "spades"
        elif self.suite == 3:
            return "clubs"
        else:
            return ""

    def get_value(self):
        if self.value <= 10:
            return str(self.value)
        if self.value == 14:
            return "ace"

    def get_color(self):
        if self.suite < 2:
            return "red"
        return "black"

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self,other):
        return self.value < other.value

    def __gt__(self,other):
        return self.value > other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __repr__(self):
        return "{} of {}".format(self.get_value(), self.get_suite()).title()

class Deck:

    def __init__(self):
        self.deck    = []
        self.discard = []
        self.full    = []
        # Suites:
        #   0 - Hearts
        #   1 - Diamonds
        #   2 - Spades
        #   3 - Clubs
        for suite in range(4):
            # Values are 2-10 for numbers cards
            # Jacks are 11, Queens 12, Kings 13, Aces 14
            for value in range(2,15):
                c = Card(suite, value)
                self.full.append(c)

        self.deck = self.full[::]
        random.shuffle(self.deck)

    # Set the deck to be the full deck again
    def reset(self):
        self.deck = self.full[::]
        random.shuffle(self.deck)

    # Draw n cards, updating variables as needed
    def draw_card(self, n=1):
        # If we can't draw enough cards, add the discard
        if n > len(self.deck):
            random.shuffle(self.discard)
            self.deck += self.discard
            self.discard = []

        ret = []
        # Stop when we hit n, or run out off all cards
        stop = min(len(self.deck), n)
        for i in range(stop):
            ret.append(self.deck.pop(0))

        return ret

    # Add cards to discard pile
    def discard(self, cards):
        if type(cards) == list:
            for c in cards:
                self.discard.append(c)
        if type(cards) == Card:
            self.discard.append(c)

    def __len__(self):
        return len(self.deck)


def Hand:

    def __init__(self, cards=[], hid=[]):
        self.down = hid[::]
        self.face = cards[::]

    def add_cards(self,cards):
        if type(cards) == list:
            for c in cards:
                self.face.append(c)
        if type(cards) == Card:
            self.face.append(c)

    def flip(self):
        self.face, self.down = self.down, self.face