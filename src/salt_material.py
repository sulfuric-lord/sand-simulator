# salt.py
from materials import Powder
from config import grid, GRID_WIDTH, GRID_HEIGHT

class Salt(Powder):
    def __init__(self):
        super().__init__((240, 240, 255))  # Белый цвет соли

    def update(self):
        """Особая логика для соли — соль собирается в более высокие кучи"""
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT - 1, -1, -1):
                if grid[x][y] is self:
                    # Проверяем, можно ли упасть вниз
                    if y + 1 < GRID_HEIGHT and grid[x][y + 1] is None:
                        grid[x][y + 1] = self
                        grid[x][y] = None
                    # Соль склонна падать не вбок, а оставаться на месте
                    elif y + 1 < GRID_HEIGHT and grid[x][y + 1] is not None:
                        pass  # Остаёмся на месте, если не можем упасть