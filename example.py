import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Axis Rotation")

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 3D axis points
axis_points = np.array([
    [100, 0, 0],  # X-axis endpoint
    [0, 100, 0],  # Y-axis endpoint
    [0, 0, 100],  # Z-axis endpoint
    [0, 0, 0]     # Origin
])

# Projection matrix (simple orthographic projection)
def project(point):
    scale = 4  # Scale factor for visualization
    return int(WIDTH / 2 + point[0] * scale), int(HEIGHT / 2 - point[1] * scale)

# Rotation matrices
def rotation_matrix_x(angle):
    return np.array([
        [1, 0, 0],
        [0, np.cos(angle), -np.sin(angle)],
        [0, np.sin(angle), np.cos(angle)]
    ])

def rotation_matrix_y(angle):
    return np.array([
        [np.cos(angle), 0, np.sin(angle)],
        [0, 1, 0],
        [-np.sin(angle), 0, np.cos(angle)]
    ])

def rotation_matrix_z(angle):
    return np.array([
        [np.cos(angle), -np.sin(angle), 0],
        [np.sin(angle), np.cos(angle), 0],
        [0, 0, 1]
    ])

# Main loop
running = True
last_mouse_pos = pygame.mouse.get_pos()
angle_x, angle_y = 0, 0
while running:
    screen.fill(WHITE)
    
    # Mouse movement for rotation
    mouse_x, mouse_y = pygame.mouse.get_pos()
    dx, dy = mouse_x - last_mouse_pos[0], mouse_y - last_mouse_pos[1]
    angle_x += np.radians(dy * 0.5)  # Adjust sensitivity
    angle_y += np.radians(dx * 0.5)
    last_mouse_pos = (mouse_x, mouse_y)
    
    # Compute rotation
    rotation_x = rotation_matrix_x(angle_x)
    rotation_y = rotation_matrix_y(angle_y)
    rotated_points = [rotation_y @ rotation_x @ point for point in axis_points]
    
    # Project and draw axis
    projected_points = [project(p) for p in rotated_points]
    pygame.draw.line(screen, RED, projected_points[3], projected_points[0], 3)  # X-axis
    pygame.draw.line(screen, GREEN, projected_points[3], projected_points[1], 3)  # Y-axis
    pygame.draw.line(screen, BLUE, projected_points[3], projected_points[2], 3)  # Z-axis
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    pygame.time.delay(16)  # 60 FPS

pygame.quit()