import pygame, sys, os, random, math
from game_logic import *
import menu

def reset(players):
    """Clears the game state after last game"""
    for player in players:
        player.cards = []
        player.points = 0

def game(width, height, screen, clock, players, mid, images, rounds):

    countdown = rounds

    unused_images = [] # dont modify the original list
    for image in images:
        unused_images.append(image)

    for player in players:
        player.get_coords(width, height)
        for i in range(6):
            new_image = unused_images.pop()
            player.cards.append(Card(new_image, i, None))

    mid.get_coords(width, height)
    generate_new_cards(players, unused_images, mid)

    menu_button = Button("MENU", (width/2 - 50, height - 120, 100, 50))

    rounds_font = pygame.font.SysFont(None, 50)

    # main game loop
    while True:
        if countdown <= 0:
            winning_screen(width, height, screen, clock, players, images, rounds)
            return None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                if event.type == pygame.KEYDOWN:
                    if check_input(event.key, players, unused_images, mid):
                        countdown -= 1
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if menu_button.check_clicked(pos):
                        return None

        screen.fill(pygame.Color(198, 142, 212))

        if countdown != 1:
            rounds_text = rounds_font.render(f"{countdown} ROUNDS TO GO!", True, pygame.Color("black"))
        else:
            rounds_text = rounds_font.render("LAST ROUND!", True, pygame.Color("black"))
        screen.blit(rounds_text, (width / 2 - rounds_text.get_width() / 2, 120))

        for player in players:
            player.draw(screen)
        mid.draw(screen)

        menu_button.draw(screen)

        pygame.display.flip()
        clock.tick(30)

def winning_screen(width, height, screen, clock, players, images, rounds):

    menu_button = Button("MENU", (width / 2 - 50, height - 120, 100, 50))

    max_points = float("-inf")
    winners = []
    for player in players:
        if player.points > max_points:
            max_points = player.points
            winners = [player]

        elif player.points == max_points:
            winners.append(player)

    if len(winners) > 1:
        to_print = ["It's a draw between"]
        second_line = ""
        for winner in winners:
            second_line += f" {winner.name},"
        second_line = second_line[:-1] + "!"
        to_print.append(second_line)
    else:
        if max_points != 1:
            to_print = ["The winner is",  f"{winners[0].name} with {max_points} points!"]
        else:
            to_print = ["The winner is", f"{winners[0].name} with 1 point!"]

    win_font = pygame.font.SysFont(None, 70)
    win_texts = []
    for i in to_print:
        win_texts.append(win_font.render(i, True, pygame.Color("black")))


    slower_movement_counter = 0 # Used not to redraw the screen every loop iteration
    menu_button = Button("MENU", (width / 2 - 50, height - 120, 100, 50))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if menu_button.check_clicked(pos):
                    return None


        if slower_movement_counter == 0:
            slower_movement_counter = 3
            screen.fill(pygame.Color(198, 142, 212))

            menu_button.draw(screen)

            screen.blit(win_texts[0], (width / 2 - win_texts[0].get_width() / 2, 210))
            screen.blit(win_texts[1], (width / 2 - win_texts[1].get_width() / 2, 300))


            for i in range(15):
                coord_x = random.randint(0, width)
                coord_y = random.randint(0, height)

                # Recalculate coordinates if the picture would cover the upper text, lower text or menu button
                while (((coord_x >= (width / 2 - (win_texts[0].get_width() / 2 + 50))) and (coord_x < (width / 2 + win_texts[0].get_width() / 2)) \
                        and (coord_y > 210 - 50) and (coord_y < 300)) \
                    or ((coord_x >= (width / 2 - (win_texts[1].get_width() / 2 + 50))) and (coord_x < (width / 2 + win_texts[1].get_width() / 2)) \
                        and (coord_y > 300 - 50) and (coord_y < 370)) \
                    or ((coord_x >= (menu_button.position[0] - 50)) and coord_x < ((menu_button.position[0] + menu_button.position[2])) \
                        and (coord_y > menu_button.position[1] - 50) and (coord_y < menu_button.position[1] + menu_button.position[3]))):
                    coord_x = random.randint(0, width)
                    coord_y = random.randint(0, height)

                screen.blit(images[random.randint(0, len(images)-1)], (coord_x, coord_y))

            pygame.display.flip()

        else:
            slower_movement_counter -= 1
        clock.tick(30)