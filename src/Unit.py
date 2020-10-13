import pygame
import pygame.sprite


class Unit(pygame.sprite.Sprite):
    __unitName = ""
    __unitHp = 0
    __unitDamage = 0
    __unitMoveSpeed = 0
    __unitX = 0
    __unitY = 0
    __unitWidth = 16
    __unitHeight = 16

    def __init__(self, name: str, hp: int, damage: int, moveSpeed: int, x: int, y: int, width: int, height: int):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        self.sprites.append(pygame.image.load("Sprites/castlebig.png"))

        self.__unitName = name
        self.__unitHp = hp
        self.__unitDamage = damage
        self.__unitMoveSpeed = moveSpeed
        self.__unitX = x
        self.__unitY = y
        self.__unitWidth = width
        self.__unitHeight = height

    def getUnitName(self):
        return self.__unitName

    def getUnitHp(self):
        return self.__unitHp

    def getUnitDamage(self):
        return self.__unitDamage

    def getUnitMoveSpeed(self):
        return self.__unitMoveSpeed

    def getUnitX(self):
        return self.__unitX

    def getUnitY(self):
        return self.__unitY

    def getUnitWidth(self):
        return self.__unitWidth

    def getUnitHeight(self):
        return self.__unitHeight

    def unitCollision(self, getUnitRect):
        unitHitBox = pygame.Rect(self.__unitX, self.__unitY, self.__unitWidth, self.__unitHeight)
        unitHitBox.colliderect(getUnitRect)

<<<<<<< Updated upstream
    # def update(self):
    #     __unitHitBox = __unitRect
=======
    def drawUnit(self, window):
        window.blit(self.unitSprite, (self.__unitX, self.__unitY))
>>>>>>> Stashed changes

    def updateUnit(self, window):
        self.drawUnit(window)