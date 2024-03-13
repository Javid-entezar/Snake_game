import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
red = (213, 50, 80)

# Snake initial settings
snake_block = 10
snake_speed = 15
snake_list = []
snake_length = 1

# Initial position of the Snake
x1, y1 = width / 2, height / 2
x1_change, y1_change = 0, 0

# Food initial position
foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

# Game loop flag
game_over = False

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, [x[0], x[1], snake_block, snake_block])

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -snake_block
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = snake_block
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -snake_block
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = snake_block
                x1_change = 0

    # Update snake position
    x1 += x1_change
    y1 += y1_change

    if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
        game_over = True

    # Clear the screen
    display.fill(white)

    # Draw the food
    pygame.draw.rect(display, red, [foodx, foody, snake_block, snake_block])

    # Snake movement
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check collision with itself
    for block in snake_list[:-1]:
        if block == snake_head:
            game_over = True

    draw_snake(snake_block, snake_list)
    pygame.display.update()

    # Snake eating food
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
        snake_length += 1

    pygame.time.Clock().tick(snake_speed)

# Quit Pygame
pygame.quit()
