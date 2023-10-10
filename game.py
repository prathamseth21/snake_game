import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
GRID_SIZE = 20
SPEED = 7

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

# Initialize the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize Snake variables
snake_x, snake_y = WIDTH // 2, HEIGHT // 2
snake_dx, snake_dy = GRID_SIZE, 0
snake_body = [(snake_x, snake_y)]

# Initialize Food variables
food_x, food_y = random.randint(0, WIDTH - GRID_SIZE) // GRID_SIZE * GRID_SIZE, random.randint(0, HEIGHT - GRID_SIZE) // GRID_SIZE * GRID_SIZE

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle user input to change Snake's direction
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dy == 0:
        snake_dx, snake_dy = 0, -GRID_SIZE
    if keys[pygame.K_DOWN] and snake_dy == 0:
        snake_dx, snake_dy = 0, GRID_SIZE
    if keys[pygame.K_LEFT] and snake_dx == 0:
        snake_dx, snake_dy = -GRID_SIZE, 0
    if keys[pygame.K_RIGHT] and snake_dx == 0:
        snake_dx, snake_dy = GRID_SIZE, 0

    # Update Snake's position
    snake_x += snake_dx
    snake_y += snake_dy

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        food_x, food_y = random.randint(0, WIDTH - GRID_SIZE) // GRID_SIZE * GRID_SIZE, random.randint(0, HEIGHT - GRID_SIZE) // GRID_SIZE * GRID_SIZE
        snake_body.append((snake_x, snake_y))

    # Check for collision with the boundaries or itself
    if (snake_x < 0 or snake_x >= WIDTH or
        snake_y < 0 or snake_y >= HEIGHT or
        (snake_x, snake_y) in snake_body[:-1]):
        pygame.quit()
        sys.exit()

    # Update Snake's body
    snake_body.insert(0, (snake_x, snake_y))

    # If the Snake hasn't eaten, remove the tail segment
    if len(snake_body) > 1 and (snake_x, snake_y) != snake_body[-1]:
        snake_body.pop()

    # Clear the screen
    screen.fill(BLACK)

    # Draw Snake
    for segment in snake_body:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    # Draw Food
    pygame.draw.rect(screen, WHITE, (food_x, food_y, GRID_SIZE, GRID_SIZE))

    # Update the display
    pygame.display.update()

    # Control game speed
    pygame.time.Clock().tick(SPEED)
# ... (previous code)

# Control game speed
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ... (remaining code)

    # Update the display
    pygame.display.update()

    # Control game speed
    clock.tick(SPEED)

# Quit Pygame
pygame.quit()
sys.exit()