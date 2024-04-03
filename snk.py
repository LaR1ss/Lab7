import pygame
import random
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
SNAKE_SIZE = 20
FOOD_SIZE = 20
INITIAL_SPEED = 5

WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game')

snake = [(WIDTH // 2, HEIGHT // 2)]
snake_direction = 'RIGHT'
snake_speed = INITIAL_SPEED

food_position = (random.randint(0, WIDTH - FOOD_SIZE) // FOOD_SIZE * FOOD_SIZE,
                 random.randint(0, HEIGHT - FOOD_SIZE) // FOOD_SIZE * FOOD_SIZE)

score = 0
level = 1

font = pygame.font.SysFont(None, 36)

def generate_food_position():
    global food_position
    while True:
        new_food_position = (random.randint(0, WIDTH - FOOD_SIZE) // FOOD_SIZE * FOOD_SIZE,
                             random.randint(0, HEIGHT - FOOD_SIZE) // FOOD_SIZE * FOOD_SIZE)
        if new_food_position not in snake:
            food_position = new_food_position
            break

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                snake_direction = 'RIGHT'
            elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                snake_direction = 'LEFT'
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                snake_direction = 'UP'
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                snake_direction = 'DOWN'

    head_x, head_y = snake[0]
    if snake_direction == 'RIGHT':
        head_x += SNAKE_SIZE
    elif snake_direction == 'LEFT':
        head_x -= SNAKE_SIZE
    elif snake_direction == 'UP':
        head_y -= SNAKE_SIZE
    elif snake_direction == 'DOWN':
        head_y += SNAKE_SIZE

    if (head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT
            or (head_x, head_y) in snake[:-1]):
        running = False

    if (head_x, head_y) == food_position:
        score += 1
        if score % 3 == 0: 
            level += 1
            snake_speed += 1  
        snake.append((head_x, head_y))
        generate_food_position()

    snake.insert(0, (head_x, head_y))
    if len(snake) > (score + 1):
        del snake[-1]

    window.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(window, GREEN, (segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE))
    pygame.draw.rect(window, RED, (food_position[0], food_position[1], FOOD_SIZE, FOOD_SIZE))

    text_surface = font.render(f'Score: {score}  Level: {level}', True, BLUE)
    window.blit(text_surface, (10, 10))

    pygame.display.update()

    clock.tick(snake_speed)

    game_over_font = pygame.font.SysFont(None, 72)
game_over_text = game_over_font.render('Game Over', True, RED)
window.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))

pygame.display.update()

time.sleep(2)

pygame.quit()
