import pygame
from Player import *
from Network import *
from Package import *
from _thread import *
pygame.init()
screen = pygame.display.set_mode((1920/2,1088/2))
clock = pygame.time.Clock()
n = Network()
player = Player(n.id)
package = Package(n.id,player)

playersList = [player,]
run = True

def sortPackages(wanted_id,list):
    for x in list:
        print(type(x.getPlayer()))
        if x.getClient_Id == wanted_id:
            if not(x.getPlayer()==None):
                return x.player
def handleOtherPalyer(otherPackage):
    global playersList
    otherPlayers_1 =sortPackages(1,otherPackage)
    otherPlayers_2 = sortPackages(2,otherPackage)
    otherPlayers_3 = sortPackages(3,otherPackage)
    
    otherPlayers_1.update(screen)
    otherPlayers_2.update(screen)
    otherPlayers_3.update(screen)
    

while run:
    screen.fill((0,0,0))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    
    
    player.draw(screen)
    player.movement()
    package.setPlayer(player)
    otherPackages = n.send(package).getChildrenList()
    #print(otherPackages)
    handleOtherPalyer(otherPackages)
    
    
    pygame.display.update()
    pygame.display.flip()
    
    
pygame.quit()

