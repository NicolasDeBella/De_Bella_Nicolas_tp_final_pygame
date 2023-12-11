import pygame
from constants import (DEBUG)

class Platform(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y,high,width):
        super().__init__()
        self.__original_image = pygame.image.load(r"assets\graphics\platform\platform_grass.png").convert_alpha()
        self.__image = pygame.transform.scale(self.__original_image, (high, width)) 
        self.__rect = self.__image.get_rect()
        self.__rect.x = pos_x
        self.__rect.y = pos_y
        self.__rect_ground_collition = pygame.Rect(self.__rect.x, self.__rect.y + 15, self.__rect.w, 55)
          
    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def rect_ground_collition(self):
        return self.__rect_ground_collition
    
    @rect_ground_collition.setter
    def rect_ground_collition(self, rect_ground_collition):
        self.__rect_ground_collition = rect_ground_collition

    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,(255,0,0),self.__rect)
            pygame.draw.rect(screen,(0, 0, 255),self.__rect_ground_collition)
        screen.blit(self.__image,self.__rect)
        if DEBUG:
            pygame.draw.rect(screen,(0, 0, 255),self.__rect_ground_collition)
        
        