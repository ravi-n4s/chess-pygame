import pygame


class Elephant(pygame.sprite.Sprite):
    def __init__(self, color, size, init_pos=None):
        super(Elephant, self).__init__()
        self.color = color
        self.size = size
        self.surf = pygame.Surface((size, size), pygame.SRCALPHA)
        img = pygame.image.load(f"assets/{self.color}_elephant.png")
        img = pygame.transform.scale(img, (size, size))
        self.surf.blit(img, (0, 0))
        self.rect = self.surf.get_rect()
        if (init_pos is not None):
            self.rect.x, self.rect.y = init_pos

    def get_pos(self):
        return (self.rect.y//self.size, self.rect.x//self.size)

    def move_to(self, pos):
        self.rect.x, self.rect.y = pos[1]*self.size, pos[0]*self.size

    def get_possible_moves(self, board):
        x, y = self.get_pos()
        return []
