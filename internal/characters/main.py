"""
Модуль главного персонажа игры
"""

import pygame

from internal.helper import resource_path

GRAVITY = 0.8
ANIMATION_SPEED = 0.1

JUMP_COST = 10

class Character(pygame.sprite.Sprite):
    """
    Родитель для всех персонажей в игре
    """

    def __init__(self, config):
        super().__init__()
        self.config = config
        self.rect = pygame.Rect(config["start_pos"], config["size"])
        self.gravity = GRAVITY
        self.vertical_speed = 0
        self.on_ground = True
        self.base_stats = {
            'health': {
                "max": 100,
                "now": 10,
                "regeneration": 0.05,
            },
            "stamina": {
                "max": 100,
                "now": 10,
                "regeneration": 0.1
            }
        }
        self.inventory = [None] * 9

    def move_left(self):
        """
        Движение в лево, не пересекая границу
        """
        if self.rect.x - self.config["speed"] > 0:
            self.rect.x -= self.config["speed"]

    def move_right(self, width):
        """
        Движение в право, не пересекая границу
        """
        if self.rect.x + self.config["speed"] + self.rect.width <= width:
            self.rect.x += self.config["speed"]

    def apply_gravity(self):
        """
        Гравитация персонажей
        """
        if not self.on_ground:
            self.vertical_speed += self.gravity
            self.rect.y += self.vertical_speed
            if self.rect.y >= self.config["start_pos"][1]:
                self.rect.y = self.config["start_pos"][1]
                self.on_ground = True
                self.vertical_speed = 0

    def regeneration(self):
        if self.base_stats['health']["now"] < self.base_stats['health']["max"]:
            self.base_stats['health']["now"] += self.base_stats['health']["regeneration"]
        if self.base_stats['stamina']["now"] < self.base_stats['stamina']["max"]:
            self.base_stats['stamina']["now"] += self.base_stats['stamina']["regeneration"]


class MainCharacter(Character):
    """
    Класс главного героя
    """

    def __init__(self, config):
        super().__init__(config)
        self.animation = {
            "sprites": [
                pygame.transform.scale(
                    pygame.image.load(
                        resource_path("assets/main_character/main.png")
                    ),
                    self.config["size"],
                ),
                pygame.transform.scale(
                    pygame.image.load(
                        resource_path("assets/main_character/main_walk1.png")
                    ),
                    self.config["size"],
                ),
                pygame.transform.scale(
                    pygame.image.load(
                        resource_path("assets/main_character/main_walk2.png")
                    ),
                    self.config["size"],
                ),
                pygame.transform.scale(
                    pygame.image.load(
                        resource_path("assets/main_character/main_walk3.png")
                    ),
                    self.config["size"],
                ),
            ],
            "current_index": 0,
            "speed": ANIMATION_SPEED,
            "frame_counter": 0,
            "is_moving": False,
        }
        self.image = self.animation["sprites"][self.animation["current_index"]]
        self.facing_right = True

    def update(self):
        """
        Обновление состояния персонажа: анимация, направление и гравитация.
        Вызывается каждый кадр игры.
        """
        if self.animation["is_moving"]:
            self.animation["frame_counter"] += self.animation["speed"]
            if (
                    self.animation["frame_counter"]
                    >= len(self.animation["sprites"]) - 1
            ):
                self.animation["frame_counter"] = 0
            self.animation["current_index"] = (
                    int(self.animation["frame_counter"]) + 1
            )
        else:
            self.animation["current_index"] = 0
        self.image = self.animation["sprites"][self.animation["current_index"]]
        self.image = pygame.transform.flip(
            self.image, not self.facing_right, False
        )
        self.apply_gravity()
        self.regeneration()

    def move(self, keys: pygame.key.ScancodeWrapper, screen_width):
        """
        Управление движением персонажа на основе нажатых клавиш.
        """
        self.animation["is_moving"] = False
        if keys[pygame.K_d]:
            self.move_right(screen_width)
            self.facing_right = True
            self.animation["is_moving"] = True
        if keys[pygame.K_a]:
            self.move_left()
            self.facing_right = False
            self.animation["is_moving"] = True
        if keys[pygame.K_SPACE]:
            self.jump()

    def jump(self):
        """
        Выполнение прыжка персонажа, если он находится на земле.
        """
        if self.on_ground and self.base_stats['stamina']['now'] - JUMP_COST > 0:
            self.vertical_speed = self.config["jumping_speed"] * -1
            self.base_stats['stamina']['now'] -= JUMP_COST
            self.on_ground = False

    def run(self, screen: pygame.Surface, keys: pygame.key.ScancodeWrapper):
        """
        Основная функция для запуска логики персонажа.
        """
        self.move(keys, screen.get_width())
        self.update()
        screen.blit(self.image, self.rect)
