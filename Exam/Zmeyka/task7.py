import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
FPS = 10

# Цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Создание окна
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Змейка")

# Функция для отрисовки сетки
def draw_grid():
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))

# Функция для отрисовки змейки
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

# Функция для генерации случайной позиции для еды
def generate_food(snake):
    while True:
        food_x = random.randint(0, GRID_WIDTH - 1) * GRID_SIZE
        food_y = random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        food_pos = (food_x, food_y)
        if food_pos not in snake:
            return food_pos

# Основной игровой цикл
snake = [(GRID_SIZE * 5, GRID_SIZE * 5)]
food = generate_food(snake)
direction = (GRID_SIZE, 0)
score = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, GRID_SIZE):
                direction = (0, -GRID_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -GRID_SIZE):
                direction = (0, GRID_SIZE)
            elif event.key == pygame.K_LEFT and direction != (GRID_SIZE, 0):
                direction = (-GRID_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-GRID_SIZE, 0):
                direction = (GRID_SIZE, 0)

    # Движение змейки
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    snake.insert(0, new_head)

    # Проверка на столкновение с едой
    if snake[0] == food:
        score += 1
        food = generate_food(snake)
    else:
        snake.pop()

    # Проверка на столкновение с границей экрана
    if (
        snake[0][0] < 0
        or snake[0][0] >= SCREEN_WIDTH
        or snake[0][1] < 0
        or snake[0][1] >= SCREEN_HEIGHT
    ):
        pygame.quit()
        sys.exit()

    # Проверка на столкновение с самой собой
    if snake[0] in snake[1:]:
        pygame.quit()
        sys.exit()

    screen.fill((0, 0, 0)) # Очистка экрана

    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE)) # Отрисовка еды

    draw_snake(snake)
    draw_grid()
    pygame.display.update() # Обновление экрана
    clock.tick(FPS) # Установка задержки