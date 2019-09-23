import pygame
import sys
import random
from Pelota import *
from Raqueta import *
from Collision import *
from Brick import * 
from Escenario import *
import selector_images as images

class Breakout():

    def __init__(self):
        self.WHITE = 225, 225, 225
        self.BLACK = 0, 0, 0
        self.clock = pygame.time.Clock()
        self.size_window = (700, 600)
        self.game_over = False
        self.salir = False
        self.soltar_pelota = False
        self.puntaje = 0
        self.nivel = 1
        self.vidas = 3
        self.SCREEN_WIDTH = self.size_window[0]
        self.SCREEN_HEIGHT = self.size_window[1]

    def load_game(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size_window)
        pygame.display.set_caption("breakout")
        self.escenario = Escenario(self.screen)
        self.collision = Collision(5)
        self.pelota = Pelota(self.screen, 16, 16, "sprites/pelota_white.png")
        self.pelota.set_velocity(2, 5)
        self.raquet = Raqueta(self.screen, 74, 12, "sprites/raquet_white.png")
        self.raquet.set_position(300, 550)
        self.bricks = self.load_bricks(12, self.nivel)
        self.tam_list = len(self.bricks)
        self.loop()

    def loop(self):
        dt = 0
        while (not self.salir):
            while (not self.game_over):
                self.ctrl_events()
                self.update(dt)
                self.render()
                self.clock.tick(60)
            self.ctrl_events()

    def reset_game(self):
        self.screen.fill(self.BLACK)
        self.clock.tick(1)
        self.game_over = False
        self.soltar_pelota = False
        self.puntaje = 0
        self.nivel = 1
        self.vidas = 3
        self.pelota.set_velocity(2, 5)
        self.raquet.set_position(300, 550)
        self.bricks = self.load_bricks(12, self.nivel)
            
    def aumentar_nivel(self):
        self.screen.fill(self.BLACK)
        self.clock.tick(1)
        self.soltar_pelota = False
        self.nivel += 1
        self.vidas = 3
        self.bricks = self.load_bricks(12, self.nivel)
        self.tam_list = len(self.bricks)
        self.pelota.set_velocity(2 + self.nivel, 5 + self.nivel)
        self.raquet.set_velocity(self.nivel)
        
    def update(self, delta):
        self.pelota.update()
        if (self.soltar_pelota):
            self.collision.detect_colision(self.pelota, self.raquet)
            self.pelota.move()
        else:
            self.center_pelota()
            self.pelota.pelota_perdida = False         
        self.raquet.update()
        for b in self.bricks:
            if (self.collision.detect_colision(self.pelota, b)):
                b.sub_resist()
                self.puntaje += 10
                if (b.cant_resist == 0):
                    self.bricks.remove(b)
                    self.tam_list -= 1
            b.update()
        if (self.tam_list == 0):
            self.aumentar_nivel()
        if (self.pelota.pelota_perdida):
            self.vidas -= 1
            if (self.vidas == 0):
                self.game_over = True
                self.bricks.clear()
            else:
                self.soltar_pelota = False
                
    def render(self):
        self.screen.fill(self.BLACK)
        if (not self.game_over):
            self.pelota.draw()
            self.raquet.draw()
            for b in self.bricks:
                b.draw()
        else:
            self.escenario.draw_game_over()
        self.escenario.draw_margen()
        self.escenario.draw_text(self.puntaje, self.vidas, self.nivel)
        pygame.display.flip()

    def center_pelota(self):
        posX = self.raquet.rect.x + (self.raquet.width/2) - (self.pelota.width/2)
        posY = self.raquet.rect.y - self.pelota.height
        self.pelota.set_position(posX, posY)

    def ctrl_events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit(1)
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_RIGHT]):
            self.raquet.move_to_rigth()
        elif (keys[pygame.K_LEFT]):
            self.raquet.move_to_left()
        if (keys[pygame.K_SPACE]):
            self.soltar_pelota = True
        if (keys[pygame.K_r]):
            self.reset_game()
    
    def load_bricks(self, rows, cols):
        list_bricks = []
        c = 0
        while (c < cols):
            r = 0
            while (r < rows):
                path = images.select_image()
                brick = Brick(self.screen, 50, 30, path)
                brick.set_position((r + 1) * 52, (c + 1) * 32)
                list_bricks.append(brick)
                r += 1
            c += 1
        return list_bricks

if (__name__ == "__main__"):
    p = Breakout()
    p.load_game()