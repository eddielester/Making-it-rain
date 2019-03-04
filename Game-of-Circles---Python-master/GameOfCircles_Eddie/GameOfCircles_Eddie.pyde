import platform
from Bullet import Bullet
from Gunna import Gunna
from Player import Player
from SpriteManager import sprites
from Raindrop import Raindrop
from JiggleBot import JiggleBot
from ScreenSaverBot import ScreenSaverBot
import SpriteManager

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height-100, playerTeam)
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(JiggleBot(200, 50, 2))
    SpriteManager.spawn(Gunna(200, 50, 2))
    
    #sprites.append(Gunna(50, 50, enemyTeam))
    #sprites.append(Raindrop(25, 25, enemyTeam))
    #sprites.append(Raindrop(75, 75, enemyTeam))
    #sprites.append(Raindrop(125, 125, enemyTeam))
    #sprites.append(Raindrop(175, 175, enemyTeam))
    #sprites.append(Raindrop(0, 0, enemyTeam))
    #sprites.append(Raindrop(300, 300, enemyTeam))
    #sprites.append(Raindrop(375, 375, enemyTeam))
    #sprites.append(Raindrop(425, 425, enemyTeam))
    #sprites.append(Raindrop(325, 325, enemyTeam))
    #sprites.append(Raindrop(475, 475, enemyTeam))
    #sprites.append(JiggleBot(random(0,500), random(0,200), enemyTeam))
    #sprites.append(ScreenSaverBot(width/2, 500, enemyTeam))
    
                                      
def draw():
    global player, sprites
    background(255)    
    SpriteManager.animate()

    for sprite in sprites:
        sprite.animate()
        
    checkCollisions()
    
def checkCollisions():
    global sprites
    for a in sprites:
        for b in sprites:
            if a.team != b.team:
                d = (pow(a.x - b.x, 2) + pow(a.y - b.y, 2))**(0.5)
                r1 = a.diameter / 2
                r2 = b.diameter / 2
                if(r1 + r2 > d):
                    sprites.remove(a)
                    sprites.remove(b)
    
def keyPressed():
    global player
    player.keyDown()    
        
def keyReleased():
    global player
    player.keyUp()
