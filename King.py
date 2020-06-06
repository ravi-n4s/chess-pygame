import pygame

class King(pygame.sprite.Sprite):
    def __init__(self, color):
        super(King, self).__init__()
        self.color = color
        self.surf = pygame.Surface((100,100), pygame.SRCALPHA)
        self.surf.blit(pygame.image.load(f"assets/{self.color}_king.png"),(0,0))
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = ((400,700) if self.color == "white" else (400,0)) #inital position
    
    def move_to(self, pos):
        self.rect.x, self.rect.y = pos