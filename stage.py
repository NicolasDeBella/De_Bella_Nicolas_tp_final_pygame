import pygame
from player import Player
from enemy import Enemy
from score import Score
from life import Life
from trap import Trap
from plataforma import Platform
from constants import (open_configs,WIDTH_WINDOW,HIGH_WINDOW,DIRECTION_R,PATH_COLLISION_SOUND,PATH_METAL_SLUG_SCREAM_SOUND)


class Stage:
    def __init__(self,screen: pygame.surface.Surface,stage:str):
        self.__stage = stage
        self.__configuration = open_configs().get(stage)
        self.__screen = screen
        self.__background = self.__configuration.get("background_img")

        self.__player_configuration = self.__configuration.get("player")
        self.__player_coord = self.__player_configuration.get("coord_player")
        self.player = Player(
            pos_x = self.__player_coord.get("pos_x"),
            pos_y = self.__player_coord.get("pos_y"),
            speed_walk = self.__player_configuration.get("player_speed"),
            gravity = self.__player_configuration.get("gravity"),
            jump_power = self.__player_configuration.get("jump_power"),
            jump_height = self.__player_configuration.get("jump_height"),
            life = self.__player_configuration.get("life"),
            ground_gravity = self.__player_configuration.get("ground_gravity"),
            frame_animacion_rate_ms = self.__player_configuration.get("frame_animation_rate_ms"),
            frame_movimiento_rate_ms = self.__player_configuration.get("frame_motion_rate_ms")
        )

        self.__enemy_configuration = self.__configuration.get("enemy")
        self.__enemies_coord = self.__enemy_configuration.get("coord_enemies")
        self.__enemies_limits_coord_x = self.__enemy_configuration.get("coord_x_limits")
        self.__flag_enemies_eliminate = False
        self.__list_dead_enemies = []
        self.__enemies_group = pygame.sprite.Group()
        
        self.__score_configuration = self.__configuration.get("score")
        self.__score_coord = self.__score_configuration.get("coord_score")
        self.__score_group = pygame.sprite.Group()
       
        self.__life_configuration = self.__configuration.get("life")
        self.__life_coord = self.__life_configuration.get("coord_life")
        self.__life_group = pygame.sprite.Group()
        
        self.__trap_group = pygame.sprite.Group()

        self.__platform_group = pygame.sprite.Group()

        self.__collision_sound = pygame.mixer.Sound(PATH_COLLISION_SOUND)
        self.__scream_sound = pygame.mixer.Sound(PATH_METAL_SLUG_SCREAM_SOUND)

        self.generate_enemies()
        self.generate_score()
        self.generate_life()
        self.generator_trap()
        self.generator_platform()

    @property
    def score_counter(self):
        return self.__score_counter

    @property
    def flag_enemies_eliminate(self):
        return self.__flag_enemies_eliminate
    
    @flag_enemies_eliminate.setter
    def flag_enemies_eliminate(self, flag_enemies_eliminate):
        self.__flag_enemies_eliminate = flag_enemies_eliminate


    def generate_background(self):
        self.__background_image = pygame.image.load(self.__background)
        self.__background_image = pygame.transform.scale(self.__background_image, (WIDTH_WINDOW, HIGH_WINDOW))
        self.__screen.blit(self.__background_image,self.__background_image.get_rect())

    def generate_enemies(self):
        for coord, limits_x in zip(self.__enemies_coord, self.__enemies_limits_coord_x):
            enemy = Enemy(
                pos_x = coord.get("coord_x"),
                pos_y = coord.get("coord_y"),
                left_limit_x = limits_x.get("left_limit_x"),
                right_limit_x = limits_x.get("right_limit_x"),
                speed_walk = self.__enemy_configuration.get("enemy_speed"),
                life = self.__enemy_configuration.get("life"),
                frame_animation_rate_ms = self.__enemy_configuration.get("frame_animation_rate_ms"),
                frame_motion_rate_ms = self.__enemy_configuration.get("frame_motion_rate_ms"),
                name_stage=self.__stage
            )
            self.__enemies_group.add(enemy)
            

    def generate_score(self):
        for coord in self.__score_coord:
            score = Score(pos_x = coord.get("pos_x"),
                          pos_y = coord.get("pos_y"))
            self.__score_group.add(score)

    def generate_life(self):
        for coord in self.__life_coord:
            life = Life(pos_x = coord.get("pos_x"),
                        pos_y = coord.get("pos_y"))
            self.__life_group.add(life)
    

    def generator_trap(self):
        if "trap" in self.__configuration:
            self.__trap_configuration = self.__configuration.get("trap")
            self.__trap_coord = self.__trap_configuration.get("coord_trap")
            
            for coord in self.__trap_coord:
                trap = Trap(pos_x = coord.get("pos_x"),
                            pos_y = coord.get("pos_y"))
                self.__trap_group.add(trap)


    def generator_platform(self):
        if "platform" in self.__configuration:
            self.__platform_configuration = self.__configuration.get("platform")
            self.__platform_coord = self.__platform_configuration.get("coord_platform")
            self.__platform_size = self.__platform_configuration.get("size_platform")
            
            for coord, size in zip(self.__platform_coord, self.__platform_size):
                platform = Platform(
                    pos_x=coord.get("pos_x"),
                    pos_y=coord.get("pos_y"),
                    high=size.get("high"),
                    width=size.get("width")
                )
                self.__platform_group.add(platform)
                          

    def collision_between_player_and_score(self):
            collision_score = pygame.sprite.spritecollide(self.player,self.__score_group,True,pygame.sprite.collide_circle)
            if collision_score:
                self.__collision_sound.play()
                self.player.score += 500
            

    def collision_between_player_and_life(self):
            collision_life = pygame.sprite.spritecollide(self.player,self.__life_group,True,pygame.sprite.collide_circle)
            if collision_life:
                self.__collision_sound.play()
                self.player.life += 1
                
    
    def collision_between_player_and_trap(self):
            collision_trap = pygame.sprite.spritecollide(self.player,self.__trap_group,False,pygame.sprite.collide_circle)
            if collision_trap:
                self.player.death()
                

    def collision_between_the_player_and_the_enemys_bullet(self):
        if self.player.flag_life:
            for enemy in self.__enemies_group:
                collisions = pygame.sprite.spritecollide(self.player,enemy.bullet_group,True,pygame.sprite.collide_circle)
                if collisions:
                    self.player.death()
                    if self.player.life < 0:
                         self.__scream_sound.play()
        else:
            for enemy in self.__enemies_group:
                pygame.sprite.spritecollide(self.player, enemy.bullet_group,False,pygame.sprite.collide_circle)

             
    def collision_between_the_enemy_and_the_player_bullet(self):
        for enemy in self.__enemies_group:
            if enemy.flag_life:
                collisions = pygame.sprite.spritecollide(enemy,self.player.bullet_group,True,pygame.sprite.collide_circle)
                if collisions:
                    enemy.death()

                if enemy.flag_life == False:
                    self.__list_dead_enemies.append(enemy)
                    
                    if len(self.__list_dead_enemies) == len(self.__enemies_group):
                        self.__flag_enemies_eliminate = True
                        self.__list_dead_enemies = []
        

    def collision_between_the_player_and_the_platforms(self):
        for platform in self.__platform_group:
            if self.player.rect_ground_collition.colliderect(platform.rect_ground_collition):
                if self.player.rect_ground_collition.top >= platform.rect_ground_collition.bottom:
                    print("Colisión plataforma y jugador")
                    self.player.rect_ground_collition.y = platform.rect_ground_collition.bottom

    
    def handle_collisions(self):
        self.collision_between_the_player_and_the_enemys_bullet()
        self.collision_between_the_enemy_and_the_player_bullet()
        self.collision_between_player_and_life()
        self.collision_between_player_and_score()
        self.collision_between_player_and_trap()
        self.collision_between_the_player_and_the_platforms()
        
        
        
        
    def render_data(self,current_time):
        font = pygame.font.Font(None, 36)  
        lives_text = font.render(f'Life: {self.player.life}', True, (255, 255, 255))  
        self.__screen.blit(lives_text, (10, 10))  

        time_text = font.render(f'Time: {current_time}', True, (255, 255, 255))
        self.__screen.blit(time_text, (10, 40))  

        font = pygame.font.Font(None, 36)  
        score_text = font.render(f'Score: {self.player.score}', True, (255, 255, 255))  
        self.__screen.blit(score_text, (10, 70))  


    def update_score(self,delta_ms):
        for score in self.__score_group:
            score.update(delta_ms)
            score.draw(self.__screen)
    
    def update_life(self,delta_ms):
        for life in self.__life_group:
            life.update(delta_ms)
            life.draw(self.__screen)
    
    def update_enemy(self,delta_ms):
        for enemy in self.__enemies_group:
            enemy.update(delta_ms,self.__screen)
            enemy.draw(self.__screen)
    
    def update_trap(self,delta_ms):
        for trap in self.__trap_group:
            trap.update(delta_ms)
            trap.draw(self.__screen)

    def update_platform(self):
        for platform in self.__platform_group:
            platform.draw(self.__screen)


    def run_stage(self,delta_ms,current_time):
        self.generate_background()
        self.render_data(current_time)
        self.update_platform()
        self.update_life(delta_ms)
        self.update_score(delta_ms)
        self.update_trap(delta_ms)
        self.update_enemy(delta_ms)
        self.player.update(delta_ms,self.__screen,self.__platform_group)
        self.player.draw(self.__screen)
        self.handle_collisions()
        
        
        
        
        
        

