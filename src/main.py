import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
CELL_SIZE = 8
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

SAND_COLOR = (194, 178, 128)
BACKGROUND_COLOR = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Симуляция песка')
clock = pygame.time.Clock()

main_font = pygame.font.Font("Monocraft.otf", 20)

grid = [[1 if random.randint(0, 8) == 0 else 0 for _ in range(GRID_HEIGHT)] for _ in range(GRID_WIDTH)]

DRAW_SAND = 1
ERASE = 2
tool_mode = DRAW_SAND

def draw_grid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[x][y] == 1:
                pygame.draw.rect(screen, SAND_COLOR, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def update_grid():
    cells_to_update = [(x, y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT - 1)]
    random.shuffle(cells_to_update)
    for x, y in cells_to_update:
        if grid[x][y] == 1:
            if y + 1 < GRID_HEIGHT and grid[x][y + 1] == 0:
                grid[x][y] = 0
                grid[x][y + 1] = 1
            elif y + 1 < GRID_HEIGHT:
                direction = random.choice([-1, 1])
                if 0 <= x + direction < GRID_WIDTH and grid[x + direction][y + 1] == 0:
                    grid[x][y] = 0
                    grid[x + direction][y + 1] = 1

def count_sand():
    total_sand = 0
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            if grid[x][y] == 1:
                total_sand += 1
    return total_sand

def handle_input():
    global tool_mode
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    grid_x = mouse_x // CELL_SIZE
    grid_y = mouse_y // CELL_SIZE

    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        tool_mode = DRAW_SAND
    elif keys[pygame.K_2]:
        tool_mode = ERASE

    if mouse_pressed[0] and 0 <= grid_x < GRID_WIDTH and 0 <= grid_y < GRID_HEIGHT:
        if tool_mode == DRAW_SAND:
            grid[grid_x][grid_y] = 1
        elif tool_mode == ERASE:
            grid[grid_x][grid_y] = 0

running = True
while running:
    screen.fill(BACKGROUND_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handle_input()
    update_grid()
    draw_grid()

    sand = count_sand()  # Теперь считаем песчинки на экране
    text = main_font.render(f"Total pixels: {sand}", False, (255, 255, 255))
    screen.blit(text, (530, 0))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
