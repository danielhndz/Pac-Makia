import pygame

class player(pygame.sprite.Sprite):
    def __init__(self, posx,posy, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.velocidad = 1
        self.rect.top = posy
        self.rect.left = posx
        self.vidas = 3
        self.score = 0
        
    def dibujar(self,superficie):
        superficie.blit(self.image, self.rect)

            
class enemy(pygame.sprite.Sprite):
    def __init__(self, posx,posy, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.velocidad = 1
        self.rect.top = posy
        self.rect.left = posx
        
    def dibujar(self,superficie):
        superficie.blit(self.image, self.rect)

class cookie(pygame.sprite.Sprite):
    def __init__(self, posx,posy, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.top = posy
        self.rect.left = posx
        self.vida = True
        
    def dibujar(self,superficie):
        superficie.blit(self.image, self.rect)

class obstacle(pygame.sprite.Sprite):
    def __init__(self, posx,posy, img):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.top = posy
        self.rect.left = posx

    def dibujar(self,superficie):
        superficie.blit(self.image, self.rect)
