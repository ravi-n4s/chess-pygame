import pygame

class Queen(pygame.sprite.Sprite):
    def __init__(self, color):
        super(Queen, self).__init__()
        self.color = color
        self.surf = pygame.Surface((100,100), pygame.SRCALPHA)
        self.surf.blit(pygame.image.load(f"assets/{self.color}_queen.png"),(0,0))
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = ((300,700) if self.color == "white" else (300,0)) #inital position
    
    def move_to(self, pos):
        self.rect.x, self.rect.y = pos