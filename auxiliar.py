import pygame
from constants import *

class Auxiliar:
    @staticmethod
    def getSurfaceFromSpriteSheet(path,columnas,filas,flip=False):
        lista = []
        surface_imagen = pygame.image.load(path)
        fotograma_ancho = int(surface_imagen.get_width()/columnas)
        fotograma_alto = int(surface_imagen.get_height()/filas)
       
        for fila in range(filas):
            for columna in range(columnas):
                x = columna * fotograma_ancho
                y = fila * fotograma_alto
                surface_fotograma = surface_imagen.subsurface(x,y,fotograma_ancho,fotograma_alto)
                surface_fotograma = pygame.transform.scale(surface_fotograma,(ALTO_PERSONAJE,ANCHO_PERSONAJE))
                if flip:
                    surface_fotograma = pygame.transform.flip(surface_fotograma,True,False)
                lista.append(surface_fotograma)
        return lista
