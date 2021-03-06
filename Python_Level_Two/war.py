#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project I used OOP to create a card game. This card game is the card game "War"
# for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

suits = "H D S C".split()
ranks = "2 3 4 5 6 7 8 9 10 J Q K A".split()


class Deck:
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play.
    """

    def __init__(self, suits, ranks):
        self.cards = [(s, r) for s in suits for r in ranks]
        self.played_cards = []
        print(self.cards)

    def shuffle(self):
        shuffle(self.cards)

    def split(self):
        self.first_half = self.cards[:26]
        self.second_half = self.cards[26:]


class Hand:
    """
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand.
    """

    def __init__(self, cards):
        self.cards = cards

    def __len__(self):
        return len(self.cards)

    def add(self, added_cards):
        [self.cards.insert(0, x) for x in cards]

    def draw(self):
        try:
            return self.cards.pop(-1)
        except IndexError:
            print("No cards left")
            game_on = False
        finally:
            pass


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Player can then play cards and check if they still have cards.
    """

    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
        self.active_card = ""

    def check_cards_remain(self):
        print("{a} has {b} cards".format(a=self.name, b=len(self.hand)))
        if len(self.hand) == 0:
            print("{} has lost".format(self.name))
            return False
        else:
            return True

    def pickup(self):
        [self.hand.cards.insert(0, x) for x in deck.played_cards]
        deck.played_cards = []

    def play_card(self, number_of_cards):
        if number_of_cards == 1:
            self.active_card = self.hand.draw()
            deck.played_cards.append(self.active_card)
            print(f"Cards on the table:{deck.played_cards}")

        elif number_of_cards == 3:
            if len(self.hand) < number_of_cards:
                number_of_cards = len(self.hand)
            war_cards = [self.hand.draw() for n in range(number_of_cards)]
            for card in war_cards:
                deck.played_cards.append(card)
                print(f"Cards on the table:{deck.played_cards}")


# base level functions
def rank(card):
    rank = card[1]
    if rank.isnumeric():
        return int(card[1])
    elif rank == "J":
        return 11
    elif rank == "Q":
        return 12
    elif rank == "K":
        return 13
    elif rank == "A":
        return 14
    else:
        return "Not a valid rank"


def empty_hand():
    if len(player_one.hand) == 0:
        return True
    elif len(player_two.hand) == 0:
        return True
    else:
        return False


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

#  INIT
deck = Deck(suits, ranks)
deck.shuffle()
deck.split()
hand_one = Hand(deck.first_half)
hand_two = Hand(deck.second_half)
player_one = Player("Mike", hand_one)
player_two = Player("Tom", hand_two)


#  GAME
game_on = True

while game_on:
    print("player one played " + str(player_one.active_card))
    print("player two played " + str(player_two.active_card))

    start_turn = input()
    player_one.play_card(1)
    player_two.play_card(1)
    if rank(player_one.active_card) > rank(player_two.active_card):
        player_one.pickup()
        game_on = player_two.check_cards_remain()

    elif rank(player_one.active_card) < rank(player_two.active_card):
        player_two.pickup()
        game_on = player_one.check_cards_remain()

    elif rank(player_one.active_card) == rank(player_two.active_card):
        print("its war!")
        war = True
        player_one.play_card(3)
        player_two.play_card(3)
        while war:
            player_one.play_card(1)
            player_two.play_card(1)
            if rank(player_one.active_card) > rank(player_two.active_card):
                player_one.pickup()
                game_on = player_two.check_cards_remain()
                print("{} won the war".format(player_one.name))
                war = False
            elif rank(player_one.active_card) < rank(player_two.active_card):
                player_two.pickup()
                game_on = player_one.check_cards_remain()
                print("{} won the war".format(player_two.name))
                war = False
            else:
                print("draw another")
    if empty_hand():
        game_on = False
        break

print("Game over!")
