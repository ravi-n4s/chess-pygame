import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE
from King import King
from Queen import Queen
from Elephant import Elephant
from Camel import Camel
from Horse import Horse
from Soldier import Soldier

pygame.init()

screen = pygame.display.set_mode([400,400])
running = True
bg_img = pygame.image.load("assets/board.png")
move_indicator = pygame.image.load("assets/move.png")

Board = [
    [Elephant("black",(0,0)), Horse("black",(100,0)), Camel("black",(200,0)),Queen("black"), King("black"), Camel("black",(500,0)), Horse("black",(600,0)), Elephant("black",(700,0))],
    [Soldier("black", (0,100)), Soldier("black", (100,100)), Soldier("black", (200,100)), Soldier("black", (300,100)), Soldier("black", (400,100)), Soldier("black", (500,100)), Soldier("black", (600,100)), Soldier("black", (700,100))],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [Soldier("white", (0,600)), Soldier("white", (100,600)), Soldier("white", (200,600)), Soldier("white", (300,600)), Soldier("white", (400,600)), Soldier("white", (500,600)), Soldier("white", (600,600)), Soldier("white", (700,600))],
    [Elephant("white",(0,700)), Horse("white",(100,700)), Camel("white",(200,700)),Queen("white"), King("white"), Camel("white",(500,700)), Horse("white",(600,700)), Elephant("white",(700,700))]
]

mouse_click = (-1,-1)
next_move = "white"

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_click = pygame.mouse.get_pos()
            print(mouse_click)
    screen.blit(bg_img, (0,0)) #background image
    
    for row,values in enumerate(Board):
        for col,piece in enumerate(values):
            if piece == 0:
                continue
            if piece == -1:
                screen.blit(move_indicator, (row*100,col*100))
                continue
            screen.blit(piece.surf, piece.rect)
            if mouse_click[0] != -1 and piece.rect.collidepoint(mouse_click) and piece.color == next_move:
                for x,y in piece.get_possible_moves():
                    Board[x][y] = -1
                mouse_click = (-1,-1)

    pygame.display.flip()

pygame.quit()