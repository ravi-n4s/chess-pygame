import pygame

class Horse(pygame.sprite.Sprite):
    def __init__(self, color, init_pos=None):
        super(Horse, self).__init__()
        self.color = color
        self.surf = pygame.Surface((100,100), pygame.SRCALPHA)
        self.surf.blit(pygame.image.load(f"assets/{self.color}_horse.png"),(0,0))
        self.rect = self.surf.get_rect()
        if (init_pos is not None):
            self.rect.x, self.rect.y = init_pos
    
    def move_to(self, pos):
        self.rect.x, self.rect.y = pos