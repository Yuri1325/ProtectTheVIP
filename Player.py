import pygame
vector = pygame.math.Vector2
class Player(pygame.sprite.Sprite):
    def __init__(self,facingRight = True):
        super().__init__()
        self.position = vector(0,0)
        
