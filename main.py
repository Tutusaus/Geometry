import pygame
from src import objects as o
from lib import transformations as t
import inputs.mouse as m

WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480

#general setup
pygame.init()
DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Geometry')
clock = pygame.time.Clock()
FPS = 120

mouse = m.Mouse(None, None, [0, 0])

axis = o.Axis([0, 0, 0])
#cube = o.Cube(100)

run = True
while run:
    # delta-time to achieve constant pixel/second speed of objects on display regardless of hardware specs
    dt = clock.tick(FPS) / 1000

    # event loop
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse.start_pos = event.pos
            mouse.button = event.button

        # Detect left mouse button release
        if event.type == pygame.MOUSEBUTTONUP:  # Left button
            axis.update(DISPLAY_SURF, mouse)
            mouse.reset()
            
    if mouse.start_pos:  # Left button is still pressed
        current_pos = pygame.math.Vector2(pygame.mouse.get_pos())  # Get the current mouse position
        mouse.direction = current_pos - mouse.start_pos

    DISPLAY_SURF.fill("black")
    # He de dibuixar qualsevol cosa a partir d'aquesta línia en avall
    
    axis.draw(DISPLAY_SURF, mouse)

    #cube.update(dt)
    
    #cube.draw(DISPLAY_SURF, (DISPLAY_SURF.get_width()/2, DISPLAY_SURF.get_height()/2))
    pygame.display.update()

pygame.quit()