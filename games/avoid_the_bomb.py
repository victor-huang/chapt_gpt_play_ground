import pygame
import random

# Initialize pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Square, circle, and bomb attributes
SQUARE_SIZE = 50
CIRCLE_RADIUS = 25
BOMB_SIZE = 40
SPEED = 5
BOMB_SPEED = 3

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Avoid the Bomb!")

x, y = (SCREEN_WIDTH - SQUARE_SIZE) // 2, (SCREEN_HEIGHT - SQUARE_SIZE) // 2
square_color = YELLOW

circles = [
    {"pos": (100, 100), "color": RED},
    {"pos": (700, 100), "color": BLUE},
    {"pos": (100, 500), "color": GREEN},
    {"pos": (700, 500), "color": RED}
]

# Bomb attributes
bomb_x = random.randint(0, SCREEN_WIDTH - BOMB_SIZE)
bomb_y = random.randint(0, SCREEN_HEIGHT - BOMB_SIZE)
bomb_dx = random.choice([-BOMB_SPEED, BOMB_SPEED])
bomb_dy = random.choice([-BOMB_SPEED, BOMB_SPEED])

game_over = False

def display_game_over():
    font = pygame.font.SysFont(None, 75)
    text = font.render("GAME OVER", True, BLACK)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))

running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= SPEED
        if keys[pygame.K_RIGHT]:
            x += SPEED
        if keys[pygame.K_UP]:
            y -= SPEED
        if keys[pygame.K_DOWN]:
            y += SPEED
        
        # Bomb movement
        bomb_x += bomb_dx
        bomb_y += bomb_dy
        
        if bomb_x <= 0 or bomb_x >= SCREEN_WIDTH - BOMB_SIZE:
            bomb_dx = -bomb_dx
        if bomb_y <= 0 or bomb_y >= SCREEN_HEIGHT - BOMB_SIZE:
            bomb_dy = -bomb_dy
        
        # Check for collisions with circles and change square color
        for circle in circles:
            distance = ((x + SQUARE_SIZE // 2 - circle["pos"][0])**2 + 
                        (y + SQUARE_SIZE // 2 - circle["pos"][1])**2)**0.5
            if distance < CIRCLE_RADIUS + SQUARE_SIZE // 2:
                square_color = circle["color"]
                break
        
        # Check for collision with bomb
        if (bomb_x < x + SQUARE_SIZE and bomb_x + BOMB_SIZE > x and
            bomb_y < y + SQUARE_SIZE and bomb_y + BOMB_SIZE > y):
            game_over = True
        
        # Draw the circles
        for circle in circles:
            pygame.draw.circle(screen, circle["color"], circle["pos"], CIRCLE_RADIUS)
        
        # Draw the bomb
        pygame.draw.rect(screen, BLACK, (bomb_x, bomb_y, BOMB_SIZE, BOMB_SIZE))
        
        # Draw the square
        pygame.draw.rect(screen, square_color, (x, y, SQUARE_SIZE, SQUARE_SIZE))
    else:
        display_game_over()
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
