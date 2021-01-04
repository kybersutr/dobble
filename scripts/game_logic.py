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

    def take_cards(self):
        self.cards = mid.cards
        for card in self.cards:
            if card.shared_with == self:
                card.shared_with = None



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

def check_input(players, key):
    """Checks if the key pressed is valid for some player. If it is and the card is shared with mid, player
    gets +1 point and card is taken, else player gets -1 point."""
    for player in players:
        if key in player.keys:
            pos = player.keys.index(key)
            for card in player.cards:
                if card.position == pos:
                    if card.shared_with == mid:
                        player.points += 1
                        player.take_cards()
                        return None
                    else:
                        player.points -= 1
                        return None