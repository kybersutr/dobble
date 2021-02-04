import pygame, sys, os, random, math

from game_logic import*
from main import *
from tests import *

def menu_loop(height, width, screen, clock, images):
    start_button = Button("START GAME", (width/2 - 150, (height - 250) * 1/3, 300, 100))
    settings_button = Button("SETTINGS", (width/2 - 150, (height - 250) * 2/3, 300, 100))
    rules_button = Button("RULES", (width/2 - 150, (height - 250) * 3/3, 300, 100))

    buttons = [start_button, settings_button, rules_button]

    slower_movement_counter = 0 # Used not to redraw the screen every loop iteration

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        if slower_movement_counter == 0:
            slower_movement_counter = 3
            screen.fill(pygame.Color(198, 142, 212))

            for button in buttons:
                button.draw(screen)


            for i in range(15):
                coord_x = random.randint(0, width)
                coord_y = random.randint(0, height)

                # Recalculate coordinates if the picture would cover the buttons
                while coord_x >= (width/2 - 200) and coord_x < (width/2 + 150) \
                        and (coord_y > 100) and (coord_y < (height - 250) * 3/3 + 100):
                    coord_x = random.randint(0, width)
                    coord_y = random.randint(0, height)

                screen.blit(images[random.randint(0, len(images)-1)], (coord_x, coord_y))

            pygame.display.flip()

        else:
            slower_movement_counter -= 1
        clock.tick(30)