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
        self.rect_size = 20
        self.rect_count = 28
        self.rect_color = (122, 122, 122)
        self.rect_color_other = (111, 132, 122)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction_to('UP')
                if event.key == pygame.K_DOWN:
                    self.snake.change_direction_to('DOWN')
                if event.key == pygame.K_LEFT:
                    self.snake.change_direction_to('LEFT')
                if event.key == pygame.K_RIGHT:
                    self.snake.change_direction_to('RIGHT')

    def update(self):
        self.snake.move()
        if self.snake.check_collision(self.food.rect):
            self.food.spawn()
            self.snake.grow()

    def draw(self):
        # def draw_rect(color, row, column):
        #     pygame.draw.rect(self.screen, color, [20 + column * self.rect_size, 20 + row * self.rect_size, self.rect_size, self.rect_size])

        for row in range(self.rect_count):
            for column in range(self.rect_count):
                if (row + column) % 2 == 0:
                    color = self.rect_color
                else:
                    color = self.rect_color_other
                # draw_rect(color, row, column)
                pygame.draw.rect(self.screen, color, [20 + column * self.rect_size, 20 + row * self.rect_size, self.rect_size, self.rect_size])
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(30)  # Ограничение частоты кадров
