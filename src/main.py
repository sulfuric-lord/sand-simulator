# main.py
import pygame
from sand_material import Sand
from salt_material import Salt
from config import grid, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT

# Инициализация
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Создаем материалы
sand_material = Sand()
salt_material = Salt()

def handle_input():
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    grid_x = mouse_x // CELL_SIZE
    grid_y = mouse_y // CELL_SIZE

    if mouse_pressed[0]:  # ЛКМ для создания песка
        sand_material.spawn(grid_x, grid_y)
    elif mouse_pressed[2]:  # ПКМ для создания соли
        salt_material.spawn(grid_x, grid_y)
    elif mouse_pressed[1]:
       grid[grid_x][grid_y] = None

running = True
while running:
    screen.fill((0, 0, 0))  # Черный фон

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    handle_input()

    # Обновляем материалы
    sand_material.update()
    salt_material.update()

    # Отображение материалов
    sand_material.draw(screen)
    salt_material.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
