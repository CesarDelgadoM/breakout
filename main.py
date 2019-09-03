import pygame
import sys
from Rect import *
import cmath

class ColisionesRect():

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.start_game()
        self.gravity = pygame.Vector2(0, 9.86)
        self.WHITE = 255, 255, 255
        self.BLACK = 0, 0, 0
        self.RED = 255, 0, 0
        self.wind_size = (500, 500)
        self.WIN_WIDTH = self.wind_size[0]
        self.WIN_HEIGHT = self.wind_size[1]
        self.window = pygame.display.set_mode(self.wind_size, 0, 0, 0)
        self.rect = Rect(self.window, 50, 50, self.WHITE)
        self.rect_static = Rect(self.window, 70, 70, self.WHITE)
        self.rect_static.set_position((self.WIN_WIDTH/2), (self.WIN_HEIGHT/2))
        self.loop()
    
    def start_game(self):
        self.game_over = False
        self.mouse_in = False
        self.velocity = pygame.Vector2(0, 0)
    
    def loop(self):
        self.dt = 0
        self.clock.tick(60)
        while(not self.game_over):
            self.ctrl_events()
            self.update(self.dt)
            self.render()
            self.dt = self.clock.tick(60) / 1000.0
            
    def update(self, dt):
        if (self.mouse_in):
            coords_mouse = pygame.mouse.get_pos()
            centerW = self.rect.width/2
            centerH = self.rect.height/2
            self.rect.set_position(coords_mouse[0] - centerW, coords_mouse[1] - centerH)
            self.rect.in_floor = False
        else:
             self.velocity += self.gravity * dt
             self.rect.accelerate(self.velocity)
        if (self.rect.in_floor):
            self.velocity.y = 0
            self.activar_gravity(False)
        else:
            self.activar_gravity(True)
        self.collision_AABB(self.rect, self.rect_static)
    
    def render(self):
        self.window.fill(self.BLACK)
        self.rect.draw()
        self.rect_static.draw()
        pygame.display.flip()
    
    def ctrl_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        mouse = pygame.mouse.get_pressed()
        if (mouse[0]):
            coords_mouse = pygame.mouse.get_pos()
            if (self.rect.get_rect().collidepoint(coords_mouse)):
                self.mouse_in = True
        else:
            self.mouse_in = False

    def collision_AABB(self, rect1, rect2):
        if (rect1.get_rect().colliderect(rect2.get_rect())):
            rect2.set_color(self.RED)
            #detectar y corregir la colision entre los rectangulos
            self.AABB_vs_AABB(rect1, rect2)
        else:
            rect2.set_color(self.WHITE)

    def AABB_vs_AABB(self, rect1, rect2):
        if (rect1.vectPos.y + rect1.height > rect2.vectPos.y and rect1.vectPos.y > 0):
            rect1.vectPos.y = rect2.vectPos.y - rect1.height
            self.rect.in_floor = True
        elif (rect1.vectPos.x < rect2.vectPos.x + rect2.width and rect1.vectPos.x < 0):
            rect1.vectPos.x = rect2.vectPos.x + rect2.width
            

    def activar_gravity(self, active):
        if (active):
            self.gravity.y = 9.86
        else:
            self.gravity.y = 0

if __name__ == "__main__":
    play = ColisionesRect()