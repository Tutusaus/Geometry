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

    def update(self):

        start_pos = None
        vector = [0, 0, 0]

        for event in pygame.event.get():
            # Detect left mouse button down
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left button
                updated_vertices = True
                start_pos = event.pos  # Store the initial click position
                self.pos = t.translation(self.pos, vector)
                for point in self.positions:
                    point = t.translation(point, vector)

            # Detect left mouse button release
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left button
                start_pos = None  # Reset start position when button is released
            
        # If the left mouse button is being held down
        if start_pos:  # Left button is still pressed
            current_pos = pygame.math.Vector2(pygame.mouse.get_pos())  # Get the current mouse position
            for i in range(len(vector)-1):
                vector[i] = current_pos[i] - start_pos[i]  # Calculate vector

        return updated_vertices

    """ def update(self, delta_time):
        SPEED = 1
        update_vertices = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.alpha -= SPEED * delta_time
            update_vertices = True
        if keys[pygame.K_s]:
            self.alpha += SPEED * delta_time
            update_vertices = True
        if keys[pygame.K_a]:
            self.beta -= SPEED * delta_time
            update_vertices = True
        if keys[pygame.K_d]:
            self.beta += SPEED * delta_time
            update_vertices = True
        if keys[pygame.K_e]:
            self.gamma -= SPEED * delta_time
            update_vertices = True
        if keys[pygame.K_q]:
            self.gamma += SPEED * delta_time
            update_vertices = True
        
        if update_vertices:
            for vertice in range(Cube.num_vertices):
                # self.vertices[vertice] = t.rotation(t.translation(self.vertices[vertice], -self.center_of_mass), self.alpha, self.beta, self.gamma)
                self.vertices[vertice] = t.rotation(self.vertices[vertice], self.alpha, self.beta, self.gamma) """

    def draw(self, display, delta_time):
        letter_offset = 5
        if self.update():
            origin = t.translation(t.xy_projection(self.pos), [display.get_width() / 2, display.get_height() / 2])
            for point, letter in zip(self.positions, ['x', 'y', 'z']):
                final_pos = t.translation(t.xy_projection(point), [display.get_width() / 2, display.get_height() / 2])
                pygame.draw.line(display, "white", origin, final_pos)
                text = self.font.render(letter, True, "white")
                text_rect = text.get_rect(center=final_pos + letter_offset)
                display.blit(text, text_rect)
                