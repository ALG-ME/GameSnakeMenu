
import pygame

class Snake:
    def __init__(self):
        self.size = 20
        self.body = [(100, 100)]  # Начальная позиция змейки

    def move(self):
        pass
    # Логика движения змейки (пока оставим пустой)

    def draw(self, screen):
        for segment in self.body:
            pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(segment[0], segment[1], self.size, self.size))

    def check_collision(self, rect):
        pass
    # Проверка столкновения с другим объектом (пока оставим пустой)

    def grow(self):
        pass
    # Увеличение размера змейки при поедании еды (пока оставим пустой)

    def check_boundary_collision(self, screen_width, screen_height):
        pass
# Проверка столкновения с границами экрана (пока оставим пустой)

