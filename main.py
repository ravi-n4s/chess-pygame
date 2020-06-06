import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE
from King import King
from Queen import Queen
from Elephant import Elephant
from Camel import Camel
from Horse import Horse
from Soldier import Soldier
from Move import Move

pygame.init()
SCREEN_SIZE = 720
ICON_SIZE = SCREEN_SIZE//8

screen = pygame.display.set_mode([SCREEN_SIZE, SCREEN_SIZE])
running = True
bg_img = pygame.transform.scale(pygame.image.load(
    "assets/board.png"), (SCREEN_SIZE, SCREEN_SIZE))
move_indicator = pygame.transform.scale(
    pygame.image.load("assets/move.png"), (ICON_SIZE, ICON_SIZE))

Board = [
    [Elephant("black", ICON_SIZE, (0, 0)), Horse("black", ICON_SIZE, (ICON_SIZE, 0)), Camel("black", ICON_SIZE, (2*ICON_SIZE, 0)), Queen("black", ICON_SIZE),
     King("black", ICON_SIZE), Camel("black", ICON_SIZE, (5*ICON_SIZE, 0)), Horse("black", ICON_SIZE, (6*ICON_SIZE, 0)), Elephant("black", ICON_SIZE, (7*ICON_SIZE, 0))],
    [Soldier("black", ICON_SIZE, (0, ICON_SIZE)), Soldier("black", ICON_SIZE, (ICON_SIZE, ICON_SIZE)), Soldier("black", ICON_SIZE, (2*ICON_SIZE, ICON_SIZE)), Soldier("black", ICON_SIZE, (3*ICON_SIZE, ICON_SIZE)),
     Soldier("black", ICON_SIZE, (4*ICON_SIZE, ICON_SIZE)), Soldier("black", ICON_SIZE, (5*ICON_SIZE, ICON_SIZE)), Soldier("black", ICON_SIZE, (6*ICON_SIZE, ICON_SIZE)), Soldier("black", ICON_SIZE, (7*ICON_SIZE, ICON_SIZE))],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [Soldier("white", ICON_SIZE, (0, 6*ICON_SIZE)), Soldier("white", ICON_SIZE, (ICON_SIZE, 6*ICON_SIZE)), Soldier("white", ICON_SIZE, (2*ICON_SIZE, 6*ICON_SIZE)), Soldier("white", ICON_SIZE, (3*ICON_SIZE, 6*ICON_SIZE)),
     Soldier("white", ICON_SIZE, (4*ICON_SIZE, 6*ICON_SIZE)), Soldier("white", ICON_SIZE, (5*ICON_SIZE, 6*ICON_SIZE)), Soldier("white", ICON_SIZE, (6*ICON_SIZE, 6*ICON_SIZE)), Soldier("white", ICON_SIZE, (7*ICON_SIZE, 6*ICON_SIZE))],
    [Elephant("white", ICON_SIZE, (0, 7*ICON_SIZE)), Horse("white", ICON_SIZE, (ICON_SIZE, 7*ICON_SIZE)), Camel("white", ICON_SIZE, (2*ICON_SIZE, 7*ICON_SIZE)), Queen("white", ICON_SIZE),
     King("white", ICON_SIZE), Camel("white", ICON_SIZE, (5*ICON_SIZE, 7*ICON_SIZE)), Horse("white", ICON_SIZE, (6*ICON_SIZE, 7*ICON_SIZE)), Elephant("white", ICON_SIZE, (7*ICON_SIZE, 7*ICON_SIZE))]
]

mouse_click = (-1,-1)
possible_moves = []
next_move = "white"
clicked_coin = (-1,-1)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click = pygame.mouse.get_pos()
    screen.blit(bg_img, (0, 0))  # background image

    for row, values in enumerate(Board):
        for col, piece in enumerate(values):
            if piece == 0:
                continue
            screen.blit(piece.surf, piece.rect)
            if mouse_click[0] != -1 and piece.rect.collidepoint(mouse_click) and piece.color == next_move: #if clicked on sprite 
                possible_moves = [] #clear possible moves
                clicked_coin = piece.get_pos()
                for row, col in piece.get_possible_moves(Board):
                    possible_moves.append(Move(ICON_SIZE, (col*ICON_SIZE, row*ICON_SIZE)))  #append move sprite to all possible moves
                mouse_click = (-1,-1)
            elif mouse_click[0] != -1: #if not clicked on sprite
                for move in possible_moves:
                    if move.rect.collidepoint(mouse_click): #if clicked on possible move
                        x,y = move.get_pos()
                        if type(Board[x][y]) is King:
                            print(f"{next_move} wins the game")
                            running = False
                        print(f"{clicked_coin} ---moved to ------{(x,y)}")
                        
                        Board[clicked_coin[0]][clicked_coin[1]].move_to((x,y))
                        Board[x][y] = Board[clicked_coin[0]][clicked_coin[1]]
                        Board[clicked_coin[0]][clicked_coin[1]] = 0

                        next_move = "white" if next_move == "black" else "black"
                        mouse_click = (-1,-1)
                #if clicked anywhere else
                possible_moves = []
                clicked_coin = None
        
    for move in possible_moves:
        screen.blit(move.surf, move.rect)
    pygame.display.flip()

pygame.quit()
