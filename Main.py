import pygame
from Player import *
from Network import *
from Package import *
from _thread import *
import VaribleWatcher 
pygame.init()
screen = pygame.display.set_mode((1920/2,1088/2))
clock = pygame.time.Clock()
n = Network()
player = Player(n.id)
package = Package(n.id,player)

playersList =[]
run = True

def sortPackages(wanted_id,list):
    for x in list:
        
        if x.getPlayer().player_id == wanted_id:
                return x.getPlayer()
        
def handleOtherPalyer(otherPackage):
    global playersList
    otherPlayers_1 = sortPackages(1,otherPackage)
    otherPlayers_2 = sortPackages(2,otherPackage)
    otherPlayers_3 = sortPackages(3,otherPackage)
    return otherPlayers_1,otherPlayers_2,otherPlayers_3


def displayOtherCharacter():
     for i in playersList:
         if (i!=None):
            i.update(screen)
    
    
   
clock.tick(60)

while run:
    screen.fill((0,0,0))
    #pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    
      
   
    player.movement(screen)
    package.setPlayer(player)
    otherPackages = n.send(package)
    p1,p2,p3 = handleOtherPalyer(otherPackages)
    #vw = VaribleWatcher.VaribleWatcher("Player Position",player.position)
    
    
    
    
    pygame.display.update()
    
    
    
    
pygame.quit()

