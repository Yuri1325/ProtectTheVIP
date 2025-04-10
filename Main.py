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

playersList =[]
run = True


 



    
   
clock.tick(60)

while run:
    screen.fill((255,255,255))
    #pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    
      
    
    package = Package(n.id,player)
    player.movement(screen)
    otherPackages = n.send(package)
    print(f"Player Pos; {player.position}")
    for x in otherPackages:
        if x.getPlayer().player_id !=player.player_id:
            x.getPlayer().draw(screen)

            

    
    
    
    
    pygame.display.update()
    
    
    
    
pygame.quit()

