import pygame

# Инициализируем
pygame.init()
#

# Ширина Высота
# Цвета
FRAME_COLOR = (59, 59, 59)

RECT_COLOR = (110, 168, 160)
RECT_SIZE = 20
COUNT_RECTS = 20
OTHER_RECT_COLOR = (110, 160, 155)
GAP = 1

SCREEN_WIDTH = RECT_SIZE * COUNT_RECTS + 2 * RECT_SIZE + GAP * RECT_SIZE
SCREEN_HEIGHT = 700
HEADER_RECT = 70
HEADER_COLOR = (147, 176, 173)

# Создаём окно
app = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Название
pygame.display.set_caption('A game written in Python using Pygame')
#


game_over = True

while game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = False

    app.fill(FRAME_COLOR)

    pygame.draw.rect(app, HEADER_COLOR, [0, 0, SCREEN_WIDTH, HEADER_RECT])


    for row in range(COUNT_RECTS):
        for column in range(COUNT_RECTS):
            color = RECT_COLOR
            if (row + column) % 2 == 0:
                pygame.draw.rect(app, color, [RECT_SIZE + column * RECT_SIZE + GAP * (column + 1),
                                              HEADER_RECT + row * RECT_SIZE + GAP * (row + 1), RECT_SIZE, RECT_SIZE], )
            else:
                color = OTHER_RECT_COLOR
                pygame.draw.rect(app, color, [RECT_SIZE + column * RECT_SIZE + GAP * (column + 1),
                                              HEADER_RECT + row * RECT_SIZE + GAP * (row + 1), RECT_SIZE, RECT_SIZE], )

    pygame.display.update()



