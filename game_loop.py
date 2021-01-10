import pygame, sys, os, random, math

from game_logic import*
from main import *
from tests import *
from menu import draw_button

def game(width, height, screen, clock, players, mid):
    unused_images = []
    for img in os.listdir("images"):
        image = pygame.image.load(os.path.join("images", img))
        image = pygame.transform.scale(image, (50, 50))
        unused_images.append(image)
        random.shuffle(unused_images)

    for player in players:
        player.get_coords(width, height)
        for i in range(6):
            new_image = unused_images.pop()
            player.cards.append(Card(new_image, i, None))

    mid.get_coords(width, height)
    generate_new_cards(players, unused_images, mid)

    # main game loop
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

        draw_button("MENU", (width/2 - 50, height - 60, 100, 50), screen)

        pygame.display.flip()
        clock.tick(30)
