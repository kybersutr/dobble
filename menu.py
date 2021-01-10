import pygame, sys, os, random, math

from game_logic import*
from main import *
from tests import *

def draw_button(text, position, screen):
    pygame.draw.rect(screen, "gray", position)

    button_font = pygame.font.Font('freesansbold.ttf', 14)
    button_surface = button_font.render(text, True,  "black")
    button_rect = button_surface.get_rect()
    button_rect.center = (position[0] + 1/2 * position[2], position[1] + 1/2 * position[3])

    screen.blit(button_surface, button_rect)