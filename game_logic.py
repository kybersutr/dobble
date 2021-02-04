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

        if num == 4:
            self.name = "TABLE"
        else:
            self.name = f"PLAYER {num + 1}"

    def get_coords(self, width, height):
        padding = 60

        if self.num == 0:
            self.top_left = (padding, padding)
        elif self.num == 1:
            self.top_left = (width - 230 - padding, padding)
        elif self.num == 2:
            self.top_left = (padding, height - 260 - padding)
        elif self.num == 3:
            self.top_left = (width - 230 - padding, height - 260 - padding)
        elif self.num == 4:
            self.top_left = (width/2 - (230/2), height/2 - (260/2))

        x, y = self.top_left[0], self.top_left[1]

        self.points_coords = (self.top_left[0] , self.top_left[1] + 35)

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

        if self.num == 4:
            self.middle = (width/2, height/2)

    def take_cards(self, mid):
        used = []
        for card in self.cards:
            if card.shared_with == None:
                used.append(card.image)
            elif card.shared_with != mid:
                other_player = card.shared_with
                for other_card in other_player.cards:
                    if other_card.shared_with == self:
                        other_card.shared_with = None

        self.cards = mid.cards
        for card in self.cards:
            if card.shared_with == self:
                card.shared_with = None

            elif card.shared_with != None:
                other_player = card.shared_with
                for other_card in other_player.cards:
                    if other_card.shared_with == mid:
                        other_card.shared_with = self
        return(used)

    def draw(self, screen):
        if self.num == 4:
            pygame.draw.circle(screen, "white", self.middle, 350/2)

        player_font = pygame.font.SysFont(None, 50)
        key_font = pygame.font.SysFont(None, 40)
        points_font = pygame.font.SysFont(None, 30)

        name_text = player_font.render(self.name, True, pygame.Color("black"))
        screen.blit(name_text, (self.top_left[0] + 230/2 - name_text.get_width()/2, self.top_left[1]))

        for card in self.cards:
            screen.blit(card.image, self.card_coords[card.position])

        if self.num != 4:
            points_text = points_font.render(f"points: {self.points}", True, pygame.Color("black"))
            screen.blit(points_text, (self.points_coords[0] + 230/2 - points_text.get_width()/2, self.points_coords[1]))

        if self.num != 4:
            for i in range(len(self.keys)):
                key_text = key_font.render(pygame.key.name(self.keys[i]), True, pygame.Color("black"))
                screen.blit(key_text, (self.key_coords[i][0] + 50/2 - key_text.get_width()/2, self.key_coords[i][1] - 50/2 + key_text.get_height()))


class Button():

    def __init__(self, text, position):
        self.text = text
        self.position = position

    def draw(self, screen):
        pygame.draw.rect(screen, "gray", self.position)

        button_font = pygame.font.Font('freesansbold.ttf', int(self.position[3]/3))
        button_surface = button_font.render(self.text, True, "black")
        button_rect = button_surface.get_rect()
        button_rect.center = (self.position[0] + 1 / 2 * self.position[2], self.position[1] + 1 / 2 * self.position[3])

        screen.blit(button_surface, button_rect)

mid = Player(None, 4)
players = []
unused_images = []

def generate_new_cards(players, unused_images, mid):
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

def check_input(key, players, unused_images, mid):
    """Checks if the key pressed is valid for some player. If it is and the card is shared with mid, player
    gets +1 point and card is taken, else player gets -1 point."""

    for player in players:
        if key in player.keys:
            pos = player.keys.index(key)
            for card in player.cards:
                if card.position == pos:
                    if card.shared_with != None and card.shared_with.num == 4:
                        player.points += 1
                        recycle = player.take_cards(mid)
                        generate_new_cards(players, unused_images, mid)
                        for i in recycle:
                            unused_images.append(i)

                        return None
                    else:
                        player.points -= 1
                        return None