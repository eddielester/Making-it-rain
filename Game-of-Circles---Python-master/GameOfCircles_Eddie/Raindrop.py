from Sprite import Sprite
import SpriteManager

class Raindrop(Sprite):
    
    speed = 5
    diameter = 30
    c = color(0,0,255)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.y += self.speed
        if self.y < 0:
            self.y *= -0.5
        if self.y > height:
            self.y = 0
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
