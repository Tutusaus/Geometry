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

        self.start_pos = None
        self.vector = [0, 0, 0]

        self.updated = False

    def update(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left button
            self.start_pos = event.pos  # Store the initial click position
            self.updated = True

        # Detect left mouse button release
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left button
            self.start_pos = None  # Reset start position when button is released
            self.updated = False
                
        return self.updated

    def draw(self, display, delta_time, event):

        origin = t.translation(t.xy_projection(self.pos), [display.get_width() / 2, display.get_height() / 2])
        for point, letter in zip(self.positions, ['x', 'y', 'z']):
            final_pos = t.translation(t.xy_projection(point), [display.get_width() / 2, display.get_height() / 2])
            pygame.draw.line(display, "white", origin, final_pos)
            letter = self.font.render(letter, True, "white")
            letter_rect = letter.get_rect(center=final_pos + self.letter_offset)
            display.blit(letter, letter_rect)

        if self.update(event):
            self.pos = t.translation(self.pos, self.vector)
            for point in range(len(self.positions)):
                self.positions[point] = t.translation(self.positions[point], self.vector)

            # If the left mouse button is being held down
            if self.start_pos:  # Left button is still pressed
                current_pos = pygame.math.Vector2(pygame.mouse.get_pos())  # Get the current mouse position
                for i in range(len(self.vector)-1):
                    self.vector[i] = current_pos[i] - self.start_pos[i]  # Calculate vector
            