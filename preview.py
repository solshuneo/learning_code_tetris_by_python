import pygame
from settings import *
from pygame.image import load
from os import path
import os
class Preview:
    def __init__(self, ) -> None:
        self.surface = pygame.Surface(PREVIEW_SIZE)
        self.surface.fill(SILVER)
        self.rect = self.surface.get_rect(topright = (WINDOW_SIZE.x - PADDING, PADDING))
        self.screen = pygame.display.get_surface()

        self.shape_surfaces = {shape : pygame.image.load(path.join('.', 'graphics', f'{shape}.png')).convert_alpha() for shape in TETROMINOS.keys() }
        # print(self.shape_surfaces)
        #print(os.getcwd())

        self.increment_height = self.surface.get_height() / 3

    def display_pieces(self, next_shape):
        for i, shape in enumerate(next_shape):
            shape_surface = self.shape_surfaces[shape]
            x = self.surface.get_width() / 2
            y = self.increment_height / 2 + i * self.increment_height
            rect = shape_surface.get_rect(center = (x, y))
            self.surface.blit(shape_surface, rect)

    def run(self, next_shape) -> None:
        self.surface.fill(BACKGROUND_COLOR)
        self.display_pieces(next_shape)
        self.screen.blit(self.surface, (2 * PADDING + GAME_SIZE.x, PADDING))
        pygame.draw.rect(self.screen, LINE_COLOR, self.rect, 2, 2)

