from Sprite import Sprite
from Bullet import Bullet

import SpriteManager

mark = 0
wait = 1000
go = True

class Gunna(Sprite):
    
    speed = 8
    diameter = 30
    #c = color(0,0,255)
    global go, mark, wait
    
    if(millis() - mark > wait):
        go = not go
        mark = millis()
            
    if(go):
        fill(255, 0, 0)
    else:
        fill(0, 0, 255)
    
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
        vector = self.aim(SpriteManager.getPlayer())
        self.fire(vector)
        
        
    def aim(self, target):
        xComp = target.x - self.x
        yComp = target.y - self.y
        d = ((self.x - target.x)**2 + (self.y  - target.y)**2)**.5
        xVector = xComp / 2
        yVector = yComp / 2
        return PVector(xVector, yVector)
        return PVector(0, 10)
    
        
    
    def fire(self, vector):
        global go, mark, wait
        SpriteManager.spawn(Bullet(self.x, self.y, vector, self.team))
    
        
    
        
        
    
