import pygame, sys, random, math

class Card():
    def __init__(self, image, position, shared_with):
        self.image = image
        self.position = position
        self.shared_with = shared_with


class Player():
    def __init__(self, keys, num):
        self.keys = keys
        self.cards = []
        self.points = 0
        self.num = num

    def get_coords(self, width, height):
        if self.num == 0:
            self.top_left = (10, 10)
        elif self.num == 1:
            self.top_left = (width - 240, 10)
        elif self.num == 2:
            self.top_left = (10, height - 270)
        elif self.num == 3:
            self.top_left = (width - 240, height - 270)
        elif self.num == 4:
            self.top_left = (width/2 - (230/2), height/2 - (260/2))

        x, y = self.top_left[0], self.top_left[1]

        card0 = (x, y + 60)
        card1 = (x + 90, y + 60)
        card2 = (x + 180, y + 60)
        card3 = (x, y + 160)
        card4 = (x + 90, y + 160)
        card5 = (x + 180, y + 160)
        self.card_coords = [card0, card1, card2, card3, card4, card5]

        key0 = (x, y + 110)
        key1 = (x + 90, y + 110)
        key2 = (x + 180, y + 110)
        key3 = (x, y + 210)
        key4 = (x + 90, y + 210)
        key5 = (x + 180, y + 210)
        self.key_coords = [key0, key1, key2, key3, key4, key5]

    def take_cards(self):
        self.cards = mid.cards
        for card in self.cards:
            if card.shared_with == self:
                card.shared_with = None

    def draw(self, screen):
        player_font = pygame.font.SysFont(None, 50)

        name = player_font.render(f'PLAYER {self.num + 1}', True, pygame.Color("black"))
        screen.blit(name, self.top_left)

        for card in self.cards:
            screen.blit(card.image, self.card_coords[card.position])

        for i in range(len(self.keys)):
            key_text = player_font.render(self.keys[i], True, pygame.Color("black"))
            screen.blit(key_text, self.key_coords[i])



mid = Player(None, 4)
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

def check_input(key):
    """Checks if the key pressed is valid for some player. If it is and the card is shared with mid, player
    gets +1 point and card is taken, else player gets -1 point."""

    print(f"input {key}")
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