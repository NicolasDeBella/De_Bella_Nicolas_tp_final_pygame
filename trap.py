import pygame
from auxiliar import Auxiliar  
from constants import (DEBUG,HIGH_TRAP,WIDTH_TRAP)

class Trap(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y):
        super().__init__()
        self.__trap = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\trap\trap.png",4,1,HIGH_TRAP,WIDTH_TRAP)
        self.__frame = 0
        self.__animation = self.__trap
        self.__image = self.__animation[self.__frame]
        self.__rect = self.__image.get_rect()
        self.__rect.x = pos_x
        self.__rect.y = pos_y
        self.__radius = 18
        self.__elapsed_time_animation = 0
        self.__frame_animacion_rate_ms = 20
    
    @property
    def rect(self):
        return self.__rect
    
    @property
    def radius(self):
        return self.__radius
    
    def animations(self,delta_ms):
        self.__elapsed_time_animation += delta_ms
        if self.__elapsed_time_animation >= self.__frame_animacion_rate_ms:
            self.__elapsed_time_animation = 0
            if self.__frame < len(self.__animation) - 1:
                self.__frame += 1
            else:
                self.__frame = 0


    def update(self,delta_ms):
        self.animations(delta_ms)


    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,(255,0,0),self.__rect)
            pygame.draw.circle(screen, (0, 0, 255), self.__rect.center,self.__radius)
        self.__image = self.__animation[self.__frame]
        screen.blit(self.__image,self.__rect)