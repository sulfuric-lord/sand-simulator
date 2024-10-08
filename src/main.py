import pygame
import random

WIDTH, HEIGHT = 200, 120
PIXEL_SIZE = 5
brush_size = 3

cursor_state = 1

grid = [[random.randint(1, 3) if random.random() < 0.3 else 0 for i in range(WIDTH)] for j in range(HEIGHT)]

pygame.init()

win = pygame.display.set_mode((WIDTH * PIXEL_SIZE, HEIGHT * PIXEL_SIZE))
clock = pygame.time.Clock()

brush_icon = pygame.image.load("images/brush.png")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b:
                cursor_state = 1
            elif event.key == pygame.K_v:
                cursor_state = 2
            
    mouse_pressed = pygame.mouse.get_pressed()
    
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    grid_x = mouse_y // PIXEL_SIZE  
    grid_y = mouse_x // PIXEL_SIZE  
        
    if mouse_pressed[0]:
        if cursor_state == 1:
            for i in range(-brush_size, brush_size + 1):
                for j in range(-brush_size, brush_size + 1):
                    if 0 <= grid_x + i < HEIGHT and 0 <= grid_y + j < WIDTH:
                        grid[grid_x + i][grid_y + j] = random.randint(1, 3)
        elif cursor_state == 2:
            for i in range(-brush_size, brush_size + 1):
                for j in range(-brush_size, brush_size + 1):
                    if 0 <= grid_x + i < HEIGHT and 0 <= grid_y + j < WIDTH:
                        grid[grid_x + i][grid_y + j] = 0
    win.fill((0, 0, 0))
    
    for x in range(HEIGHT - 2, -1, -1):
        for y in range(WIDTH):
            if grid[x][y] != 0:

                if grid[x + 1][y] == 0:
                    grid[x][y], grid[x + 1][y] = 0, grid[x][y]

                elif y < WIDTH - 1 and grid[x + 1][y + 1] == 0:
                    grid[x][y], grid[x + 1][y + 1] = 0, grid[x][y]
                
                elif y > 0 and grid[x + 1][y - 1] == 0:
                    grid[x][y], grid[x + 1][y - 1] = 0, grid[x][y]
                    
    for x in range(HEIGHT):
        for y in range(WIDTH):
            if grid[x][y] == 1:
                pygame.draw.rect(win, (255, 215, 0), (y * PIXEL_SIZE, x * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
            if grid[x][y] == 2:
                pygame.draw.rect(win, (255, 223, 51), (y * PIXEL_SIZE, x * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))
            if grid[x][y] == 3:
                pygame.draw.rect(win, (254, 255, 107), (y * PIXEL_SIZE, x * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE))    
    
    win.blit(brush_icon, (WIDTH * PIXEL_SIZE - 50, 10))
    
    pygame.display.update()

    clock.tick(30)

pygame.quit()
