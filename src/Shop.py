import pygame

class Shop:

    def buy(self, cost, balance):

        if(cost > balance):
            return self.cantAfford()

        elif(cost <= balance):
            remainingBalance = balance - cost
            return remainingBalance


    def cantAfford(self):
        pass



