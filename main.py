import pygame
from os.path import join

import objects as o

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

#general setup
pygame.init()
DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Geometry')
clock = pygame.time.Clock()
FPS = 120

abs_axis = o.Axis([0, 0, 0])

run = True
while run:
    # delta-time to achieve constant pixel/second speed of objects on display regardless of hardware specs
    dt = clock.tick(FPS) / 1000

    # event loop
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            abs_axis.update() = True

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            abs_axis.update() = False

    DISPLAY_SURF.fill("black")

    abs_axis.draw(DISPLAY_SURF, dt)

    pygame.display.update()

pygame.quit()