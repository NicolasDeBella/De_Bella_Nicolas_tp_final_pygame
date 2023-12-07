import pygame
from player import Player
from enemy import Enemy
from score import Score
from life import Life
from constants import *


class Stage:
    def __init__(self,screen: pygame.surface.Surface,stage:str):
        
        self.__configuration = open_configs().get(stage)
        self.__screen = screen
        self.__background = self.__configuration.get("background_img")

        self.__player_configuration = self.__configuration.get("player")
        self.__player_coord = self.__player_configuration.get("coord_player")
        self.player = Player(
            pos_x = self.__player_coord["pos_x"],
            pos_y = self.__player_coord["pos_y"],
            speed_walk = self.__player_configuration["player_speed"],
            gravity = self.__player_configuration["gravity"],
            y_speed = self.__player_configuration["Y_speed"],
            life = self.__player_configuration["life"],
            frame_animacion_rate_ms = self.__player_configuration["frame_animation_rate_ms"],
            frame_movimiento_rate_ms = self.__player_configuration["frame_motion_rate_ms"]
        )

        self.__enemy_configuration = self.__configuration.get("enemy")
        self.__enemies_coord = self.__enemy_configuration.get("coord_enemies")
        self.__max_enemies = self.__enemy_configuration.get("max_enemies")
        self.__flag_enemies_eliminate = False
        self.__list_dead_enemies = []
        self.__enemies_group = pygame.sprite.Group()
        
     
        self.__score_configuration = self.__configuration.get("score")
        self.__score_coord = self.__score_configuration.get("coord_score")
        self.__score_group = pygame.sprite.Group()
       

        self.__life_configuration = self.__configuration.get("life")
        self.__life_coord = self.__life_configuration.get("coord_life")
        self.__life_group = pygame.sprite.Group()
            
        self.generate_enemies()
        self.generate_score()
        self.generate_life()

    @property
    def flag_enemies_eliminate(self):
        return self.__flag_enemies_eliminate
    
    @flag_enemies_eliminate.setter
    def flag_enemies_eliminate(self, flag_enemies_eliminate):
        self.__flag_enemies_eliminate = flag_enemies_eliminate
    
    def generate_background(self):
        self.background_image = pygame.image.load(self.__background)
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH_WINDOW, HIGH_WINDOW))
        self.__screen.blit(self.background_image,self.background_image.get_rect())


    def generate_enemies(self):
        for coord in self.__enemies_coord:
            enemy = Enemy(
                pos_x = coord["coord_x"],
                pos_y = coord["coord_y"],
                left_limit_x = self.__enemy_configuration["left_limit_x"],
                right_limit_x = self.__enemy_configuration["right_limit_x"],
                speed_walk = self.__enemy_configuration["enemy_speed"],
                life = self.__enemy_configuration["life"],
                frame_animation_rate_ms = self.__enemy_configuration["frame_animation_rate_ms"],
                frame_motion_rate_ms = self.__enemy_configuration["frame_motion_rate_ms"]
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
                          
                                            
    
    def collision_between_player_and_score(self):
            collision_score = pygame.sprite.spritecollide(self.player,self.__score_group,True,pygame.sprite.collide_circle)
            if collision_score:
                self.player.score += 500
    
    def collision_between_player_and_life(self):
            collision_life = pygame.sprite.spritecollide(self.player,self.__life_group,True,pygame.sprite.collide_circle)
            if collision_life:
                self.player.life += 1


    # def collision_between_player_and_enemy(self):
    #     collision = pygame.sprite.spritecollide(self.player,self.enemies_group,False,pygame.sprite.collide_circle)
    #     if collision:
    #         self.player.death()


    def collision_between_the_player_and_the_enemys_bullet(self):
        if self.player.flag_life:
            for enemy in self.__enemies_group:
                collisions = pygame.sprite.spritecollide(self.player,enemy.bullet_group,True,pygame.sprite.collide_circle)
                if collisions:
                    self.player.death()
        else:
            for enemy in self.__enemies_group:
                pygame.sprite.spritecollide(self.player, enemy.bullet_group,False,pygame.sprite.collide_circle)

             
    def collision_between_the_enemy_and_the_player_bullet(self):
    
        for enemy in self.__enemies_group:
            if enemy.flag_life:
                collisions = pygame.sprite.spritecollide(enemy, self.player.bullet_group, True, pygame.sprite.collide_circle)
                if collisions:
                    enemy.death()
                    
        if enemy.life == 0:
            self.__list_dead_enemies.append(enemy)
   
        if len(self.__list_dead_enemies) == self.__max_enemies:
            self.__flag_enemies_eliminate = True
            self.__list_dead_enemies = []
                
            
        
        

    def handle_collisions(self):
        #self.collision_between_player_and_enemy()
        #self.collision_between_the_player_and_the_enemys_bullet()
        self.collision_between_the_enemy_and_the_player_bullet()
        self.collision_between_player_and_life()
        self.collision_between_player_and_score()
        
        
    def render_data(self):
        font = pygame.font.Font(None, 36)  
        lives_text = font.render(f'Life: {self.player.life}', True, (255, 255, 255))  
        self.__screen.blit(lives_text, (10, 10))  

        tiempo_actual = pygame.time.get_ticks() // 1000  
        time_text = font.render(f'Time: {tiempo_actual}', True, (255, 255, 255))
        self.__screen.blit(time_text, (10, 40))  

        font = pygame.font.Font(None, 36)  
        score_text = font.render(f'Score: {self.player.score}', True, (255, 255, 255))  
        self.__screen.blit(score_text, (10, 70))  





    def run_stage(self,delta_ms):
        
        self.generate_background()

        for score in self.__score_group:
            score.update(delta_ms)
            score.draw(self.__screen)
        
        for life in self.__life_group:
            life.update(delta_ms)
            life.draw(self.__screen)
        
        for enemy in self.__enemies_group:
            enemy.update(delta_ms,self.__screen)
            enemy.draw(self.__screen)

        self.player.update(delta_ms, self.__screen)
        self.player.draw(self.__screen)

        self.handle_collisions()
        self.render_data()
        
        
        
        
        

