"""
Модуль заднего фона игры
"""

import random

import pygame
from helper import resource_path


class AutumnBackground(pygame.sprite.Sprite):
    """
    Класс весеннего заднего фона
    """

    def __init__(self, size_x, size_y, particles_count):
        super().__init__()  # Вызов конструктора родительского класса
        self.size = (size_x, size_y)

        self.background = pygame.transform.scale(
            pygame.image.load(
                resource_path("assets/background/background.png")
            ),
            self.size,
        )
        self.rect = self.background.get_rect(topleft=(0, 0))

        self.leaf = pygame.transform.scale(
            pygame.image.load(resource_path("assets/background/leaf.png")),
            (20, 20),
        )
        self.leaf_rect = self.leaf.get_rect(topleft=(0, 0))

        self.particles = []
        for _ in range(particles_count):
            x = random.randint(0, self.size[0])
            y = random.randint(-self.size[1], 0)
            speed_x = random.uniform(-1, 1)
            speed_y = random.uniform(0.5, 1)
            delay = random.randint(0, 100)
            self.particles.append([x, y, speed_x, speed_y, delay])

    def display(self, screen: pygame.Surface):
        """
        Отрисовка занего фона на экране
        """
        screen.blit(self.background, self.rect)
        self.particles_update()
        for particle in self.particles:
            screen.blit(self.leaf, (particle[0], particle[1]))

    def particles_update(self):
        """
        Изменение положения листьев
        """
        for particle in self.particles:
            if particle[4] > 0:
                particle[4] -= 1
            else:
                particle[0] += particle[2]
                particle[1] += particle[3]

                if particle[1] > self.size[1]:
                    particle[0] = random.randint(0, self.size[0])
                    particle[1] = random.randint(-self.size[1], 0)
                    particle[4] = random.randint(0, 100)
