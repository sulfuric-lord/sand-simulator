# material.py
import pygame
from config import grid, GRID_WIDTH, GRID_HEIGHT, CELL_SIZE
import random

class Material:
    def __init__(self, color):
        self.color = color

    def spawn(self, x, y):
        """Создает материал в указанных координатах"""
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            if grid[x][y] is None:  # Проверяем, что клетка пуста
                grid[x][y] = self  # Сохраняем объект материала в сетке

    def draw(self, surface):
        """Отображает материал на экране"""
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT):
                if isinstance(grid[x][y], Material):
                    pygame.draw.rect(surface, grid[x][y].color, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

class Powder(Material):
    def update(self):
        """Обновляет положение порошкообразного материала"""
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT - 1, -1, -1):  # Проходим сетку снизу вверх
                if grid[x][y] is self:
                    # Падаем вниз, если клетка под текущей пуста
                    if y + 1 < GRID_HEIGHT and grid[x][y + 1] is None:
                        grid[x][y + 1] = self
                        grid[x][y] = None
                    # Если клетка под занята, пытаемся сместиться вбок
                    elif y + 1 < GRID_HEIGHT:
                        direction = random.choice([-1, 1])  # Рандомно выбираем направление
                        if 0 <= x + direction < GRID_WIDTH and grid[x + direction][y + 1] is None:
                            grid[x + direction][y + 1] = self
                            grid[x][y] = None
