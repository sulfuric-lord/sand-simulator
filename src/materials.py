from materials_type import Powder, Liquid, Solid
from config import grid, GRID_WIDTH, GRID_HEIGHT

import random


class Sand(Powder):
    def __init__(self):
        super().__init__((237, 201, 175), "Sand")

class Salt(Powder):
    def __init__(self):
        super().__init__((240, 240, 255), "Salt")

    def update(self):
        for x in range(GRID_WIDTH):
            for y in range(GRID_HEIGHT - 1, -1, -1):
                if grid[x][y] is self:
                    if y + 1 < GRID_HEIGHT and (grid[x][y + 1] is None or isinstance(grid[x][y + 1], Liquid)):
                        grid[x][y + 1] = self
                        grid[x][y] = None
                    
                    interact_direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                    for i in interact_direction:
                        new_x = x + i[0]
                        new_y = y + i[1]
                        if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
                            if isinstance(grid[new_x][new_y], Water):
                                if random.randint(0, 10) == 1:
                                    grid[x][y] = None


class Water(Liquid):
    def __init__(self):
        super().__init__((0, 0, 255), "Water")

class Steel(Solid):
    def __init__(self):
        super().__init__((100, 100, 100), "Steel")