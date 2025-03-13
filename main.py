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

start_pos = None
vector = pygame.math.Vector2([0, 0])

abs_axis = o.Axis([0, 0, 0])

run = True
while run:
    # delta-time to achieve constant pixel/second speed of objects on display regardless of hardware specs
    dt = clock.tick(FPS) / 1000

    DISPLAY_SURF.fill("black")

    if start_pos:  # Left button is still pressed
        current_pos = pygame.math.Vector2(pygame.mouse.get_pos())  # Get the current mouse position
        vector = current_pos - start_pos

    abs_axis.draw(DISPLAY_SURF, vector)

    # event loop
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left button
            start_pos = event.pos  # Store the initial click position
            abs_axis.update(vector)

        # Detect left mouse button release
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left button
            start_pos = None  # Reset start position when button is released

    pygame.display.update()

pygame.quit()