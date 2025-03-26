import pygame
import objects as o
import transformations as t

def debug(obj):
    #Faig una translació amb lclick, deixo anar el lclick i això hauria d'actualitzar les posicions dels punts del meu eix de coordenades (abs_axis).
    # Podem provar això fent: lclick -> moure el mouse -> automàticament homotècia.
    pygame.draw.line(DISPLAY_SURF, 'red', pygame.mouse.get_pos(), t.translation(obj.pos[:2], [DISPLAY_SURF.get_width()/2, DISPLAY_SURF.get_height()/2]))
    for point in obj.positions:
        pygame.draw.line(DISPLAY_SURF, 'red', pygame.mouse.get_pos(), t.translation(point[:2], [DISPLAY_SURF.get_width()/2, DISPLAY_SURF.get_height()/2]))

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
            start_pos = event.pos

        # Detect left mouse button release
        if event.type == pygame.MOUSEBUTTONUP:  # Left button
            abs_axis.update(DISPLAY_SURF, event, vector)
            vector = [0, 0]
            start_pos = None  # Reset start position when button is released
            
    if start_pos:  # Left button is still pressed
        current_pos = pygame.math.Vector2(pygame.mouse.get_pos())  # Get the current mouse position
        vector = current_pos - start_pos

    DISPLAY_SURF.fill("black")
    
    abs_axis.draw(DISPLAY_SURF, vector)
    #debug(abs_axis)
    #print(abs_axis.pos, abs_axis.x_pos, abs_axis.y_pos, abs_axis.z_pos)

    #cube.update(dt)
    
    #cube.draw(DISPLAY_SURF, (DISPLAY_SURF.get_width()/2, DISPLAY_SURF.get_height()/2))

    pygame.display.update()

pygame.quit()