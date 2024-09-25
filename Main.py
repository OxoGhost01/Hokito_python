import pygame
import Plateau
import sys
import Menu

from pygame.locals import *
"""
:author : OxoGhost
"""

"""
BLANC = 0
NOIR = 1

0 = Homepage
1 = Bot level choice
2 = Easy mode
3 = Medium mode
4 = Duo
5 = Exit
"""

pygame.init()
screen = pygame.display.set_mode((840, 840))
pygame.display.set_caption("Hokito")
menu = Menu.Menu(screen)
mode = 0
choice = 0
done = False
while True:
    screen.fill((120, 120, 120))
    menu.view(mode)
    if mode != 0 and mode != 1:
        jeu.dessin_plateau()
        jeu.play_bot(mode)
    else:
        choice = menu.cursor(pygame.mouse.get_pos(), mode)
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONUP:
            if mode == 0 or mode == 1:
                mode = choice
                if choice == 2 or choice == 3 or choice == 4:
                    jeu = Plateau.Jeu(screen, choice)
            else:
                jeu.click(pygame.mouse.get_pos())
        if event.type == K_ESCAPE:
            jeu.reset()
        if event.type == QUIT or mode == 5:
            pygame.quit()
            sys.exit()
    pygame.display.update()
