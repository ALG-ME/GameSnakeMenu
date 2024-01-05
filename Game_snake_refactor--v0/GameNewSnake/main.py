# Snake_game_main_project/main.py
from src.game.game import Game
import pygame
import sys


def main():
    pygame.init()

    screen_width = 800
    screen_height = 600

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake Game")

    game = Game(screen)
    game.run()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
