# game/menu.py

import pygame
import sys
from ..entities import Button

class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font("./assets/fonts/segoe-ui-semibold-2.ttf", 36)

        self.buttons = [
            Button("Новая игра", (50, 150), (250, 50), self.start_game),
            Button("Сложность", (50, 220), (250, 50), self.set_difficulty),
            Button("Рекорд", (50, 290), (250, 50), self.show_records),
            Button("Выход из игры", (50, 360), (250, 50), sys.exit),
            Button("Музыка: Play", (50, 430), (250, 50), self.toggle_music),
        ]

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in self.buttons:
                    if button.rect.collidepoint(event.pos):
                        button.perform_action()

    def update(self):
        pass  # Возможные обновления меню

    def draw(self):
        self.screen.fill((255, 255, 255))

        for button in self.buttons:
            button.draw(self.screen, self.font)

        pygame.display.flip()

    def run(self):
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(30)

    def start_game(self):
        print("Начать новую игру")

    def set_difficulty(self):
        print("Настройка сложности")

    def show_records(self):
        print("Показать рекорды")

    def toggle_music(self):
        print("Переключить музыку")
