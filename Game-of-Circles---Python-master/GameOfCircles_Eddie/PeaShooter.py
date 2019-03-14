import SpriteManager

class PeaShooter:
    wait = 1000
    mark = 0
    
    def __init__ (self, handler):
        self.handler = handler
        
    def shoot(self, vector)
    if (millis() - self.mark > self.wait):
        pea = (Bullet(self.handler.x, self.handler.y, vector, self.handler.team)
               SpriteManager.spawn(pea)
