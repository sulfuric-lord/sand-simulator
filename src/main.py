import pygame
import materials
from config import grid, CELL_SIZE, GRID_WIDTH, GRID_HEIGHT

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

materials_list = []

materials_list.append(materials.Sand())
materials_list.append(materials.Salt())
materials_list.append(materials.Water())
materials_list.append(materials.Steel())

active_material = 0

main_font = pygame.font.Font("Monocraft.otf", 24)


def handle_input():
    mouse_pressed = pygame.mouse.get_pressed()
    mouse_x, mouse_y = pygame.mouse.get_pos()

    grid_x = mouse_x // CELL_SIZE
    grid_y = mouse_y // CELL_SIZE

    if mouse_pressed[0]:
        materials_list[active_material].spawn(grid_x, grid_y)
    elif mouse_pressed[2]:
       grid[grid_x][grid_y] = None

running = True
while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                active_material = 0
            elif event.key == pygame.K_2:
                active_material = 1
            elif event.key == pygame.K_3:
                active_material = 2
            elif event.key == pygame.K_4:
                active_material = 3

    handle_input()

    for material in materials_list:
        material.update()
        material.draw(screen)

    name_text = main_font.render(materials_list[active_material].name, False, (255, 255, 255))
    screen.blit(name_text, (0, 0))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
