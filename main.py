import pygame, sys, os, random, math

from game_logic import *
from tests import *

unused_images = []
for img in os.listdir("images"):
    image = pygame.image.load(os.path.join("images", img))
    image = pygame.transform.scale(image, (50, 50))
    unused_images.append(image)
    random.shuffle(unused_images)

pygame.init()
pygame.display.set_caption('Dobble')

width = 1200
height = 750


screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# definuj stav hry (INITIALIZE)
# ...

Zero = Player([113, 119, 101, 97, 115, 100], 0)
One = Player([116, 121, 117, 103, 104, 106], 1)
Two = Player([56, 57, 48, 105, 111, 112], 2)
Three = Player([107, 108, 59, 44, 46, 47], 3)
mid = Player(None, 4)
players = [Zero, One, Two, Three]
for player in players:
    player.get_coords(width, height)
    for i in range(6):
        new_image = unused_images.pop()
        player.cards.append(Card(new_image, i, None))

mid.get_coords(width, height)
generate_new_cards(players, unused_images, mid)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            if event.type == pygame.KEYDOWN:
                check_input(event.key, players, unused_images, mid)

    screen.fill(pygame.Color(198, 142, 212))
    for player in players:
        player.draw(screen)
    mid.draw(screen)


    pygame.display.flip()
    clock.tick(30)

