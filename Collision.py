
class Collision(object):

    def __init__(self, _error):
        self.error = _error

    def detect_colision(self, rect1, rect2):
        self.is_resolved = False
        if (rect1.rect.colliderect(rect2.rect)):
            if (not self.resolve_collision(rect1, rect2)):
                rect1.rect.y = rect2.rect.y - rect1.height
                print("COLISION NO RESUELTA")
                rect1.velocity.y *= -1
            return True
        return False

    def resolve_collision(self, rect1, rect2):
        is_resolved = False
        if (rect1.right_old - self.error < rect2.left):#collision left
            rect1.rect.x = rect2.rect.x - rect1.width
            rect1.velocity.x *= -1
            is_resolved = True
        if (rect1.left_old + self.error > rect2.right):#collision right
            rect1.rect.x = rect2.rect.x + rect2.width
            rect1.velocity.x *= -1
            is_resolved = True
        if (rect1.top_old + self.error > rect2.bottom):#collision bottom
            rect1.rect.y = rect2.rect.y + rect2.height
            rect1.velocity.y *= -1
            is_resolved = True
        if (rect1.bottom_old - self.error < rect2.top):#collsion top
            rect1.rect.y = rect2.rect.y - rect1.height
            rect1.velocity.y *= -1
            is_resolved = True
        return is_resolved
        