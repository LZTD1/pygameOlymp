"""
Модуль заднего фона игры
"""

import pygame
from helper import resource_path


class AutumnBackground(pygame.sprite.Sprite):
    """
    Класс весеннего заднего фона
    """

    def __init__(self, size_x, size_y):
        super().__init__()
        self.size = (size_x, size_y)

        self.background = pygame.transform.scale(
            pygame.image.load(
                resource_path("assets/background/background.png")
            ),
            self.size,
        )
        self.rect = self.background.get_rect(topleft=(0, 0))

    def display(self, screen: pygame.Surface):
        """
        Отрисовка занего фона на экране
        """
        screen.blit(self.background, self.rect)
