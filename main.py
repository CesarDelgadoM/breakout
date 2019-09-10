import pygame
import sys
from Rect import *
import cmath
import random

class ColisionesRect():

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.start_game()
        self.WHITE = 255, 255, 255
        self.GREEN = 0, 255, 0
        self.BLUE = 0, 0, 255
        self.BLACK = 0, 0, 0
        self.RED = 255, 0, 0
        self.wind_size = (600, 600)
        self.WIN_WIDTH = self.wind_size[0]
        self.WIN_HEIGHT = self.wind_size[1]
        self.window = pygame.display.set_mode(self.wind_size, 0, 0, 0)
        self.rect = Rect(self.window, 50, 50, self.BLACK)
        self.rect_static = Rect(self.window, 70, 70, self.GREEN)
        self.rect_static.set_position((self.WIN_WIDTH/2), (self.WIN_HEIGHT/2))
        self.rect_static_2 = Rect(self.window, 70, 70, self.BLUE)
        self.rect_static_2.set_position(self.rect_static.vectPos.x, self.rect_static.vectPos.y - self.rect_static.height)
        self.loop()

    def cargar_rect(self):
        width = random.randint(20, 70)
        height = random.randint(20, 70)
        pos_mouse = pygame.mouse.get_pos()
        posX = pos_mouse[0]#random.randint(0, self.WIN_WIDTH - width)
        posY = pos_mouse[1]#random.randint(0, self.WIN_HEIGHT - height)
        rect = Rect(self.window, width, height, self.BLACK)
        rect.set_position(posX, posY)
        self.list_rect.append(rect)
    
    def start_game(self):
        self.list_rect = []
        self.game_over = False
        self.colision_x = False
        self.colision_y = False
        self.gravity = pygame.Vector2(5, 5)
        self.clic = True
    
    def loop(self):
        self.dt = 0
        while(not self.game_over):
            self.ctrl_events()
            self.update(self.dt)
            self.render()
            self.dt = self.clock.tick(60) / 1000.0
            
    def update(self, dt):
        i = 0
        tam_list = len(self.list_rect)
        while (i <= tam_list - 1):
            if (tam_list > 1):
                j = i + 1
                while (j  <= tam_list - 1):
                    self.detect_colision(self.list_rect[i], self.list_rect[j])
                    self.detect_colision(self.list_rect[j], self.list_rect[i])
                    j += 1
            i += 1
        for rect in self.list_rect:
            rect.velocity += self.gravity
            #rect.desacelerar(rect.friction)
            rect.update(dt)
    
    def render(self):
        self.window.fill(self.WHITE)
        for rect in self.list_rect:
            rect.draw()
        pygame.display.flip()
    
    def ctrl_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        mouse = pygame.mouse.get_pressed()
        if (mouse[0] and self.clic):
            self.clic = False
            self.cargar_rect()
        elif (not mouse[0] and not self.clic):
            self.clic = True

    def detect_colision(self, rect1, rect2):
        if (self.AABB_vs_AABB(rect1, rect2)):
            #print("colision!", rect1)
            rect1.set_color(self.RED)
            self.resolve_collision(rect1, rect2)
            return True
        else:
            rect1.set_color(rect1.color_origin)
            return False

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
        if (rect1.right_old < rect2.left):#collision left
            rect1.velocity.x *= -1
            rect1.vectPos.x = rect2.left - rect1.width - 1
            #rect1.velocity.x = 0
        if (rect1.left_old > rect2.right):#collision right
            rect1.velocity.x *= -1
            rect1.vectPos.x = rect2.right + 1
            #rect1.velocity.x = 0
        if (rect1.top_old > rect2.bottom):#collision bottom
            rect1.velocity.y *= -1
            rect1.vectPos.y = rect2.bottom + 1
            #rect1.velocity.y = 0
        if (rect1.bottom_old < rect2.top):#collsion top
            rect1.velocity.y *= -1
            rect1.vectPos.y = rect2.top - rect1.height - 1
            #rect1.velocity.y = 0

if __name__ == "__main__":
    play = ColisionesRect()