import pygame
from lib import transformations as t

def points_tracker(obj, display):
    #Faig una translació amb lclick, deixo anar el lclick i això hauria d'actualitzar les posicions dels punts del meu eix de coordenades (abs_axis).
    # Podem provar això fent: lclick -> moure el mouse -> automàticament homotècia.
    pygame.draw.line(display, 'red', pygame.mouse.get_pos(), t.translation(obj.pos[:2], [display.get_width()/2, display.get_height()/2]))
    for point in obj.positions:
        pygame.draw.line(display, 'red', pygame.mouse.get_pos(), t.translation(point[:2], [display.get_width()/2, display.get_height()/2]))