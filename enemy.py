import pygame
from constants import (DIRECTION_L,DIRECTION_R,WIDTH_ENEMY,HIGH_ENEMY,DEBUG,open_configs,PATH_DISPARO_SOUND)
from volume import Volume
from auxiliar import Auxiliar  
from bullet import Bullet

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,left_limit_x,right_limit_x,speed_walk,life,frame_animation_rate_ms,frame_motion_rate_ms,name_stage):
        super().__init__()
        self.__configuration = open_configs().get(name_stage)
        self.__configuration_enemy = self.__configuration.get("enemy")
        self.__load_image_enemy = self.__configuration_enemy.get("enemy_path_image")
        self.__shoot =  self.__load_image_enemy[0]
        self.__death =  self.__load_image_enemy[1]
        self.__shoot_r = Auxiliar.getSurfaceFromSpriteSheet(self.__shoot["enemy_img_shoot"],self.__shoot["columns"],self.__shoot["rows"],HIGH_ENEMY,WIDTH_ENEMY)
        self.__shoot_l = Auxiliar.getSurfaceFromSpriteSheet(self.__shoot["enemy_img_shoot"],self.__shoot["columns"],self.__shoot["rows"],HIGH_ENEMY,WIDTH_ENEMY,True)
        self.__death_r = Auxiliar.getSurfaceFromSpriteSheet(self.__death["enemy_img_death"],self.__death["columns"],self.__death["rows"],HIGH_ENEMY,WIDTH_ENEMY)
        self.__death_l = Auxiliar.getSurfaceFromSpriteSheet(self.__death["enemy_img_death"],self.__death["columns"],self.__death["rows"],HIGH_ENEMY,WIDTH_ENEMY,True)
        self.__frame = 0
        self.__animation = self.__shoot_l
        self.__image = self.__animation[self.__frame]
        self.__rect = self.__image.get_rect()

        self.__rect.x = pos_x
        self.__rect.y = pos_y
        self.__left_limit_x = left_limit_x
        self.__right_limit_x = right_limit_x
        self.__speed_walk = speed_walk
        self.__direction = DIRECTION_L

        self.__life = life
        self.__flag_life = True
        self.__flag_shoot = True
        self.__radius = 20
        
        self.__time_elapsed_animation = 0 
        self.__frame_animation_rate_ms = frame_animation_rate_ms
        self.__time_elapsed_motion = 0
        self.__frame_motion_rate_ms = frame_motion_rate_ms
        
        self.__bullet_group = pygame.sprite.Group()
        self.__time_bullet = 0
        self.__time_bullet_rate_ms = 2500
    

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
    
    def sound_disparo(self):
        self.__disparo = Volume(PATH_DISPARO_SOUND)
        self.__disparo.play_sound()
    
    
    def cooldown_ready_to_action(self):
        curent_time = pygame.time.get_ticks()
        return curent_time - self.__time_bullet >= self.__time_bullet_rate_ms
    
        
    def create_bullet(self):
        if self.__direction == DIRECTION_L:
            bullet_direction = DIRECTION_R
        else:
            bullet_direction = DIRECTION_L
        bullet = Bullet(self.__rect.centerx, self.__rect.centery, bullet_direction, r"assets\graphics\enemy\bullet\bullet_enemy.png")
        return self.__bullet_group.add(bullet)


    def shoot(self):
            if self.__flag_shoot:
                #self.sound_disparo()
                if self.__rect.right > self.__right_limit_x:
                    self.__animation = self.__shoot_l
                    self.__direction = DIRECTION_L
                elif self.__rect.left < self.__left_limit_x:
                    self.__animation = self.__shoot_r
                    self.__direction = DIRECTION_R

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
            self.__flag_shoot = False
            self.__flag_life = False
            self.__speed_walk = 0 


    def animations(self,delta_ms):
        self.__time_elapsed_animation += delta_ms
        if self.__time_elapsed_animation >= self.__frame_animation_rate_ms:
            self.__time_elapsed_animation = 0
            if self.__flag_life:
                if self.__frame < len(self.__animation) - 1:
                    self.__frame += 1
                else:
                    self.__frame = 0
            else:
                if self.__frame < len(self.__animation) - 1:
                    self.__frame += 1
            

    
    def motion(self, delta_ms):
        self.__time_elapsed_motion += delta_ms
        if self.__time_elapsed_motion >= self.__frame_motion_rate_ms:
            self.__time_elapsed_motion = 0
            self.__rect.x += self.__speed_walk * self.__direction
        

            
    def update(self,delta_ms,screen):
        self.motion(delta_ms)
        self.animations(delta_ms)
        self.__bullet_group.update()
        self.__bullet_group.draw(screen)
        self.shoot()
        
        
           
    def draw(self, screen):
        if DEBUG:
            pygame.draw.rect(screen,(255,0,0),self.__rect)
            pygame.draw.circle(screen, (0, 0, 255), self.__rect.center,self.__radius)
        self.__image = self.__animation[self.__frame]
        screen.blit(self.__image,self.__rect)
        
        
       
        
