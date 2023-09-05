# TESTING PROCESS TO GET THE WINDOWS SIZE

"""import pygame

pygame.init()
screen = pygame.display.set_mode((1750,900))
background = pygame.image.load("assets/poker-table.asset.jpeg").convert_alpha()
SCREEN_WIDHT, SCREEN_HEIGHT = pygame.display.get_surface().get_size()


background = pygame.transform.scale(background, (SCREEN_WIDHT, SCREEN_HEIGHT))


run = True

while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.blit(background, (0,0))
    pygame.display.update()

pygame.quit()"""

# CODE TO PLAY ALONG (WINDOWS SIZE)
"""
#imports
import pygame
from pygame.locals import *
pygame.init()

#bounds definition
STARTWIDTH, STARTHEIGHT = 200, 200
MAXWIDTH, MAXHEIGHT = 200, 200
MINWIDTH, MINHEIGHT = 200, 200

#variables
screen = pygame.display.set_mode((STARTWIDTH, STARTHEIGHT), RESIZABLE)
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == VIDEORESIZE:

            width = min(MAXWIDTH, max(MINWIDTH, event.w))
            height = min(MAXHEIGHT, max(MINHEIGHT, event.h))

            if (width, height) != event.size:
                screen = pygame.display.set_mode((width, height), RESIZABLE)

    screen.fill((255,255,255))
    pygame.display.update()

pygame.quit()
"""