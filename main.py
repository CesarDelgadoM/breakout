import pygame
import sys
from Rect import *
import cmath

class ColisionesRect():

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.start_game()
        self.WHITE = 255, 255, 255
        self.BLACK = 0, 0, 0
        self.RED = 255, 0, 0
        self.wind_size = (600, 600)
        self.WIN_WIDTH = self.wind_size[0]
        self.WIN_HEIGHT = self.wind_size[1]
        self.window = pygame.display.set_mode(self.wind_size, 0, 0, 0)
        self.rect = Rect(self.window, 50, 50, self.WHITE)
        self.rect_static = Rect(self.window, 70, 70, self.WHITE)
        self.rect_static.set_position((self.WIN_WIDTH/2), (self.WIN_HEIGHT/2))
        self.loop()
    
    def start_game(self):
        self.game_over = False
        self.vel = 5
        self.colision_x = False
        self.colision_y = False
    
    def loop(self):
        self.dt = 0
        self.clock.tick(60)
        while(not self.game_over):
            self.ctrl_events()
            self.update(self.dt)
            self.render()
            self.dt = self.clock.tick(60) / 1000.0
            
    def update(self, dt):
        self.rect.update(dt) 
        self.rect_static.update(dt)
        self.detect_colision(self.rect, self.rect_static)
    
    def render(self):
        self.window.fill(self.BLACK)
        self.rect.draw()
        self.rect_static.draw()
        pygame.display.flip()
    
    def ctrl_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP]):
            self.rect.velocity.y -= self.vel
        if (keys[pygame.K_DOWN]):
            self.rect.velocity.y += self.vel
        if (keys[pygame.K_RIGHT]):
            self.rect.velocity.x += self.vel
        if (keys[pygame.K_LEFT]):
            self.rect.velocity.x -= self.vel
        self.rect.desacelerar(self.rect.friction)

    def detect_colision(self, rect1, rect2):
        if (self.AABB_vs_AABB(rect1, rect2)):
            rect2.set_color(self.RED)
            self.resolve_collision(rect1, rect2)
        else:
            rect2.set_color(self.WHITE)

    def AABB_vs_AABB(self, rect1, rect2):
        if (rect1.vectPos.x + rect1.width >= rect2.vectPos.x and
            rect2.vectPos.x + rect2.width >= rect1.vectPos.x):
            self.colision_x = True
        else:
            self.colision_x = False
        if (rect1.vectPos.y + rect1.height >= rect2.vectPos.y and
            rect2.vectPos.y + rect2.height >= rect1.vectPos.y):
            self.colision_y = True
        else:
            self.colision_x = False
        return self.colision_x and self.colision_y
    
    def resolve_collision(self, rect1, rect2):
        pass
        

if __name__ == "__main__":
    play = ColisionesRect()