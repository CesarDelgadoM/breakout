import pygame

class ImpresorTexto():

    def __init__(self, _window, _color, tam_font):
        self.window = _window
        self.color = _color
        self.font = pygame.font.Font(None, tam_font)
    
    def render(self, mensaje, position):
        self.text = self.font.render(mensaje, 0, self.color)
        self.window.blit(self.text, position)