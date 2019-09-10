import pygame

class Rect(object):

    def __init__(self, _window, _width, _height, _color):
        self.window = _window
        self.size_win = pygame.display.get_surface().get_size()
        self.width = _width
        self.height = _height
        self.color = _color
        self.friction = 0.98
        self.vectPos = pygame.Vector2(0, 0)
        self.velocity = pygame.Vector2(0, 0)
        self.rect = pygame.Rect((self.vectPos.x, self.vectPos.y), (self.width, self.height))
        self.update_directions()
        self.save_directions_old()
        self.save_color()
    
    def update(self, dt):
        self.save_directions_old()
        self.accelerate(dt)
        self.update_directions()
        self.detect_limit_window()
        self.rect = pygame.Rect((self.vectPos.x, self.vectPos.y), (self.width, self.height))
    
    def update_directions(self):
        self.left = self.vectPos.x
        self.right = self.vectPos.x + self.width
        self.top = self.vectPos.y
        self.bottom = self.vectPos.y + self.height
        self.center = pygame.Vector2(((self.vectPos.x + self.width)/2), ((self.vectPos.y + self.height)/2))
    
    def save_directions_old(self):
        self.left_old = self.left
        self.right_old = self.right
        self.top_old = self.top
        self.bottom_old = self.bottom

    def detect_limit_window(self):
        if (self.vectPos.x < 0):
            self.vectPos.x = 0
            self.velocity.x *= -1
        if (self.vectPos.x + self.width > self.size_win[0]):
            self.vectPos.x = self.size_win[0] - self.width
            self.velocity.x *= -1
        if (self.vectPos.y < 0):
            self.vectPos.y = 0
            self.velocity.y *= -1
        if (self.vectPos.y + self.height > self.size_win[1]):
            self.vectPos.y = self.size_win[1] - self.height
            self.velocity.y *= -1
        #self.desacelerar(self.friction)

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    def accelerate(self, dt):
        self.vectPos += self.velocity * dt

    def desacelerar(self, friction):
        if (self.velocity.x != 0):
            if (self.velocity.x > 0):
                self.velocity.x -= friction
            else:
                self.velocity.x += friction
        if (self.velocity.y != 0):                
            if (self.velocity.y > 0):
                self.velocity.y -= friction
            else:
                self.velocity.y += friction
        
    def set_position(self, _posX, _posY):
        self.vectPos.x = _posX
        self.vectPos.y = _posY

    def set_color(self, _color):
        self.color = _color

    def save_color(self):
        self.color_origin = self.color

    def get_rect(self):
        return self.rect