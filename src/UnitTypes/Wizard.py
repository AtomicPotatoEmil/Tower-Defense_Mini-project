from src.Unit import *


class Wizards(Unit):
    coolDown = 0

    def __init__(self, hp: int, damage: int, moveSpeed: int, range: int, attackSpeed: int, name: str, x: int, y: int,
                 width: int, height: int):
        super().__init__(hp, damage, moveSpeed, range, attackSpeed, name, x, y, width, height)

    def castSpell(self):
        print('castSpell')
