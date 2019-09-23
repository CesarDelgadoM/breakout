
class DirectionRect(object):

    def __init__(self, _rect, _width, _height):
        self.rect = _rect
        self.width = _width
        self.height = _height
        self.left = self.rect.x
        self.right = self.rect.x + self.width
        self.top = self.rect.y
        self.bottom = self.rect.y + self.height

    def update_directions(self, _rect):
        self.rect = _rect
        self.__save()
        self.__update()
        return self.rect

    def __update(self):
        self.left = self.rect.x
        self.right = self.rect.x + self.width
        self.top = self.rect.y
        self.bottom = self.rect.y + self.height
    
    def __save(self):
        self.left_old = self.left
        self.right_old = self.right
        self.top_old = self.top
        self.bottom_old = self.bottom   