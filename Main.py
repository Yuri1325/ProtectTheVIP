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

playersList =[]
run = True




# def displayOtherCharacter():
#      for i in playersList:
#          if (i!=None):
#             i.update(screen)
    
    
   
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
    
    
    
    
    pygame.display.update()
    
    
    
    
pygame.quit()

