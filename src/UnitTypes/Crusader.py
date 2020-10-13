from src.Unit import Unit
import pygame.sprite


class Crusader(pygame.sprite.Sprite):
    __name = "Crusader"
    __hp = 50
    __damage = 5
    __moveSpeed = 1
    __x = 0
    __y = 0
    __width = 16
    __height = 16
    __attackSpeed = 1
    __range = 1

    def __init__(self, hp: int, damage: int, moveSpeed: int, range: int, attackSpeed: int, name: str, x: int, y: int,
                 width: int, height: int):
        super().__init__(name, hp, damage, moveSpeed, x, y, width, height)
        pygame.sprite.Sprite.__init__(self)

        self.__attackSpeed = attackSpeed
        self.__range = range

        self.sprites = []
        self.sprites.append(pygame.image.load("Sprites/Blue_Crusader.png"))
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]


    def slash(self):
        print("slash")

        return 10
