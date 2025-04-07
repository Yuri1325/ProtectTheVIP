import pygame
vector = pygame.math.Vector2
class Player(pygame.sprite.Sprite):
    def __init__(self,facingRight = True):
        super().__init__()
        self.position = vector(0,0)
        self.rect = pygame.Surface((20,50))
        self.rect.fill('White')
   
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.position[1] -=5
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.position[1] +=5
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.position[0] +=5
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.position[0] -=5
            
    def update(self,win):
        self.draw(win)
        self.movement()
    def draw(self,window):
        window.blit(self.rect,(self.position[0],self.position[1]))
