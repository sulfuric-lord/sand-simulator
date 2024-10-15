# powder.py
import random
from materials import Material
from config import GRID_WIDTH, GRID_HEIGHT

class Powder(Material):
    def update(self, material_type):
        cells_to_update = [(x, y) for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT - 1)]
        random.shuffle(cells_to_update)
        
        for x, y in cells_to_update:
            if self.grid[x][y] == material_type:
                if y + 1 < GRID_HEIGHT and self.grid[x][y + 1] == 0:
                    self.grid[x][y] = 0
                    self.grid[x][y + 1] = material_type
                elif y + 1 < GRID_HEIGHT:
                    direction = random.choice([-1, 1])
                    if 0 <= x + direction < GRID_WIDTH and self.grid[x + direction][y + 1] == 0:
                        self.grid[x][y] = 0
                        self.grid[x + direction][y + 1] = material_type
