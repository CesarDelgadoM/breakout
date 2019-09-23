import pygame
from DirectionRect import *

class Raqueta(DirectionRect):

    def __init__(self, _screen, _weidth, _height, _path):
        self.screen = _screen
        self.size_window = pygame.display.get_surface().get_size()
        self.width = _weidth
        self.height = _height
        self.load_image(_path)
        self.rect = self.raquet.get_rect()
        self.velocity = pygame.Vector2(8, 0)
        DirectionRect.__init__(self, self.rect, self.width, self.height)

    def load_image(self, path):
        pygame.sprite.Sprite.__init__(self)
        self.raquet = pygame.image.load(path)

    def draw(self):
        self.screen.blit(self.raquet, self.rect)

    def update(self):
        self.rect = self.update_directions(self.rect)
        self.limit_window()
    
    def set_position(self, posX, posY):
        self.rect.x = posX
        self.rect.y = posY

    def set_velocity(self, velX):
        self.velocity.x += velX

    def move_to_left(self):
        self.rect.x -= self.velocity.x
    
    def move_to_rigth(self):
        self.rect.x += self.velocity.x

    def limit_window(self):
        if (self.rect.x <= 0):
            self.rect.x = 0
        if (self.rect.x + self.width >= self.size_window[0]):
            self.rect.x = self.size_window[0] - self.width

