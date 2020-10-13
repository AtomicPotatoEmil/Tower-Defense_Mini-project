import pygame


class Unit:
    __name = ""
    __hp = 0
    __damage = 0
    __moveSpeed = 0
    __x = 0
    __y = 0
    __width = 16
    __height = 16

    def __init__(self, name: str, hp: int, damage: int, moveSpeed: int, x: int, y: int, width: int, height: int):
        self.__name = name
        self.__hp = hp
        self.__damage = damage
        self.__moveSpeed = moveSpeed
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def getUnitName(self):
        return self.__name

    def getUnitHp(self):
        return self.__hp

    def getUnitDamage(self):
        return self.__damage

    def getUnitMoveSpeed(self):
        return self.__moveSpeed

    def getUnitX(self):
        return self.__x

    def getUnitY(self):
        return self.__y

    def getUnitWidth(self):
        return self.__width

    def getUnitHeight(self):
        return self.__height

    def move(self):
        self.__y += self.__moveSpeed

    def unitHitBox(self):
        _unitHitBox = pygame.Rect(self.__x, self.__y, self.__width, self.__height)

    # def update(self):
    #     __unitHitBox = __unitRect

    def draw(self, surface):
        __unitRect = pygame.draw.rect(surface, (0, 0, 128), self.__x, self.__y, self.__width, self.__height)
