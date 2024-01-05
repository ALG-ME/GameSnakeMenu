
import pygame

class Snake:
    def __init__(self):
        self.position = [100, 50]
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "DOWN"
        self.change_direction = self.direction
        self.size = 20
        self.body = [(100, 100)]  # Начальная позиция змейки

    def change_direction_to(self, dir):
        if dir == "RIGHT" and not(self.direction == "LEFT" or (self.direction == "LEFT" and
                                                           self.direction == "UP" or
                                                           self.direction == "LEFT" and
                                                           self.direction == "DOWN")):
            self.direction = "RIGHT"
        if dir=="LEFT" and not self.direction=="RIGHT":
            self.direction = "LEFT"
        if dir=="UP" and not self.direction=="DOWN":
            self.direction = "UP"
        if dir=="DOWN" and not self.direction=="UP":
            self.direction = "DOWN"

    def move(self):
        if self.direction == "RIGHT":
            self.position[0] += 20
        if self.direction == "LEFT":
            self.position[0] -= 20
        if self.direction == "UP":
            self.position[1] -= 20
        if self.direction == "DOWN":
            self.position[1] += 20
        self.body.insert(0, list(self.position))
        # if self.position != food_position:
        #     self.body.pop()


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

