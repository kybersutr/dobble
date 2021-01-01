import pygame, sys, random, math

class Card():
    def __init__(self, image, position, shared_with):
        self.image = image
        self.position = position
        self.shared_with = shared_with


class Player():
    def __init__(self, keys):
        self.keys = keys
        self.cards = []
        self.points = 0


mid = Player(None)
players = []
unused_images = []

def generate_new_cards(players, unused_images):
    """Takes one card from every player, which is not shared with another player.
    The cards are then supplemented with others (with unused images) to make
    a total of 6."""

    new_cards = []
    positions = [0,1,2,3,4,5]
    random.shuffle(positions)
    random.shuffle(unused_images)

    for player in players:
        random.shuffle(player.cards)
        for card in player.cards:
            if card.shared_with == None:
                card.shared_with = mid
                pos = positions.pop()
                new_cards.append(Card(card.image, pos, player))
                break

    for i in range(len(positions)):
        new_image = unused_images.pop()
        pos = positions.pop()
        new_cards.append(Card(new_image, pos, None))

    mid.cards = new_cards

def take_card():
    pass

def test1_generate():
    Player1 = Player(None)
    Player2 = Player(None)

    unused_images = ["Evžen","Oněgin","Je","Placeholder","Který","Z","Nějakého","Důvodu","Používám"]

    cards1 = [Card("1.0", 0, None), Card("1.1", 1, None), Card("1.2", 2, None), Card("1.3", 3, None), Card("1.4", 4, None), Card("1.5", 5, None)]
    cards2 = [Card("2.0", 0, None), Card("2.1", 1, None), Card("2.2", 2, None), Card("2.3", 3, None), Card("2.4", 4, None), Card("2.5", 5, None)]

    Player1.cards = cards1
    Player2.cards = cards2

    players = [Player1, Player2]

    generate_new_cards(players, unused_images)

    for card in mid.cards:
        print(card.image, card.position, card.shared_with)

    for card in Player1.cards:
        print(card.image, card.position, card.shared_with)

    for card in Player2.cards:
        print(card.image, card.position, card.shared_with)