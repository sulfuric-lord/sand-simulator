# sand_material.py
from materials import Powder

class Sand(Powder):
    def __init__(self):
        super().__init__((237, 201, 175))  # Красный цвет песка