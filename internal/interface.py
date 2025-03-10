"""
Моудль UI интерфейса игры
"""

import pygame
from characters.main import Character

HEALTH_CONFIG = {"pos": (0, 0), "size": (300, 10)}


class Interface:
    """
    Класс интерфейса игры
    """

    def __init__(self, health=HEALTH_CONFIG):
        self.health = {
            "bg": pygame.Rect(
                health["pos"][0],
                health["pos"][1],
                health["size"][0],
                health["size"][1],
            ),
            "main": pygame.Rect(
                health["pos"][0],
                health["pos"][1],
                health["size"][0],
                health["size"][1],
            ),
        }

    def display_health(self, screen: pygame.Surface, character: Character):
        """
        Отображение здоровья персонажа
        """
        health_ratio = character.health["now"] / character.health["max"]

        self.health["main"].width = int(self.health["bg"].width * health_ratio)

        pygame.draw.rect(screen, (50, 50, 50), self.health["bg"])

        pygame.draw.rect(screen, (200, 0, 0), self.health["main"])
