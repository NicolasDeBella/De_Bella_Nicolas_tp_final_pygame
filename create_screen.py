import pygame
from constants import (WIDTH_WINDOW,HIGH_WINDOW)

class CreateScreen():
    def __init__ (self,path,width,high):
        self.__image = pygame.image.load(path).convert_alpha()
        self.__transform_image = pygame.transform.scale(self.__image,(width,high))
        self.__rect =  self.__transform_image.get_rect()
        self.__rect.x = (WIDTH_WINDOW - width) / 2
        self.__rect.y = (HIGH_WINDOW - high) / 2

    def draw(self,screen):
        screen.blit( self.__transform_image,self.__rect)