"""
Моудль UI интерфейса игры
"""

import pygame
from characters.main import Character

STATS_PADDING = 10
STAT_WIDTH = 300
STAT_HEIGHT = 10

STATS_CONFIG = {
    'pos': (0, 0),
    'stamina_color': (43, 71, 196),
    'health_color': (200, 0, 0),
    'bg_color': (0, 0, 0),
}

class Interface:
    """
    Класс интерфейса игры
    """

    def __init__(self, stats=STATS_CONFIG):
        self.stats = {
            "bg": pygame.Rect(
                stats["pos"][0],
                stats["pos"][1],
                STAT_WIDTH + STATS_PADDING,
                STAT_HEIGHT + STATS_PADDING * 3,  # Added padding between health and stamina bars
            ),
            "health": pygame.Rect(
                stats["pos"][0] + STATS_PADDING / 2,
                stats["pos"][1] + STATS_PADDING / 2,
                STAT_WIDTH,
                STAT_HEIGHT,
            ),
            "stamina": pygame.Rect(
                stats["pos"][0] + STATS_PADDING / 2,
                stats["pos"][1] + STAT_HEIGHT + STATS_PADDING,  # Positioned below health
                STAT_WIDTH,
                STAT_HEIGHT,
            ),
        }
        self.colors = {
            'health': stats['health_color'],
            'stamina': stats['stamina_color'],
            'bg': stats['bg_color'],
        }

    def display_stats(self, screen: pygame.Surface, character: Character):
        """
        Отображение стамины и здоровья персонажа
        """
        health_ratio = character.base_stats['health']["now"] / character.base_stats['health']["max"]
        stamina_ratio = character.base_stats['stamina']["now"] / character.base_stats['stamina']["max"]

        self.stats["health"].width = int(STAT_WIDTH * health_ratio)
        self.stats["stamina"].width = int(STAT_WIDTH * stamina_ratio)

        pygame.draw.rect(screen, (50, 50, 50), self.stats["bg"])

        pygame.draw.rect(screen, self.colors["bg"], self.stats["bg"])
        pygame.draw.rect(screen, self.colors["health"], self.stats["health"])
        pygame.draw.rect(screen, self.colors["stamina"], self.stats["stamina"])