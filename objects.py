import pygame
import transformations as t

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

    def update(self, v):
        pos_xy = t.translation(t.xy_projection(self.pos), v)
        self.pos[:2] = pos_xy
        for point in range(len(self.positions)):
            positions_xy = t.translation(t.xy_projection(self.positions[point]), v)
            self.positions[point][:2] = positions_xy

    def draw(self, display, v):
        # This is what must be drawn always
        origin = t.translation(t.translation(t.xy_projection(self.pos), [display.get_width() / 2, display.get_height() / 2]), v)
        for point, letter in zip(self.positions, ['x', 'y', 'z']):
            final_pos = t.translation(t.translation(t.xy_projection(point), [display.get_width() / 2, display.get_height() / 2]), v)
            pygame.draw.line(display, "white", origin, final_pos)
            letter = self.font.render(letter, True, "white")
            letter_rect = letter.get_rect(center=final_pos + self.letter_offset)
            display.blit(letter, letter_rect)