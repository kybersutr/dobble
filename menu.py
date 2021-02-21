import pygame, sys, os, random, math
import game_loop
from game_logic import *


def menu_loop(width, height, screen, clock, images, players, mid, default_players, rounds = 20):
    """Draw menu with buttons. players and rounds are in default mode (4 players, 20 rounds)
    unless the user changes them in settings"""

    start_button = Button("START GAME", (width/2 - 150, (height - 250) * 1/3, 300, 100))
    settings_button = Button("SETTINGS", (width/2 - 150, (height - 250) * 2/3, 300, 100))
    rules_button = Button("RULES", (width/2 - 150, (height - 250) * 3/3, 300, 100))

    buttons = [start_button, settings_button, rules_button]

    slower_movement_counter = 0
    # Used not to redraw the screen every loop iteration (because of the moving pictures in background)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()

                if start_button.check_clicked(pos):
                    game_loop.reset(players) # Clear game state from last game
                    game_loop.game(width, height, screen, clock, players, mid, images, rounds)
                    start_button.colour = "gray" # So that it does not appear pressed when user returns to menu

                elif settings_button.check_clicked(pos):
                    # Lets the user set number of players, number of rounds and player controls
                    players, rounds, default_players = \
                        settings_loop(width, height, screen, clock, players, rounds, default_players)
                    settings_button.colour = "gray"

                elif rules_button.check_clicked(pos):
                    rules_loop(width, height, screen, clock)
                    rules_button.colour = "gray"

        if slower_movement_counter == 0: # Redraw the screen every four iterations
            slower_movement_counter = 3
            screen.fill(pygame.Color(198, 142, 212))

            for button in buttons:
                button.draw(screen)

            for i in range(15):
                # Get random coordinates of the images in the background
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

def settings_loop(width, height, screen, clock, players, rounds, default_players):
    """Lets user chose the number of players, player controls, number of rounds and turn the music on or off.
    Returns list of players, number of rounds and default players (with new controls)"""

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
                        return players, rounds, default_players

                    # Choose number of players
                    if players_buttons[0].check_clicked(pos):
                        players = [default_players[0], default_players[1]]
                    if players_buttons[1].check_clicked(pos):
                        players = [default_players[0], default_players[1], default_players[2]]
                    if players_buttons[2].check_clicked(pos):
                        players = [default_players[0], default_players[1], default_players[2], default_players[3]]

                    # Get to the loop for choosing player controls
                    if controls_button.check_clicked(pos):
                        controls_loop(width, height, screen, clock, default_players)
                        controls_button.colour = "gray"

                    # Turn music on or off
                    if music_buttons[0].check_clicked(pos):
                        pygame.mixer.music.play(-1)
                    if music_buttons[1].check_clicked(pos):
                        pygame.mixer.music.stop()

                    # Choose number of rounds
                    if rounds_buttons[0].check_clicked(pos):
                        rounds = 5
                    if rounds_buttons[1].check_clicked(pos):
                        rounds = 10
                    if rounds_buttons[2].check_clicked(pos):
                        rounds = 20
                    if rounds_buttons[3].check_clicked(pos):
                        rounds = 30
                    if rounds_buttons[4].check_clicked(pos):
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

def controls_loop(width, height, screen, clock, default_players):
    """Lets user choose player controls"""

    for player in default_players:
        player.cards = [] # Used not to draw any pictures on the screen

    settings_button = Button("SETTINGS", (width/2 - 50, height - 120, 100, 50))

    # six control keys buttons for each player (two-dimensional list)
    controls_buttons = []
    for player in default_players:
        controls = []
        for key in player.key_coords:
            controls.append(Button("", (key[0], key[1] - 10, 50, 50)))
        controls_buttons.append(controls)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if settings_button.check_clicked(pos):
                        return None

                    for player_num in range(4):
                        # Check if each button of each player is clicked
                        for i in range(6):
                            if controls_buttons[player_num][i].check_clicked(pos):
                                controls_buttons[player_num][i].draw(screen) # Show empty spot instead of player key
                                pygame.display.flip()

                                end = False
                                while end == False:
                                    # Wait for user to press a key
                                    for new_event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            sys.exit()
                                        elif new_event.type == pygame.KEYDOWN:
                                            controls_buttons[player_num][i].colour = "gray"
                                            new_key = new_event.key
                                            end = True # User pressed new key
                                        elif new_event.type == pygame.MOUSEBUTTONUP:
                                            # User clicked elsewhere, break from loop
                                            controls_buttons[player_num][i].colour = "gray"
                                            end = True
                                            break
                                        else:
                                            continue

                                        # Check if the new key does not belong to other player, if not change the button
                                        for player in default_players:
                                            if new_key in player.keys:
                                                break
                                        else:
                                            default_players[player_num].keys[i] = new_key

        screen.fill(pygame.Color(198, 142, 212))

        for player_buttons in controls_buttons:
            for i in range(6):
                player_buttons[i].draw(screen)

        for player in default_players:
            player.draw(screen, False) # False -> do not show points

        settings_button.draw(screen)

        show_instructions(width, height, screen)

        pygame.display.flip()
        clock.tick(30)

def show_instructions(width, height, screen):
    """Used in controls_loop to show instructions in the middle"""

    instructions_font = pygame.font.SysFont(None, 40)
    instructions_text1 = instructions_font.render("Click the button", True,
                                                  pygame.Color("black"))
    instructions_text2 = instructions_font.render("you want to change", True,
                                                  pygame.Color("black"))
    instructions_text3 = instructions_font.render("and press the new key.", True,
                                                  pygame.Color("black"))
    instructions_text4 = instructions_font.render("Two different players", True,
                                                  pygame.Color("black"))
    instructions_text5 = instructions_font.render("cannot share a key.", True,
                                                  pygame.Color("black"))
    screen.blit(instructions_text1, (width / 2 - instructions_text1.get_width() / 2, height/2 - 150))
    screen.blit(instructions_text2, (width / 2 - instructions_text2.get_width() / 2, height/2 - 100))
    screen.blit(instructions_text3, (width / 2 - instructions_text3.get_width() / 2, height/2 - 50))
    screen.blit(instructions_text4, (width / 2 - instructions_text4.get_width() / 2, height/2 + 40))
    screen.blit(instructions_text5, (width / 2 - instructions_text5.get_width() / 2, height/2 + 90))

def rules_loop(width, height, screen, clock):
    """Show tutorial. Tutorial is created from images of the game screen."""

    tutorial_images = []
    for img in os.listdir("tutorial"):
        tutorial_img = pygame.image.load(os.path.join("tutorial", img))
        tutorial_img = pygame.transform.smoothscale(tutorial_img, (width, height))
        tutorial_images.append(tutorial_img)

    text_font = pygame.font.SysFont(None, 40)
    tutorial_texts = []
    tutorial_texts.append((text_font.render("The goal of this game is to find", True, pygame.Color("black")),
                           text_font.render("the picture you share with the table.", True, pygame.Color("black"))))
    tutorial_texts.append((text_font.render("Press the key", True, pygame.Color("black")),
                           text_font.render("written under the shared picture.", True, pygame.Color("black"))))
    tutorial_texts.append((text_font.render("If you press the right key,", True, pygame.Color("black")),
                           text_font.render("you get a point.", True, pygame.Color("black"))))
    tutorial_texts.append((text_font.render("But be careful!", True, pygame.Color("black")),
                           text_font.render("If you press a wrong key...", True, pygame.Color("black"))))
    tutorial_texts.append((text_font.render("...", True, pygame.Color("black")),
                           text_font.render("You lose a point.", True, pygame.Color("black"))))
    tutorial_texts.append((text_font.render("Player with the most points wins.", True, pygame.Color("black")),
                           text_font.render("Have fun!", True, pygame.Color("black"))))


    menu_button = Button("MENU", (width/2 - 50, height - 120, 100, 50))
    next_button = Button(">", (width/2 + 70, height - 120, 50, 50))
    previous_button = Button("<", (width/2 - 120, height - 120, 50, 50))
    i = 0 # counts which page of the tutorial is the user currently on

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if menu_button.check_clicked(pos):
                        return None
                    if next_button.check_clicked(pos):
                        # if user is on the last page, do not show the "next" button
                        if i < len(tutorial_images) - 1:
                            i += 1
                    if previous_button.check_clicked(pos):
                        # if user is on the first page, do not show the "previous" button
                        if i > 0:
                            i -= 1

        screen.fill(pygame.Color(198, 142, 212))
        screen.blit(tutorial_images[i], (0,0))

        text = tutorial_texts[i]
        screen.blit(text[0], (width/2 - text[0].get_width()/2, 80))
        screen.blit(text[1], (width / 2 - text[1].get_width() / 2, 130))


        menu_button.draw(screen)
        if i < len(tutorial_images) - 1:
            # if user is on the last page, do not show the "next" button
            next_button.draw(screen)
        if i > 0:
            # if user is on the first page, do not show the "previous" button
            previous_button.draw(screen)

        pygame.display.flip()

        clock.tick(30)