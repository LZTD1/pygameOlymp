"""
Модуль описания частиц на экране
"""

import random

import pygame
from helper import resource_path

DEFAULT_PARAM = {
    "width": 20,
    "height": 20,
}


class Particles:
    """
    Класс родитель для всех частич
    """

    def __init__(
        self,
        particle_path,
        particle_param=DEFAULT_PARAM,
    ):
        self.particle = pygame.transform.scale(
            pygame.image.load(resource_path(particle_path)),
            (particle_param["width"], particle_param["height"]),
        )
        self.particle_rect = self.particle.get_rect(topleft=(0, 0))
        self.all_particles = []

    def set_particles(self, count):
        """
        Функция генерирует нужно количество частиц
        """
        self.all_particles = []
        for _ in range(count):
            speed_x = random.uniform(-1, 1)
            speed_y = random.uniform(0.5, 1)
            delay = random.randint(0, 100)
            self.all_particles.append(
                {
                    "speed": [speed_x, speed_y],
                    "delay": delay,
                    "pos": [None, None],
                }
            )

    def display(self, screen: pygame.Surface):
        """
        Главная функция отображения частиц
        """
        self.particles_update(screen.get_width(), screen.get_height())
        for particle in self.all_particles:
            screen.blit(self.particle, particle["pos"])

    def particles_update(self, width, height):
        """
        Функция обновления частиц, для имитации полета
        """
        for particle in self.all_particles:
            if particle["pos"] == [None, None]:
                particle["pos"] = [
                    random.randint(0, width),
                    random.randint(-height, 0),
                ]
            if particle["delay"] > 0:
                particle["delay"] -= 1
            else:
                particle["pos"][0] += particle["speed"][0]
                particle["pos"][1] += particle["speed"][1]

                if particle["pos"][1] > height:
                    particle["pos"] = [
                        random.randint(0, width),
                        random.randint(-height, 0),
                    ]
                    particle["delay"] = random.randint(0, 100)
