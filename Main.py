import pygame
from Player import *

pygame.init()
screen = pygame.display.set_mode((1920/2,1088/2))
clock = pygame.time.Clock()
p = Player(True)
run = True
while run:
    screen.fill((0,0,0))
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            run = False
    p.update(screen)
    pygame.display.update()
    pygame.display.flip()
    
pygame.quit()
