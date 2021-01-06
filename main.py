import pygame, sys, os, random, math

from game_logic import *
from tests import *

unused_images = []
for img in os.listdir("images"):
    image = pygame.image.load(os.path.join("images", img))
    image = pygame.transform.scale(image, (50, 50))
    unused_images.append(image)

def draw_game():
    pass

pygame.init()

width = 1200
height = 750


screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# definuj stav hry (INITIALIZE)
# ...

New = Player(["a","b","c","d","e","f"], 1)
New.get_coords(width, height)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        else:
            if event.type == pygame.KEYDOWN:
                check_input(event.key)

    New.draw(screen)
    screen.fill(pygame.Color(198, 142, 212))

    for image in unused_images:
        screen.blit(image, (random.randint(0,width - 50), random.randint(0,height - 50)))



    draw_game()

    pygame.display.flip()
    clock.tick(30)

