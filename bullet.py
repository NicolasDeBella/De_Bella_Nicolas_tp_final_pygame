import pygame
from constants import (DIRECTION_L, DIRECTION_R, WIDTH_WINDOW)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, direction, path):
        super().__init__()
        self.__original_image = pygame.image.load(path).convert_alpha()
        self.__image = pygame.transform.scale(self.__original_image, (9, 9)) 
        self.__rect = self.__image.get_rect(center=(pos_x, pos_y))
        self.__speed = 15
        self.__direction = direction
        self.__radius = 18

    @property
    def image(self):
        return self.__image
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def radius(self):
        return self.__radius
    
    def update(self):
        if self.__direction == DIRECTION_L:
            self.rect.x -= self.__speed
        elif self.__direction == DIRECTION_R:  
            self.rect.x += self.__speed
        
        if self.rect.right < 0 or self.rect.left > WIDTH_WINDOW:
            self.kill()
