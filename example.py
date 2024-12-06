import pygame

pygame.init()

# Screen setup
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Click and Drag Vector")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Variables to track the initial click position and vector
start_pos = None  # Will store the initial click position
vector = (0, 0)   # Vector between start_pos and current mouse position

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect left mouse button down
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left button
            start_pos = event.pos  # Store the initial click position

        # Detect left mouse button release
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left button
            start_pos = None  # Reset start position when button is released

    # If the left mouse button is being held down
    if start_pos and pygame.mouse.get_pressed()[0]:  # Left button is still pressed
        current_pos = pygame.mouse.get_pos()  # Get the current mouse position
        vector = (current_pos[0] - start_pos[0], current_pos[1] - start_pos[1])  # Calculate vector

    # Drawing
    screen.fill(BLACK)  # Clear the screen
    if start_pos:
        # Draw the initial point
        pygame.draw.circle(screen, RED, start_pos, 5)
        # Draw a line showing the vector
        pygame.draw.line(screen, WHITE, start_pos, pygame.mouse.get_pos(), 2)

    # Display the vector on the console
    if start_pos:
        print(f"Vector: {vector}")

    pygame.display.flip()  # Update the screen

pygame.quit()
