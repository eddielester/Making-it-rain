from Sprite import Sprite

class ScreenSaverBot(Sprite):
    
    speedX = 8
    speedY = 8
    diameter = 30
    c = color(200,200,255)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.y += self.speedY
        self.x += self.speedX
        if self.y < 0 or self.y > height:
            self.speedY *= -1
        if self.x < 0 or self.x > width:
            self.speedX *= -1
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
