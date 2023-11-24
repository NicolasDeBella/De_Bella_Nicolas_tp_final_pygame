import pygame
from constants import *
from auxiliar import Auxiliar
from bullet import Bullet

class Player(pygame.sprite.Sprite):
    def __init__(self,x,y,speed_walk,gravity,jump_power,frame_animacion_rate_ms,frame_movimiento_rate_ms) -> None:
        super().__init__()
        self.stay_r = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\stay.png",1,1)
        self.stay_l = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\stay.png",1,1,True)
        self.walk_r = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\walk.png",9,1)
        self.walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\walk.png",9,1,True)
        self.jump_r = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\jump.png",13,1)
        self.jump_l = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\jump.png",13,1,True)
        self.attack_r = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\attack.png",4,1)
        self.attack_l = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\attack.png",4,1,True)
        self.move_x = 0 #player arranca quieto en la posicion x
        self.move_y = 0 #player arranca quieto en la posicion y
        self.speed_walk = speed_walk
        self.gravity = gravity
        self.jump_power = jump_power
        self.is_jump = False
        self.y_start_jump = 0
        self.direction = DIRECTION_R
        self.tiempo_transcurrido_animacion = 0
        self.frame_animacion_rate_ms = frame_animacion_rate_ms
        self.tiempo_transcurrido_movimiento = 0
        self.frame_movimiento_rate_ms = frame_movimiento_rate_ms
        self.frame = 0
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = x #posicion inicial en x
        self.rect.y = y #posicion inicial en y
        self.bullet_group = pygame.sprite.Group()

    def stay(self):
        if self.animation != self.stay_r and self.animation != self.stay_l:
            if self.direction == DIRECTION_R:
                self.animation = self.stay_r   
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0
            #self.is_jump = False

    def walk(self,direction):
        if self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l):
            self.frame = 0
            self.direction = direction
            if self.direction == DIRECTION_R:
                self.move_x = self.speed_walk
                self.animation = self.walk_r
            else:
                self.move_x = -self.speed_walk
                self.animation = self.walk_l
            
    def jump(self):
        if not self.is_jump:
            self.is_jump = True
            self.y_start_jump = self.rect.y
            self.jump_power = self.jump_power

        if self.is_jump:
            if self.jump_power >= -self.jump_power:
                self.rect.y = self.y_start_jump - (self.jump_power * abs(self.jump_power)) * 0.5
                self.jump_power -= self.gravity
                self.animation = self.jump_r
            else:
                self.jump_power = self.jump_power
                self.is_jump = False

    def attack(self):
        if self.direction == DIRECTION_R:
            self.animation = self.attack_r   
        else:
            self.animation = self.attack_l
        self.create_bullet()
        self.frame = 0


    def create_bullet(self):
        if self.direction == DIRECTION_R:
            bullet_direction = DIRECTION_L
        else:
            bullet_direction = DIRECTION_R
        bullet = Bullet(self.rect.centerx, self.rect.centery, bullet_direction)
        self.bullet_group.add(bullet)


    def keyboard_events(self, teclas_presionadas):
        if not teclas_presionadas[pygame.K_LEFT] and not teclas_presionadas[pygame.K_RIGHT]:
            self.stay()
        if teclas_presionadas[pygame.K_LEFT] and teclas_presionadas[pygame.K_RIGHT]:
            self.stay()
        elif teclas_presionadas[pygame.K_LEFT] and not teclas_presionadas[pygame.K_RIGHT]:
            self.walk(DIRECTION_L)
        elif not teclas_presionadas[pygame.K_LEFT] and teclas_presionadas[pygame.K_RIGHT]:
            self.walk(DIRECTION_R)
        if teclas_presionadas[pygame.K_SPACE]:
            self.jump()
        if teclas_presionadas[pygame.K_f] and not teclas_presionadas[pygame.K_LEFT] and not teclas_presionadas[pygame.K_RIGHT]:
            self.attack()

    def windows_limits(self):
        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > ANCHO_VENTANA - self.rect.width:
            self.rect.x = ANCHO_VENTANA - self.rect.width

        if self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.y > ALTO_VENTANA - self.rect.height:
            self.rect.y = ALTO_VENTANA - self.rect.height
    

    def movimiento(self,delta_ms):
        self.tiempo_transcurrido_movimiento += delta_ms
        if self.tiempo_transcurrido_movimiento >= self.frame_movimiento_rate_ms:
            self.tiempo_transcurrido_movimiento = 0
            self.rect.x += self.move_x
            self.rect.y += self.move_y

            # if self.rect.y < 475:
            #     self.rect.y += self.gravity 
            
            
    def animacion(self,delta_ms):
        self.tiempo_transcurrido_animacion += delta_ms
        if self.tiempo_transcurrido_animacion >= self.frame_animacion_rate_ms:
            self.tiempo_transcurrido_animacion = 0

            if self.frame < len(self.animation) - 1:
                self.frame += 1
                self.windows_limits()
            else:
                self.frame = 0
      
    def update(self,delta_ms):
        self.movimiento(delta_ms)
        self.animacion(delta_ms)
        self.bullet_group.update()
           
    def draw(self,screen):
        self.image = self.animation[self.frame]
        screen.blit(self.image,self.rect)
        self.bullet_group.draw(screen)