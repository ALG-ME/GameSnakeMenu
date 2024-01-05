import pygame
import sys
from menu_button import ImageButton

# Инициализируем
pygame.init()

#Параметры окна
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600

RECT_LINE_WIDTH = SCREEN_WIDTH - 350
RECT_LINE_COLOR = (149, 124, 124)

#ФПС
FPS = 60
FramePerSecond = pygame.time.Clock()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Game menu')

#Кнопки
# PLAY
Button_Play = ImageButton(
    (SCREEN_WIDTH - 350)/2 - (200/2),
    (SCREEN_HEIGHT / 2 - (50/2)) - 60,
    200,
    50,
    'PLAY',
    './Public/Button_default.png',
    './Public/Button_focus.png',
    '')

Button_Rate = ImageButton(
    (SCREEN_WIDTH - 350)/2 - (200/2),
    (SCREEN_HEIGHT / 2 - (50/2)),
    200,
    50,
    'RATE',
    './Public/Button_default.png',
    './Public/Button_focus.png',
    '')

Button_Last_Score = ImageButton(
    (SCREEN_WIDTH - 350)/2 - (200/2),
    (SCREEN_HEIGHT / 2 - (50/2))+60,
    200,
    50,
    'LAST SCORE',
    './Public/Button_default.png',
    './Public/Button_focus.png',
    '')




def main_menu():
    game_over = True

    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False

            for btn in [Button_Play, Button_Rate, Button_Last_Score]:
                btn.handle_event(event)

            if event.type == pygame.USEREVENT and event.button == Button_Rate:
                print('Нажата сложность')
                difficult_menu()
                pygame.quit()


        font = pygame.font.Font(None, 72)
        text_surface = font.render('shhhhhh snake', True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=((SCREEN_WIDTH - 350)/2, 100))
        SCREEN.blit(text_surface, text_rect)

        #Полоска между меню и таблицей подсчёта
        pygame.draw.rect(SCREEN, RECT_LINE_COLOR, (RECT_LINE_WIDTH, 50, 2,
                                                   SCREEN_HEIGHT - 100))

        # Отрисовка кнопок
        check = pygame.mouse.get_pos()

        for btn in [Button_Play, Button_Rate, Button_Last_Score]:
            # btn.check_hover(check)
            btn.draw(SCREEN, check)
        pygame.display.flip()

def difficult_menu():
    game_over = True


    while game_over:
        SCREEN.fill((0,0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            for btn2 in [Button_Easy, Button_Hard, Button_Insane, Button_Back]:
                btn2.handle_event(event)
        Button_Easy = ImageButton(
            SCREEN_WIDTH / 2 - (200 / 2),
            (SCREEN_HEIGHT / 2 - (50 / 2)) - 60,
            200,
            50,
            'EASY',
            './Public/Button_default.png',
            './Public/Button_focus.png',
            '')

        Button_Hard = ImageButton(
            SCREEN_WIDTH / 2 - (200 / 2),
            (SCREEN_HEIGHT / 2 - (50 / 2)),
            200,
            50,
            'HARD',
            './Public/Button_default.png',
            './Public/Button_focus.png',
            '')

        Button_Insane = ImageButton(
            SCREEN_WIDTH / 2 - (200 / 2),
            (SCREEN_HEIGHT / 2 - (50 / 2)) + 60,
            200,
            50,
            'INSANE',
            './Public/Button_default.png',
            './Public/Button_focus.png',
            '')

        Button_Back = ImageButton(
            SCREEN_WIDTH / 2 - (200 / 2),
            (SCREEN_HEIGHT / 2 - (50 / 2)) + 130,
            200,
            50,
            'BACK',
            './Public/Button_default.png',
            './Public/Button_focus.png',
            '')


        for btn2 in [Button_Easy, Button_Hard, Button_Insane, Button_Back]:
            btn2.draw(SCREEN, pygame.mouse.get_pos())

        pygame.display.flip()

main_menu()


