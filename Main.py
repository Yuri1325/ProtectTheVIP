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
otherPackages = []
playersList = [player,]
run = True

def sortPackages(wanted_id,list):
    for x in list:
        if x.getClient_Id == wanted_id:
            return x.getPlayer()
def handleOtherPalyer(otherPackage):
    global playersList
    otherPlayers_1 = start_new_thread(sortPackages,(1,otherPackage))
    playersList.append(otherPlayers_1)
    otherPlayers_2 = start_new_thread(sortPackages,(2,otherPackage))
    playersList.append(otherPlayers_2)
    otherPlayers_3 = start_new_thread(sortPackages,(3,otherPackage))
    playersList.append(otherPlayers_3)
def updatePlayers():
        global playersList,screen
        for x in playersList:
             x.update(screen)
while run:
    screen.fill((0,0,0))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    
    
    player.draw(screen)
    
    package.setPlayer(player)
    otherPackages = n.send(package)
    handleOtherPalyer(otherPackages)
    #updatePlayers()
    player.movement()
    pygame.display.update()
    pygame.display.flip()
    
    
pygame.quit()

