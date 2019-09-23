import pygame
from ImpresorTexto import *

class Escenario(object):

    def __init__(self, _screen):
        self.screen = _screen
        self.WHITE = 255, 255, 255
        self.size_window = pygame.display.get_surface().get_size()
        self.score = ImpresorTexto(self.screen, self.WHITE, 30)
        self.vida = ImpresorTexto(self.screen, self.WHITE, 30)
        self.msg_nivel = ImpresorTexto(self.screen, self.WHITE, 30)
        self.msg_gameover = ImpresorTexto(self.screen, self.WHITE, 80)

    def draw_margen(self):
        pygame.draw.line(self.screen, self.WHITE, [0, 30], [self.size_window[0], 30], 1)    
        pygame.draw.line(self.screen, self.WHITE, [0, 530], [self.size_window[0], 530], 1)

    def draw_text(self, puntaje, vidas, nivel):
        self.score.render("SCORE " + str(puntaje), (300, 10))
        self.vida.render("LIVES " + str(vidas), (550, 10))
        self.msg_nivel.render("NIVEL " + str(nivel), (50, 10))

    def draw_game_over(self):
        self.msg_gameover.render("GAME OVER", (200, 200))

