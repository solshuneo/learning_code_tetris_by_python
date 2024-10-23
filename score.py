import pygame
from settings import *
from os.path import join
class Score:
    def __init__(self) -> None:
        self.surface = pygame.Surface(SCORE_SIZE)
        self.surface.fill(BACKGROUND_COLOR)
        self.screen = pygame.display.get_surface()

        self.font = pygame.font.Font(join('', '', 'Russo_One.ttf'), 30)
        self.increment_height = self.surface.get_height() / 3

        self.score = 0
        self.level = 1
        self.lines = 0

    def display_text(self, pos, text):
        text_surface = self.font.render(f'{text[0]} :{text[1]}', True, 'white')
        text_rext = text_surface.get_rect(center = pos)
        self.surface.blit(text_surface, text_rext)

    def run(self) -> None:
        self.surface.fill(BACKGROUND_COLOR)
        for i, text in enumerate([('Score', self.score), ('Level', self.level), ('Lines', self.lines)]):
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            self.display_text((x, y), text)
        self.screen.blit(self.surface, (PADDING + GAME_SIZE.x + PADDING, PADDING + PREVIEW_SIZE.y + PADDING))

