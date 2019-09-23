import pygame
from DirectionRect import *

class Brick(DirectionRect):

    def __init__(self, _screen, _width, _height, _path):
        self.screen = _screen
        self.size_window = pygame.display.get_surface().get_size()
        self.width = _width
        self.height = _height
        self.load_image(_path)
        self.cant_resist = 1
        self.rect = self.image.get_rect()
        DirectionRect.__init__(self, self.rect, self.width, self.height)

    def load_image(self, path):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect = self.update_directions(self.rect)

    def set_position(self, posX, posY):
        self.rect.x = posX
        self.rect.y = posY

    def sub_resist(self):
        self.cant_resist -= 1

    def set_resistencia(self, resist):
        self.cant_resist = resist