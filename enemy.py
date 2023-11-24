import pygame
from constants import *
from auxiliar import Auxiliar  
from bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, x_limit_left, x_limit_right,speed,frame_animacion_rate_ms,frame_movimiento_rate_ms):
        super().__init__()
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\walk.png", 9, 1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\walk.png", 9, 1, True)
        self.attack_r = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\enemy\atack.png", 6, 1)
        self.attack_l = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\enemy\atack.png", 6, 1, True)
        self.frame = 0
        self.animation = self.walk_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x_limit_left = x_limit_left
        self.x_limit_right = x_limit_right
        self.speed = speed
        self.direction = DIRECTION_R # 1 para derecha, -1 para izquierda
        self.tiempo_transcurrido_animacion = 0
        self.frame_animacion_rate_ms = frame_animacion_rate_ms
        self.tiempo_transcurrido_movimiento = 0
        self.frame_movimiento_rate_ms = frame_movimiento_rate_ms
        self.bullet_group = pygame.sprite.Group()
        self.time_bullet = 0
        self.time_bullet_rate_ms = 1500

    def cooldown_ready_to_action(self):
        curent_time = pygame.time.get_ticks()
        return curent_time - self.time_bullet >= self.time_bullet_rate_ms
    
    def shoot_bullet(self):
        self.create_bullet()
        self.time_bullet = pygame.time.get_ticks()

        if self.animation != self.attack_l and self.animation != self.attack_r:
            if self.direction == DIRECTION_R:
                self.animation = self.attack_r
            else:
                self.animation = self.attack_l


    def atacar(self):
        if self.rect.right > self.x_limit_right:
            self.animation = self.attack_l
            self.direction = DIRECTION_L
        elif self.rect.left < self.x_limit_left:
              self.animation = self.attack_r
              self.direction = DIRECTION_R
        self.create_bullet()
        
    def create_bullet(self):
        if self.direction == DIRECTION_R:
            bullet_direction = DIRECTION_L
        else:
            bullet_direction = DIRECTION_R
        bullet = Bullet(self.rect.centerx, self.rect.centery, bullet_direction)
        return self.bullet_group.add(bullet)

    def animacion(self,delta_ms):
        self.tiempo_transcurrido_animacion += delta_ms
        if self.tiempo_transcurrido_animacion >= self.frame_animacion_rate_ms:
            self.tiempo_transcurrido_animacion = 0

            if self.frame < len(self.animation) - 1:
                self.frame += 1
            else:
                self.frame = 0

    
    def movimiento(self, delta_ms):
        self.tiempo_transcurrido_movimiento += delta_ms
        if self.tiempo_transcurrido_movimiento >= self.frame_movimiento_rate_ms:
            self.tiempo_transcurrido_movimiento = 0
            self.rect.x += self.speed * self.direction
            
    def update(self,delta_ms,screen):
        self.movimiento(delta_ms)
        self.animacion(delta_ms)
        self.atacar()
        self.shoot_bullet()
        self.bullet_group.update()
        self.bullet_group.draw(screen)
        
        
    def draw(self, screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
        
