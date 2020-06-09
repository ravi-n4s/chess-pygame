import pygame


class King(pygame.sprite.Sprite):
    def __init__(self, color, size):
        super(King, self).__init__()
        self.color = color
        self.size = size
        self.surf = pygame.Surface((size, size), pygame.SRCALPHA)
        img = pygame.image.load(f"assets/{self.color}_king.png")
        img = pygame.transform.scale(img, (size, size))
        self.surf.blit(img, (0, 0))
        self.rect = self.surf.get_rect()
        self.rect.x, self.rect.y = (
            (4*size, 7*size) if self.color == "white" else (4*size, 0))  # inital position

    def get_pos(self):
        return (self.rect.y//self.size, self.rect.x//self.size)

    def move_to(self, pos):
        self.rect.x, self.rect.y = pos[1]*self.size, pos[0]*self.size

    def tryGetBoardValue(self, board, x, y):
        try:
            if board[x][y] == 0 or board[x][y].color != self.color and x > -1 and y > -1:
                return (x, y)
            else:
                return None
        except:
            return None

    def get_possible_moves(self, board):
        x, y = self.get_pos()
        moves = [  # 8 possible moves for king
            self.tryGetBoardValue(board, x+1, y+1),
            self.tryGetBoardValue(board, x+1, y),
            self.tryGetBoardValue(board, x+1, y-1),

            self.tryGetBoardValue(board, x, y+1),
            self.tryGetBoardValue(board, x, y-1),

            self.tryGetBoardValue(board, x-1, y+1),
            self.tryGetBoardValue(board, x-1, y),
            self.tryGetBoardValue(board, x-1, y-1)
        ]
        return [m for m in moves if m is not None]
