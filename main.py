import pygame, sys, os, random, math

from game_logic import *
from game_loop import *
from tests import *
from menu import *

# Initialize window
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
default_players = [Zero, One, Two, Three]
players = []
for player in default_players:
    player.get_coords(width, height)
    players.append(player)

# Initialize images
images = []
for img in os.listdir("images"):
    image = pygame.image.load(os.path.join("images", img))
    image = pygame.transform.scale(image, (50, 50))
    images.append(image)
    random.shuffle(images)

# Load and start playing music
pygame.mixer.music.load("muzik.mid")
pygame.mixer.music.play(-1)

# Go to menu
menu_loop(width, height, screen, clock, images, players, mid, default_players)


