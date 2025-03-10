"""
Главный игровой стартер
"""

import sys

import pygame
from background import AutumnBackground
from characters.main import MainCharacter

pygame.init()

WIDTH, HEIGHT = 1000, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Платформер")

player_config = {
    "start_pos": (10, 300),
    "size": (80, 100),
    "speed": 5,
    "jumping_speed": 12,
}
player = MainCharacter(player_config)
bg = AutumnBackground(WIDTH, HEIGHT, particles_count=15)

RUNNING = True
while RUNNING:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            RUNNING = False
    bg.display(screen)

    keys = pygame.key.get_pressed()

    player.run(screen, keys)

    pygame.display.update()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
