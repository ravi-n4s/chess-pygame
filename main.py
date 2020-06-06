import pygame

pygame.init()

screen = pygame.display.set_mode([800,800])
running = True
bg_img = pygame.image.load("assets/board.png")
wking = pygame.image.load("assets/white_king.png")
bking = pygame.image.load("assets/black_king.png")
move_indicator = pygame.image.load("assets/move.png")

possible_moves = [(340,40),(340, 140),(440,640),(440,740)]

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill([255,255,255])
    screen.blit(bg_img, (0,0)) #background image
    
    screen.blit(wking, (300,700))
    screen.blit(bking, (400,0))

    for move in possible_moves:
        screen.blit(move_indicator, move)

    pygame.display.flip()

pygame.quit()