import pygame
import math

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Recursive Tree")

def draw_branch(screen, start_x, start_y, length, angle, depth):
    if depth <= 0:
        return

    # Calculate the end point of the branch
    end_x = start_x + length * math.cos(angle)
    end_y = start_y + length * math.sin(angle)

    # Draw the branch
    pygame.draw.line(screen, (255, 255, 255), (start_x, start_y), (end_x, end_y), 1)

    # Recursively draw the next branches
    new_length = length * 0.67  # Reduce the length for the next branches
    new_depth = depth - 1
    # Increase the angle difference for left and right branches
    left_angle = angle - math.pi / 3  # 60 degrees for left branch
    right_angle = angle + math.pi / 3  # 60 degrees for right branch

    draw_branch(screen, end_x, end_y, new_length, left_angle, new_depth)
    draw_branch(screen, end_x, end_y, new_length, right_angle, new_depth)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  # Clear screen with black

    # Draw the tree
    draw_branch(screen, width / 2, height - 100, 150, -math.pi / 2, 10)

    pygame.display.flip()  # Update the full display Surface to the screen

pygame.quit()
