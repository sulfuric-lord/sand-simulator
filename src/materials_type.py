import pygame
from config import grid, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE
import random

class Material:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def spawn(self, x, y):
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            if grid[x][y] is None:
                grid[x][y] = self

    def draw(self, surface):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if isinstance(grid[x][y], Material):
                    pygame.draw.rect(surface, grid[x][y].color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Solid(Material):
    def update(self):
        pass

class Liquid(Material):
    def update(self):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT - 1, -1, -1):
                if grid[x][y] is self:
                    if y + 1 < GRID_HEIGHT and grid[x][y + 1] is None:
                        grid[x][y + 1] = self
                        grid[x][y] = None
                    elif y + 1 < GRID_HEIGHT:
                        direction = random.choice([-1, 1])
                        if 0 <= x + direction < GRID_WIDTH:
                            if grid[x + direction][y] == None:
                                grid[x + direction][y] = self
                                grid[x][y] = None

class Powder(Material):
    def update(self):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT - 1, -1, -1):
                if grid[x][y] is self:
                    if y + 1 < GRID_HEIGHT and (grid[x][y + 1] is None or isinstance(grid[x][y + 1], Liquid)):
                        grid[x][y + 1] = self
                        grid[x][y] = None
                    elif y + 1 < GRID_HEIGHT:
                        direction = random.choice([-1, 1])
                        if 0 <= x + direction < GRID_WIDTH and (grid[x + direction][y + 1] is None or isinstance(grid[x + direction][y + 1], Liquid)):
                            grid[x + direction][y + 1] = self
                            grid[x][y] = None