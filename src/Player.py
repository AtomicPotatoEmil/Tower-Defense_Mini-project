

import pygame
import pygame.sprite




class Player:
    __cash = 0
    __hitPoints = 0
    __name = "default"
    __xCastle = 0
    __yCastle = 0
    __hCastle = 64
    __wCastle = 64

    mouseHit = False
    castleImg = pygame.image.load("Sprites/castlebig.png")


    def __init__(self, hp: int, money: int, name: str, xCastle, yCastle):
        self.__cash = money
        self.__hitPoints = hp
        self.__name = name
        castleDisplay = pygame.display.set_mode((self.__wCastle,self.__hCastle))
        castleDisplay.blit(self.castleImg, (xCastle, yCastle))





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

    def updatePlayer(self):
        self.takeDamage()
        self.hitDetection()

