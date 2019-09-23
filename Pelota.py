import pygame
from DirectionRect import *

class Pelota(DirectionRect):

    def __init__(self, _screen, _width, _height, _path):
        self.screen = _screen
        self.size_window = pygame.display.get_surface().get_size()
        self.width = _width
        self.height = _height
        self.pelota_perdida = False
        self.velocity = pygame.Vector2(0, 0)
        self.load_image(_path)
        self.rect = self.pelota.get_rect()
        DirectionRect.__init__(self, self.rect, self.width, self.height)
        
    def load_image(self, path):
        pygame.sprite.Sprite.__init__(self)
        self.pelota = pygame.image.load(path)
        
    def draw(self):
        self.screen.blit(self.pelota, self.rect)

    def update(self):
        self.rect = self.update_directions(self.rect)
        self.limits_window()

    def set_velocity(self, velX, velY):
        self.velocity.x = velX
        self.velocity.y = velY
    
    def move(self):
        self.rect.x += self.velocity.x
        self.rect.y += self.velocity.y

    def set_position(self, posX, posY):
        self.rect.x = posX
        self.rect.y = posY

    def limits_window(self):
        if (self.rect.x + self.width >= self.size_window[0]):
            self.rect.x = self.size_window[0] - self.width
            self.velocity.x *= -1
        if (self.rect.x <= 0):
            self.rect.x = 0
            self.velocity.x *= -1
        if (self.rect.y <= 30):#ojo (limite de la linea superior)
            self.rect.y = 30
            self.velocity.y *= -1
        if (self.rect.y >= self.size_window[1] + self.height + 100):
            self.velocity.y *= -1
            self.pelota_perdida = False;


