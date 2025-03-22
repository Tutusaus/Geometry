import pygame
import transformations as t
import math

class Axis():

    def __init__(self, pos):
        self.pos = pygame.Vector3(pos)
        self.length = 50
        self.x_pos = self.pos + [self.length, 0, 0]
        self.y_pos = self.pos + [0, self.length, 0]
        self.z_pos = self.pos + [0, 0, self.length]
        self.positions = [self.x_pos, self.y_pos, self.z_pos]
        
        self.font = pygame.font.Font(None, 20)
        self.letter_offset = 5

    def update(self, display, event, v):
        mouse_pos = t.translation(list(event.pos), [-display.get_width() / 2, -display.get_height() / 2])
        if event.button == 1: # 2d translation along the xy-plane
            self.pos[:2] = t.translation(t.xy_projection(self.pos), v)
            for point in range(len(self.positions)):
                self.positions[point][:2] = t.translation(t.xy_projection(self.positions[point]), v)
        elif event.button == 3: # space rotation
            """ self.pos = t.rotation(self.pos, math.acos(v[1]/math.dist(self.pos, self.z_pos)), -math.asin(v[0]/math.dist(self.pos, self.z_pos)), math.asin(v[1]/math.dist(self.pos, self.x_pos)))
            for point in range(len(self.positions)):
                self.positions[point] = t.rotation(self.positions[point], math.acos(v[1]/math.dist(self.pos, self.z_pos)), -math.asin(v[0]/math.dist(self.pos, self.z_pos)), math.asin(v[1]/math.dist(self.pos, self.x_pos))) """
        elif event.button == 4:
            self.pos[:2] = t.homothety(mouse_pos, t.xy_projection(self.pos))
            for i in range(len(self.positions)):
                self.positions[i][:2] = t.homothety(mouse_pos, t.xy_projection(self.positions[i]))
        elif event.button == 5:
            self.pos[:2] = t.homothety(mouse_pos, t.xy_projection(self.pos), 0.99)
            for i in range(len(self.positions)):
                self.positions[i][:2] = t.homothety(mouse_pos, t.xy_projection(self.positions[i]), 0.99)

    def draw(self, display, v):
        # This is what must be drawn always
        origin = t.translation(t.translation(t.xy_projection(self.pos), [display.get_width() / 2, display.get_height() / 2]), v)
        for point, letter in zip(self.positions, ['x', 'y', 'z']):
            final_pos = t.translation(t.translation(t.xy_projection(point), [display.get_width() / 2, display.get_height() / 2]), v)
            pygame.draw.line(display, "white", origin, final_pos)
            letter = self.font.render(letter, True, "white")
            letter_rect = letter.get_rect(center=final_pos + self.letter_offset)
            display.blit(letter, letter_rect)