import pygame
vector = pygame.math.Vector2
class Player(pygame.sprite.Sprite):
    def __init__(self,player_id,facingRight = True):
        super().__init__()
        self.position = vector(0,0)
        self.rect = pygame.Surface((20,50))
        self.player_id = player_id
        self.rect.fill('Black')
        
    def movement(self,win):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.position[1] -=0.5
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.position[1] +=0.5
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.position[0] +=0.5
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.position[0] -=0.5
        self.update_f(win)  
    def update_f(self,win):
        self.draw(win)
    def draw(self,window):
        window.blit(self.rect,(self.position[0],self.position[1]))
    def setColor(self,id):
        if id == 0:
            self.rect.fill('Yellow')
        elif id ==1:
            self.rect.fill('Red')
        elif id ==2:
            self.rect.fill('Blue')
        elif id ==3:
            self.rect.fill('Green')
    def __getstate__(self):
        state = self.__dict__.copy()
        # Exclude the non-serializable attributes
        del state['rect']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.rect = pygame.Surface((20,50))
       
    
    
