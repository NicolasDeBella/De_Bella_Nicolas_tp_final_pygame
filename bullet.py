
import pygame
from constants import (DIRECTION_L, DIRECTION_R,ANCHO_VENTANA)

class Bullet(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,direction):
        super().__init__()
        original_image = pygame.image.load(r"assets\graphics\player\bullet_circule.png").convert_alpha()
        scaled_image = pygame.transform.scale(original_image,(9,9))
        self.image = scaled_image
        self.rect = self.image.get_rect(center=(pos_x, pos_y))
        self.speed = 5  # Ajusta la velocidad de la bala
        self.direction = direction
        
    def update(self):
        # Actualiza la posición de la bala en función de su dirección y velocidad
        if self.direction == DIRECTION_L:
            self.rect.x += self.speed
        elif self.direction == DIRECTION_R:  
            self.rect.x -= self.speed
        
        if self.rect.right < 0 or self.rect.left > ANCHO_VENTANA:
            self.kill()