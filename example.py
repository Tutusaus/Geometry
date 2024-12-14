import pygame
from os.path import join
import transformations as t

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400

#general setup
pygame.init()
DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
DISPLAY_SURF_MID = [WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2]
pygame.display.set_caption('kjknk')
clock = pygame.time.Clock()
FPS = 120

start_pos = None
vector = [0, 0]

line_start = DISPLAY_SURF_MID
line_end = DISPLAY_SURF_MID + pygame.math.Vector2(50, 0)

run = True
while run:
    # delta-time to achieve constant pixel/second speed of objects on display regardless of hardware specs
    dt = clock.tick(FPS) / 1000

    DISPLAY_SURF.fill("black")

    # event loop
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT or (event.type == pygame.KEYUP and event.key == pygame.K_ESCAPE):
            run = False

        # Detect left mouse button down
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left button
            start_pos = event.pos  # Store the initial click position
            line_start = t.translation(line_start, vector)
            line_end = t.translation(line_end, vector)

        # Detect left mouse button release
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left button
            start_pos = None  # Reset start position when button is released

    # If the left mouse button is being held down
    if start_pos:  # Left button is still pressed
        current_pos = pygame.math.Vector2(pygame.mouse.get_pos())  # Get the current mouse position
        vector = current_pos - start_pos  # Calculate vector


    pygame.draw.line(DISPLAY_SURF, "white", t.translation(line_start, vector), t.translation(line_end, vector))

    pygame.display.update()

pygame.quit()