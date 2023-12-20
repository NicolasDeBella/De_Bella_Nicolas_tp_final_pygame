import pygame
from constants import (DIRECTION_L,DIRECTION_R,WIDTH_PLAYER,HIGH_PLAYER,HIGH_WINDOW,WIDTH_WINDOW,DEBUG,GROUND_RECT_H,PATH_DISPARO_SOUND)
from auxiliar import Auxiliar
from bullet import Bullet


class Player(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,speed_walk,gravity,jump_power,jump_height,life,ground_gravity,frame_animacion_rate_ms,frame_movimiento_rate_ms) -> None:
        super().__init__()
        self.__still_r = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\still.png", 1, 1, HIGH_PLAYER, WIDTH_PLAYER)
        self.__still_l = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\still.png", 1, 1, HIGH_PLAYER, WIDTH_PLAYER, True)
        self.__walk_r = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\walk.png", 9, 1, HIGH_PLAYER, WIDTH_PLAYER)
        self.__walk_l = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\walk.png", 9, 1, HIGH_PLAYER, WIDTH_PLAYER, True)
        self.__jump_r = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\jump.png", 13, 1, HIGH_PLAYER, WIDTH_PLAYER)
        self.__jump_l = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\jump.png", 13, 1, HIGH_PLAYER, WIDTH_PLAYER, True)
        self.__shoot_r = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\shoot.png", 10, 1, HIGH_PLAYER, WIDTH_PLAYER)
        self.__shoot_l = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\shoot.png", 10, 1, HIGH_PLAYER, WIDTH_PLAYER, True)
        self.__death_r = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\death.png", 10, 1, HIGH_PLAYER, WIDTH_PLAYER)
        self.__death_l = Auxiliar.getSurfaceFromSpriteSheet(r"assets\graphics\player\death.png", 10, 1, HIGH_PLAYER, WIDTH_PLAYER, True)
        self.__frame = 0
        self.__animation = self.__still_r
        self.__image = self.__animation[self.__frame]
        self.__rect = self.__image.get_rect()
        
        self.__rect.x = pos_x  
        self.__rect.y = pos_y  
        self.__move_x = 0 
        self.__move_y = 0  
        self.__direction = DIRECTION_R

        self.__speed_walk = speed_walk
        self.__life = life
        self.__flag_life = True
        self.__score = 0
        self.__gravity = gravity
        self.__jump_power = jump_power
        self.__jump_height = jump_height
        self.__is_jump = False
        self.__radius = 15
        self.__ground_gravity = ground_gravity
        
        self.__bullet_group = pygame.sprite.Group()
        self.__time_bullet = 0
        self.__time_bullet_rate_ms = 200

        self.__tiempo_transcurrido_animacion = 0
        self.__frame_animacion_rate_ms = frame_animacion_rate_ms
        self.__tiempo_transcurrido_movimiento = 0
        self.__frame_movimiento_rate_ms = frame_movimiento_rate_ms
        self.__disparo = pygame.mixer.Sound(PATH_DISPARO_SOUND)
       

    @property
    def rect(self):
        return self.__rect
    
    @property
    def life(self):
        return self.__life
    
    @life.setter
    def life(self, life):
        self.__life = life

    @property
    def score(self):
        return self.__score
    
    @score.setter
    def score(self, score):
        self.__score = score
    
    @property
    def flag_life(self):
        return self.__flag_life
    
    @property
    def bullet_group(self):
        return self.__bullet_group
    
    @property
    def animation(self):
        return self.__animation
    
    @animation.setter
    def animation(self, animation):
        self.__animation = animation
    
    @property
    def radius(self):
        return self.__radius

    @property
    def is_collision_platform(self):
        return self.__is_collision_platform

    @property
    def rect_ground_collition(self):
        return self.__rect_ground_collition

    @rect_ground_collition.setter
    def rect_ground_collition(self, rect_ground_collition):
        self.__rect_ground_collition = rect_ground_collition

    @property
    def direction(self):
        return self.__direction
    

    def cooldown_ready_to_action(self):
        curent_time = pygame.time.get_ticks()
        return curent_time - self.__time_bullet >= self.__time_bullet_rate_ms
    
    def create_bullet(self):
        bullet = Bullet(self.__rect.centerx, self.__rect.centery, self.__direction, r"assets\graphics\player\bullet_player.png")
        return self.__bullet_group.add(bullet)
    
    def still(self):
        if self.__animation != self.__still_r and self.__animation != self.__still_l:
            if self.__direction == DIRECTION_R:
                self.animation = self.__still_r   
            else:
                self.animation = self.__still_l
            self.__move_x = 0
            self.__move_y = 0
            self.__frame = 0
            

    def walk(self,direction):
        if self.__direction != direction or (self.__animation != self.__walk_r and self.__animation != self.__walk_l):
            self.__frame = 0
            self.__direction = direction
            if self.__direction == DIRECTION_R:
                self.__move_x = self.__speed_walk
                self.__animation = self.__walk_r
            else:
                self.__move_x = -self.__speed_walk
                self.__animation = self.__walk_l
            
    def jump(self):
        self.__is_jump = True
        if self.__direction == DIRECTION_R:
            self.__move_x = 10
            self.__animation = self.__jump_r
        else:
            self.__move_x -= 10
            self.__animation = self.__jump_l
        self.__frame = 0
        
        
    def shoot(self):
        if self.__direction == DIRECTION_R:
            self.__animation = self.__shoot_r   
        else:
            self.__animation = self.__shoot_l
        self.__frame = 0
        if self.cooldown_ready_to_action():
            self.create_bullet()
            self.__time_bullet = pygame.time.get_ticks()
    

    def death(self):
        if self.__life > 0:
            self.__life -= 1
        else:
            if self.__direction == DIRECTION_R:
                self.__animation = self.__death_r
            else:
                self.__animation = self.__death_l
            self.__flag_life = False
            self.__move_x = 0 
            self.__move_y = 0
        return self.__flag_life


    def keyboard_events(self, teclas_presionadas):
        if self.__flag_life:
            if not teclas_presionadas[pygame.K_LEFT] and not teclas_presionadas[pygame.K_RIGHT]:
                self.still()
            if teclas_presionadas[pygame.K_LEFT] and teclas_presionadas[pygame.K_RIGHT]:
                self.still()
            elif teclas_presionadas[pygame.K_LEFT] and not teclas_presionadas[pygame.K_RIGHT]:
                self.walk(DIRECTION_L)
            elif not teclas_presionadas[pygame.K_LEFT] and teclas_presionadas[pygame.K_RIGHT]:
                self.walk(DIRECTION_R)
            if teclas_presionadas[pygame.K_SPACE]:
                self.jump()
            if teclas_presionadas[pygame.K_f] and not teclas_presionadas[pygame.K_LEFT] and not teclas_presionadas[pygame.K_RIGHT]:
                self.__disparo.play()
                self.shoot()


    def screen_limits(self):
        if self.__rect.x < 0:
            self.__rect.x = 0
        elif self.__rect.x > WIDTH_WINDOW - self.__rect.width:
            self.__rect.x = WIDTH_WINDOW - self.__rect.width

        if self.__rect.y < 0:
            self.__rect.y = 0
        elif self.__rect.y > HIGH_WINDOW - self.__rect.height:
            self.__rect.y = HIGH_WINDOW - self.__rect.height
    

    def motion(self,delta_ms,platforms_list):
        self.__rect_ground_collition = pygame.Rect(self.__rect.x + self.__rect.w / 4, (self.__rect.y + self.__rect.h - GROUND_RECT_H),self.__rect.w / 2,GROUND_RECT_H)
        self.__tiempo_transcurrido_movimiento += delta_ms
        if self.__tiempo_transcurrido_movimiento >= self.__frame_movimiento_rate_ms:
            self.__tiempo_transcurrido_movimiento = 0
            self.__rect.x += self.__move_x
            self.__rect.y += self.__move_y

        if not self.is_on_platform(platforms_list):
            self.__rect.y += self.__gravity
        
        if self.__is_jump:
            if self.__rect.y > self.__jump_height:
                self.__rect.y -= self.__jump_power
                self.__is_jump = False
            

    def is_on_platform(self,platforms_list):
        retorno = False
        if self.__rect.y >= self.__ground_gravity:
            retorno = True
        else:
            for platform in platforms_list:
                if self.__rect_ground_collition.colliderect(platform.rect_ground_collition):
                    retorno = True
                    break
        return retorno

        
    def animations(self,delta_ms):
        self.__tiempo_transcurrido_animacion += delta_ms
        if self.__tiempo_transcurrido_animacion >= self.__frame_animacion_rate_ms:
            self.__tiempo_transcurrido_animacion = 0
            if self.__flag_life:
                if self.__frame < len(self.__animation) - 1:
                    self.__frame += 1
                else:
                    self.__frame = 0
            else:
                if self.__frame < len(self.__animation) - 1:
                    self.__frame += 1
    

    def update(self,delta_ms,screen,platforms_list):
        self.screen_limits()
        self.motion(delta_ms,platforms_list)
        self.animations(delta_ms)
        self.__bullet_group.update()
        self.__bullet_group.draw(screen)
    
            
    def draw(self,screen):
        if DEBUG:
            pygame.draw.rect(screen,(255,0,0),self.__rect)
            pygame.draw.circle(screen, (0, 0, 255), self.__rect.center, self.__radius)
            pygame.draw.rect(screen,(0, 0, 255),self.__rect_ground_collition)
        self.__image = self.__animation[self.__frame]
        screen.blit(self.__image,self.__rect)
    
            
        
      
        