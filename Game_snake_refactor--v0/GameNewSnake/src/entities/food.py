
import pygame
import random


class Food:
    def __init__(self):
        self.size = 20
        self.rect = pygame.Rect(0, 0, self.size, self.size)
        self.spawn()

    def spawn(self):
        # Появление еды в случайном месте на экране
        x = random.randrange(0, 800, self.size)
        y = random.randrange(0, 600, self.size)
        self.rect.topleft = (x, y)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), self.rect)
