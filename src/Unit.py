import pygame


class Unit:
    __hp = 0
    __damage = 0
    __moveSpeed = 0
    __range = 0
    __attackSpeed = 0
    __name = ""
    __x = 0
    __y = 0
    __width = 16
    __height = 16
    olleh = 12
    test = "test"

    def __init__(self, hp: int, damage: int, moveSpeed: int, range: int, attackSpeed: int, name: str, x: int, y: int,
                 width: int, height: int):
        self.__hp = hp
        self.__damage = damage
        self.__moveSpeed = moveSpeed
        self.__range = range
        self.__attackSpeed = attackSpeed
        self.__name = name
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def getUnitX(self):
        return self.__x

    def getUnitY(self):
        return self.__y

    def move(self):
        self.__y += self.__moveSpeed

    def unitHitBox(self):
        __unitHitBox = pygame.Rect(self.__x, self.__y, self.__width, self.__height)

    def update(self):
        __unitHitBox = __unitRect

    def draw(self, surface):
        __unitRect = pygame.draw.rect(surface, (0, 0, 128), self.__x, self.__y, self.__width, self.__height)