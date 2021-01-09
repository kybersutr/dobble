import pygame, sys, os, random, math

from game_logic import *
from tests import *
from game_loop import *

pygame.init()
pygame.display.set_caption('Dobble')

width = 1100
height = 750


screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

Zero = Player([113, 119, 101, 97, 115, 100], 0)
One = Player([116, 121, 117, 103, 104, 106], 1)
Two = Player([56, 57, 48, 105, 111, 112], 2)
Three = Player([107, 108, 59, 44, 46, 47], 3)
mid = Player(None, 4)
players = [Zero, One, Two, Three]

game()


