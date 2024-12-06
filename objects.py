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

    def update(self, delta_time):
        SPEED = 1
        updated_vertices = True
        """ start_pos = None
        vector = (0, 0)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                start_pos = event.pos
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                start_pos = None
            
        if start_pos and pygame.mouse.get_pressed()[0]:
            updated_vertices = True
            current_pos = pygame.mouse.get_pos()
            vector = (current_pos[0] - start_pos[0], current_pos[1] - start_pos[1])
            self.positions = [t.translation(point, vector) for point in self.positions]
 """
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
        if self.update(delta_time):
            origin = t.xy_projection(self.pos) + [display.get_width() / 2, display.get_height() / 2]
            for point in self.positions:
                pygame.draw.line(display, "white", origin, t.xy_projection(point) + [display.get_width() / 2, display.get_height() / 2])