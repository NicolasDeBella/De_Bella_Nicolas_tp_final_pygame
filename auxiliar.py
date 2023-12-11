import pygame
from constants import *

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path,columns,rows,high_image,width_image,flip=False):
        list = []
        surface_image = pygame.image.load(path)
        width_frame = int(surface_image.get_width()/columns)
        high_frame = int(surface_image.get_height()/rows)
       
        for row in range(rows):
            for columns in range(columns):
                x = columns * width_frame
                y = row * high_frame
                surface_frame = surface_image.subsurface(x,y,width_frame,high_frame)
                surface_frame = pygame.transform.scale(surface_frame,(high_image,width_image))
                if flip:
                    surface_frame = pygame.transform.flip(surface_frame,True,False)
                list.append(surface_frame)
        return list
