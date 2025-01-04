import pygame
import random

# Initialize Pygame
pygame.init()

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Game settings
display_width = 800
display_height = 600
block_size = 10
snake_speed = 15
font_style = pygame.font.SysFont(None, 25)

# Initialize the display
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

def display_score(score):
    """Displays the score on the screen."""
    value = font_style.render("Your Score: " + str(score), True, white)
    game_display.blit(value, [0, 0])

def draw_snake(block_size, snake_list):
    """Draws the snake on the screen."""
    for x, y in snake_list:
        pygame.draw.rect(game_display, green, [x, y, block_size, block_size])

def message(msg, color):
    """Displays a message on the screen."""
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [display_width / 6, display_height / 3])

def game_loop():
    """Main game loop."""
    game_over = False
    game_close = False

    # Starting position of the snake
    x1 = display_width / 2
    y1 = display_height / 2
    x1_change = 0
    y1_change = 0

    # Snake properties
    snake_list = []
    snake_length = 1

    # Food position
    foodx = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
    foody = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0

    while not game_over:
        while game_close == True:
            game_display.fill(black)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -block_size
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = block_size
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -block_size
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = block_size
                    x1_change = 0

        # Boundary check
        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        game_display.fill(black)

        # Draw food
        pygame.draw.rect(game_display, red, [foodx, foody, block_size, block_size])

        # Snake body mechanics
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check if snake hit itself
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(block_size, snake_list)
        display_score(snake_length - 1)

        pygame.display.update()

        # Check if snake hit the food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - block_size) / 10.0) * 10.0
            foody = round(random.randrange(0, display_height - block_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()