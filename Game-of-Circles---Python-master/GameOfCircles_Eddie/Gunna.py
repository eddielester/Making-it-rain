from Sprite import Sprite
from Bullet import Bullet

import SpriteManager

class Gunna(Sprite):
    
    speed = 5
    diameter = 30
    c = color(0,0,255)
    
    mark = 0
    wait = 1000
    go = False
    
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
        
        
        
    def aim(self, target):
        global go, mark, wait
        xComp = target.x - self.x
        yComp = target.y - self.y
        d = ((self.x - target.x)**2 + (self.y  - target.y)**2)**.5
        xVector = xComp / 2 *.035
        yVector = yComp / 2 *.035
        return PVector(xVector, yVector)
        return PVector(0, 10)
    
        
    
    def fire(self, vector):
        global go, mark, wait
        
        if(millis() - self.mark > self.wait):
            self.go = not self.go
            self.mark = millis()
            
        if(self.go):
            self.go = False
            SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
        
    
        
        
    
