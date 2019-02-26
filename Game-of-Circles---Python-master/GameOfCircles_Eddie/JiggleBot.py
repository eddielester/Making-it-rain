

class JiggleBot:
    
    speed = 4
    diameter = 30
    c = color(150, 100, 255)
        
    def move(self):
        self.y += random(-self.speed, self.speed)
        self.x += random(-self.speed, self.speed)
        self.x = constrain(self.x, 0, width)
        self.y = constrain(self.y, 0, height)
