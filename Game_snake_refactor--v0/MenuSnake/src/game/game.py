# game.py
import pygame
import sys
from ..entities.snake import Snake
from ..entities.food import Food

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.snake = Snake()
        self.food = Food()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        self.snake.move()
        if self.snake.check_collision(self.food.rect):
            self.food.spawn()
            self.snake.grow()

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)  # Ограничение частоты кадров
