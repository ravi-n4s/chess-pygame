import pygame

class Move(pygame.sprite.Sprite):
    def __init__(self, size, init_pos=None):
        super(Move, self).__init__()
        self.size = size
        self.surf = pygame.Surface((size,size), pygame.SRCALPHA)
        img = pygame.image.load(f"assets/move.png")
        img = pygame.transform.scale(img, (size, size))
        self.surf.blit(img, (0, 0))
        self.rect = self.surf.get_rect()
        if (init_pos is not None):
            self.rect.x, self.rect.y = init_pos
    
    def get_pos(self):
        return (self.rect.y//self.size, self.rect.x//self.size)