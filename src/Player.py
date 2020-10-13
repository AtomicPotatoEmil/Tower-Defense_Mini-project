import pygame
import pygame.sprite

from src.Unit import *
from src.GameView import *


class Player(pygame.sprite.Sprite):
    __cash = 0
    __hitPoints = 0
    __name = "default"
    __xCastle = 168
    __yCastle = 636
    __hCastle = 64
    __wCastle = 64

    mouseHit = False

    def __init__(self, hp: int, money: int, name: str):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        self.sprites.append(pygame.image.load("Sprites/castlebig.png"))
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.topleft = [self.__xCastle, self.__yCastle]

        self.__cash = money
        self.__hitPoints = hp
        self.__name = name

    def getName(self):
        return self.__name

    def setName(self, newName: str):
        self.__name = newName

    def getMoney(self):
        return self.__cash

    def setMoney(self, money: int):
        self.__cash = money

    def getHp(self):
        return self.__hitPoints

    def setHp(self, hp: int):
        self.__hitPoints = hp

    def buyUnits(self, unitCost: int):
        moneyLeft = self.getMoney() - unitCost
        self.setMoney(moneyLeft)

    def takeDamage(self, damage: int):
        hpLeft = self.getHp() - damage
        self.setHp(hpLeft)

    def hitDetection(self, getRect):
        hitBox = pygame.Rect(self.__xCastle, self.__yCastle, self.__wCastle, self.__hCastle)
        hitBox.colliderect(getRect)

    def mouseDetection(self, mousePos, rectPos):
        if rectPos.collidepoint(mousePos):
            return self.mouseHit

    def placeUnit(self, mousePos, unitCost: int):
        if self.mouseHit == True:
            self.buyUnits(unitCost)

    def drawCastle(self, window):
        window.blit(self.castleImg, (self.__xCastle, self.__yCastle))


    def updatePlayer(self, window, damage: int, getRect):
        self.takeDamage(damage)
        self.hitDetection(getRect)
        self.drawCastle(window)

