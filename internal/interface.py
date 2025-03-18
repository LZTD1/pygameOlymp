"""
Моудль UI интерфейса игры
"""

import pygame

from characters.main import Character

STATS_PADDING = 10
STAT_WIDTH = 300
STAT_HEIGHT = 10

SLOT_SIZE = 30
SLOT_PADDING = 5
SLOT_BORDER = 2

STATS_CONFIG = {
    'pos': (0, 0),
    'stamina_color': (43, 71, 196),
    'health_color': (200, 0, 0),
    'bg_color': (0, 0, 0),
    'border_color': (43, 43, 43),
}

INVENTORY_CONFIG = {
    'pos': (0, 0),
    'border_color': (43, 71, 196),
    'fill_color': (50, 50, 50),
    'active_color': (0, 255, 0),
}


class Interface:
    """
    Класс интерфейса игры
    """

    def __init__(self, stats=STATS_CONFIG, inventory=INVENTORY_CONFIG):
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
            'border_color': stats['border_color'],
        }

        self.inventory_config = inventory
        self.inventory_slots = []
        self._create_inventory()

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
        pygame.draw.rect(screen, self.inventory_config['border_color'], self.stats["bg"], SLOT_BORDER)
        pygame.draw.rect(screen, self.colors["health"], self.stats["health"])
        pygame.draw.rect(screen, self.colors["stamina"], self.stats["stamina"])

    def display_inventory(self, screen: pygame.Surface, character: Character):
        """
        Отображение инвентаря игрока в стиле Minecraft
        """
        for i, slot in enumerate(self.inventory_slots):
            pygame.draw.rect(screen, self.inventory_config['fill_color'], slot)

            if i == character.inventory['active_slot']:
                pygame.draw.rect(screen, self.inventory_config['active_color'], slot, SLOT_BORDER)
            else:
                pygame.draw.rect(screen, self.inventory_config['border_color'], slot, SLOT_BORDER)
            # TODO: Отображение картинки оружия

    def _create_inventory(self):
        """
        Метод создающий ячейки
        """

        for i in range(9):
            slot_x = self.inventory_config['pos'][0] + i * (SLOT_SIZE + SLOT_PADDING)
            slot_y = self.inventory_config['pos'][1]
            slot_rect = pygame.Rect(slot_x, slot_y, SLOT_SIZE, SLOT_SIZE)
            self.inventory_slots.append(slot_rect)
