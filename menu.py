import pygame, sys, os, random, math
import game_loop
from game_logic import *


def menu_loop(width, height, screen, clock, images, players, mid, rounds = 20):
    start_button = Button("START GAME", (width/2 - 150, (height - 250) * 1/3, 300, 100))
    settings_button = Button("SETTINGS", (width/2 - 150, (height - 250) * 2/3, 300, 100))
    rules_button = Button("RULES", (width/2 - 150, (height - 250) * 3/3, 300, 100))

    buttons = [start_button, settings_button, rules_button]

    slower_movement_counter = 0 # Used not to redraw the screen every loop iteration

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if start_button.check_clicked(pos):
                    game_loop.reset(players)
                    game_loop.game(width, height, screen, clock, players, mid, images, rounds)

                elif settings_button.check_clicked(pos):
                    players, rounds = settings_loop(width, height, screen, clock, players, rounds)
                    settings_button.colour = "gray"

                elif rules_button.check_clicked(pos):
                    rules_loop(width, height, screen, clock)
                    rules_button.colour = "gray"

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

def settings_loop(width, height, screen, clock, players, rounds):

    # Number of players buttons
    players_buttons = []

    players_buttons.append(Button("2", (width/2 - 135, 120, 50, 50)))
    players_buttons.append(Button("3", (width / 2 - 25, 120, 50, 50)))
    players_buttons.append(Button("4", (width / 2 + 85, 120, 50, 50)))

    controls_button = Button("CONTROLS", (width/2 - 75, 195, 150, 40))

    # Music buttons
    music_buttons = []

    music_buttons.append(Button("ON", (width/2 - 105, 345, 70, 50)))
    music_buttons.append(Button("OFF", (width/2 + 35, 345, 70, 50)))

    # Number of rounds buttons
    rounds_buttons = []

    rounds_buttons.append(Button("5", (width/2 - (25 + 4 * 50), 495, 50, 50)))
    rounds_buttons.append(Button("10", (width / 2 - (25 + 2 * 50), 495, 50, 50)))
    rounds_buttons.append(Button("20", (width / 2 - 25, 495, 50, 50)))
    rounds_buttons.append(Button("30", (width / 2 + (25 + 50), 495, 50, 50)))
    rounds_buttons.append(Button("50", (width / 2 + (25 + 3 * 50), 495, 50, 50)))

    menu_button = Button("MENU", (width/2 - 50, height - 120, 100, 50))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if menu_button.check_clicked(pos):
                        return players, rounds

                    if players_buttons[0].check_clicked(pos):
                        Zero = Player([113, 119, 101, 97, 115, 100], 0)
                        One = Player([116, 121, 117, 103, 104, 106], 1)
                        players = [Zero, One]
                    elif players_buttons[1].check_clicked(pos):
                        Zero = Player([113, 119, 101, 97, 115, 100], 0)
                        One = Player([116, 121, 117, 103, 104, 106], 1)
                        Two = Player([56, 57, 48, 105, 111, 112], 2)
                        players = [Zero, One, Two]
                    elif players_buttons[2].check_clicked(pos):
                        Zero = Player([113, 119, 101, 97, 115, 100], 0)
                        One = Player([116, 121, 117, 103, 104, 106], 1)
                        Two = Player([56, 57, 48, 105, 111, 112], 2)
                        Three = Player([107, 108, 59, 44, 46, 47], 3)
                        players = [Zero, One, Two, Three]

                    if music_buttons[0].check_clicked(pos):
                        pygame.mixer.music.play()
                    elif music_buttons[1].check_clicked(pos):
                        pygame.mixer.music.stop()

                    if rounds_buttons[0].check_clicked(pos):
                        rounds = 5
                    elif rounds_buttons[1].check_clicked(pos):
                        rounds = 10
                    elif rounds_buttons[2].check_clicked(pos):
                        rounds = 20
                    elif rounds_buttons[3].check_clicked(pos):
                        rounds = 30
                    elif rounds_buttons[4].check_clicked(pos):
                        rounds = 50


        screen.fill(pygame.Color(198, 142, 212))

        # Draw headers and buttons on screen
        header_font = pygame.font.SysFont(None, 50)

        players_text = header_font.render("NUMBER OF PLAYERS", True, pygame.Color("black"))
        music_text = header_font.render("MUSIC", True, pygame.Color("black"))
        rounds_text = header_font.render("NUMBER OF ROUNDS", True, pygame.Color("black"))
        screen.blit(players_text, (width / 2 - players_text.get_width() / 2, 65))
        screen.blit(music_text, (width / 2 - music_text.get_width() / 2, 290))
        screen.blit(rounds_text, (width / 2 - rounds_text.get_width() / 2, 440))

        for button in players_buttons:
            button.draw(screen)
        controls_button.draw(screen)

        for button in music_buttons:
            button.draw(screen)

        for button in rounds_buttons:
            button.draw(screen)
        menu_button.draw(screen)

        pygame.display.flip()
        clock.tick(30)

def rules_loop(width, height, screen, clock):



    menu_button = Button("MENU", (width/2 - 50, height - 120, 100, 50))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if menu_button.check_clicked(pos):
                        return None

        screen.fill(pygame.Color(198, 142, 212))

        menu_button.draw(screen)

        pygame.display.flip()
        clock.tick(30)