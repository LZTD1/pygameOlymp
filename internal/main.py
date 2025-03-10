"""
Главный игровой стартер
"""

import sys

import pygame
from background import AutumnBackground
from characters.main import MainCharacter
from interface import Interface
from particles import Particles

pygame.init()

WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super-Game")


player = MainCharacter(
    {
        "start_pos": (10, 300),
        "size": (80, 100),
        "speed": 5,
        "jumping_speed": 12,
    }
)
bg = AutumnBackground(WIDTH, HEIGHT)
ui = Interface(health={"pos": (350, 10), "size": (300, 10)})
leafs = Particles("assets/background/leaf.png")
leafs.set_particles(15)

RUNNING = True
while RUNNING:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            RUNNING = False

    keys = pygame.key.get_pressed()

    bg.display(screen)
    player.run(screen, keys)
    leafs.display(screen)
    ui.display_health(screen, player)

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
