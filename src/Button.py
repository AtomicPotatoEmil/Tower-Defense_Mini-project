import pygame


class Button:
    __image = []


    def __init__(self, image, size_x, size_y, pos_x, pos_y, text = ''):
        self.__image = image
        self.__sizeX = size_x
        self.__sizeY = size_y
        self.__posX = pos_x
        self.__posY = pos_y
        self.__text = text

    def get_text(self) -> str:
        return self.__text

    def set_text(self, new_text: str) -> None:
        self.__text = new_text

    def display_button(self):
        pygame.image.load