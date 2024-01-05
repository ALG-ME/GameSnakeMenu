import pygame

class Button:
    def __init__(self, text, position, size, action=None):
        self.text = text
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position, size)
        self.action = action

    def draw(self, screen, font, color=(255, 255, 255), highlight_color=(200, 200, 200)):
        pygame.draw.rect(screen, highlight_color if self.rect.collidepoint(pygame.mouse.get_pos()) else color, self.rect)
        text_surface = font.render(self.text, True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def perform_action(self):
        if self.action:
            self.action()

