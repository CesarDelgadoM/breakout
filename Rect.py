import pygame

class Rect():

    def __init__(self, _window, _width, _height, _color):
        self.window = _window
        self.size_win = pygame.display.get_surface().get_size()
        self.width = _width
        self.height = _height
        self.color = _color
        self.vectPos = pygame.Vector2(0, 0)
        self.normal = pygame.Vector2(0, 0)
        self.penetration = 1
        self.min = pygame.Vector2(self.vectPos.x, self.vectPos.y + self.height)
        self.max = pygame.Vector2(self.vectPos.x + self.width, self.vectPos.y )
        self.rect = pygame.Rect((self.vectPos.x, self.vectPos.y), (self.width, self.height))
        self.in_floor = False
    
    def __update_rect(self):
        self.min = pygame.Vector2(self.vectPos.x, self.vectPos.y + self.height)
        self.max = pygame.Vector2(self.vectPos.x + self.width, self.vectPos.y )
        self.rect = pygame.Rect((self.vectPos.x, self.vectPos.y), (self.width, self.height))

    def detect_limit_window(self):
        if (self.vectPos.x < 0):
            self.vectPos.x = 0
        elif (self.vectPos.x + self.width > self.size_win[0]):
            self.vectPos.x = self.size_win[0] - self.width
        elif (self.vectPos.y < 0):
            self.vectPos.y = 0
        elif (self.vectPos.y + self.height > self.size_win[1]):
            self.vectPos.y = self.size_win[1] - self.height
            self.in_floor = True
        self.__update_rect()

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)

    def accelerate(self, velocity):
        self.vectPos += velocity
        self.detect_limit_window()

    def set_position(self, _posX, _posY):
        self.vectPos.x = _posX
        self.vectPos.y = _posY
        self.detect_limit_window()

    def set_color(self, _color):
        self.color = _color

    def get_AABB(self):
        return 

    def get_rect(self):
        return self.rect