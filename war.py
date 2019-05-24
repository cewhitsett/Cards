from common import Card, Hand, Deck, Player, Game
import time
import random

class Player(Player):

    def __init__(self, is_comp=True):
        super().__init__(is_comp)

    def add_cards(self, cards):
        self.unseen.add_cards(cards)

    def discard_cards(self, cards):
        self.discard.add_cards(cards)

    def play_card(self):
        if not len(self.unseen.cards):
            random.shuffle(self.discard.cards)
            self.unseen.cards += self.discard.cards
            self.discard.cards = []

        if not len(self.unseen.cards):
            return None

        return self.unseen.pop_top()

class War(Game):

    def __init__(self):
        super().__init__("War")
        self.players = [Player() for i in range(self.np)]

    def play_game(self):
        self.init_game()
        self.print_init()
        steps = 0
        while not self.game_over():
            if steps % 10 == 0:
                self.print_summary()

            # time.sleep(.1)
            card1 = self.players[0].play_card()
            card2 = self.players[1].play_card()
            print("P1: {}       P2: {}".format(card1,card2))
            # print(card1.value,card2.value)
            if card1 == card2:
                print("Tie! I Declare War!")
                ans = self.IDW()
                if ans:
                    self.players[0].discard_cards([card1, card2])
                else:
                    self.players[1].discard_cards([card1, card2])
            elif card1 < card2:
                print("P2 Wins round!")
                self.players[1].discard_cards([card1, card2])
            else:
                print("P1 Wins round!")
                self.players[0].discard_cards([card1, card2])
            steps += 1
        winner = self.get_winner()
        print()
        print("Good game. P{} wins!".format(winner+1))

    def IDW(self):
        discard = []

        if len(self.players[0]) < 4:
            print("Player 2 Wins!")
            return False

        if len(self.players[1]) < 4:
            print("Player 1 Wins!")
            return True

        for i in range(min(3, len(self.players[0]))):
            discard.append(self.players[0].play_card())

        for i in range(min(3, len(self.players[1]))):
            discard.append(self.players[1].play_card())

        if self.game_over():
            if len(self.players[0]):
                self.players[0].discard_cards(discard)
            else:
                self.players[1].discard_cards(discard)
        else:
            card1 = self.players[0].play_card()
            card2 = self.players[1].play_card()

            print("P1: {}       P2: {}".format(card1,card2))

            if card1 == card2:
                print("Tie again! I Declare War!")
                ans = self.IDW()
                if ans:
                    self.players[0].discard_cards([card1, card2])
                    self.players[0].discard_cards(discard)
                else:
                    self.players[1].discard_cards([card1, card2])
                    self.players[1].discard_cards(discard)
                return ans
            elif card1 < card2:
                print("P2 Wins round!")
                self.players[1].discard_cards([card1, card2])
                self.players[1].discard_cards(discard)
                return False
            else:
                print("P1 Wins round!")
                self.players[0].discard_cards([card1, card2])
                self.players[0].discard_cards(discard)
                return True

    def print_init(self):
        print("Welcome to War!")
        print("There's not much here, as this game is completely automated.")

    def print_summary(self):
        cl1, cl2 = len(self.players[0]), len(self.players[1])
        print()
        print("A summary:")
        print("P1: Cards Left {}      P2: Cards Left {}".format(cl1, cl2))
        print()

    def init_game(self):
        for i in range(len(self.deck)):
            c = self.deck.draw_card()
            self.players[i%self.np].add_cards(c)

    def game_over(self):
        return any([len(x)==0 for x in self.players])

    def reset_game(self):
        self.players = [Player() for i in range(self.np)]
        self.deck    = Deck()

    def get_winner(self):
        return int( len(self.players[1]) != 0 )

if __name__ == "__main__":
    g = War()
    g.play_game()
