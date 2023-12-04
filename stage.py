import pygame
from player import Player
from enemy import Enemy
from score import Score
from life import Life
from constants import *


class Stage:
    def __init__(self):
        self.player = Player(pos_x=0,pos_y=500,speed_walk=4,gravity=1,y_speed=20,life=3,frame_animacion_rate_ms=80,frame_movimiento_rate_ms=20)
        self.enemies_group = pygame.sprite.Group()
        self.score_group = pygame.sprite.Group()
        self.life_group = pygame.sprite.Group()
        
        coordenadas_x = [500,1000,1500]
        coordenadas_x_score = [500,1000,1400]
        coordenadas_x_life = [300,700,1200]
        # Crear y agregar enemigos con distintas coordenadas x al grupo
        for coord_x in coordenadas_x:
            enemy = Enemy(coord_x,pos_y=475,left_limit_x=0,right_limit_x=WIDTH_WINDOW,speed_walk=3,life=4,frame_animation_rate_ms=80,frame_motion_rate_ms=30)
            self.enemies_group.add(enemy)
        
        for coord_x in coordenadas_x_score:
            score = Score(coord_x,pos_y=400)
            self.score_group.add(score)
        
        for coord_x in coordenadas_x_life:
            life = Life(coord_x,pos_y=400)
            self.life_group.add(life)
    
    
    def collision_between_player_and_score(self):
            collision_score = pygame.sprite.spritecollide(self.player,self.score_group,True,pygame.sprite.collide_circle)
            if collision_score:
                self.player.score += 500
    
    def collision_between_player_and_life(self):
            collision_life = pygame.sprite.spritecollide(self.player,self.life_group,True,pygame.sprite.collide_circle)
            if collision_life:
                self.player.life += 1


    # def collision_between_player_and_enemy(self):
    #     collision = pygame.sprite.spritecollide(self.player,self.enemies_group,False,pygame.sprite.collide_circle)
    #     if collision:
    #         self.player.death()


    def collision_between_the_player_and_the_enemys_bullet(self):
        if self.player.flag_life:
            for enemy in self.enemies_group:
                collisions = pygame.sprite.spritecollide(self.player,enemy.bullet_group,True,pygame.sprite.collide_circle)
                if collisions:
                    self.player.death()
        else:
            for enemy in self.enemies_group:
                pygame.sprite.spritecollide(self.player, enemy.bullet_group,False,pygame.sprite.collide_circle)

             
    def collision_between_the_enemy_and_the_player_bullet(self):
        for enemy in self.enemies_group:
            if enemy.flag_life:
                collisions = pygame.sprite.spritecollide(enemy,self.player.bullet_group,True,pygame.sprite.collide_circle)
                if collisions:
                    enemy.death()
            

    def handle_collisions(self):
        #self.collision_between_player_and_enemy()
        self.collision_between_the_player_and_the_enemys_bullet()
        self.collision_between_the_enemy_and_the_player_bullet()
        self.collision_between_player_and_life()
        self.collision_between_player_and_score()
        
        
    def mostrar_estadisticas(self,screen):
        font = pygame.font.Font(None, 36)  # Puedes ajustar el tamaño de la fuente
        lives_text = font.render(f'Life: {self.player.life}', True, (255, 255, 255))  # Color blanco
        screen.blit(lives_text, (10, 10))  # Puedes ajustar la posición

        tiempo_actual = pygame.time.get_ticks() // 1000  # Convertir a segundos
        time_text = font.render(f'Time: {tiempo_actual}', True, (255, 255, 255))
        screen.blit(time_text, (10, 40))  # Ajusta la posición según sea necesario

        font = pygame.font.Font(None, 36)  # Puedes ajustar el tamaño de la fuente
        score_text = font.render(f'Score: {self.player.score}', True, (255, 255, 255))  # Color blanco
        screen.blit(score_text, (10, 70))  # Puedes ajustar la posición





    def run(self, delta_ms, screen):
        for enemy in self.enemies_group:
            enemy.update(delta_ms,screen)
            enemy.draw(screen)

        self.player.update(delta_ms, screen)
        self.player.draw(screen)
        
        for score in self.score_group:
            score.update(delta_ms)
            score.draw(screen)
        
        for life in self.life_group:
            life.update(delta_ms)
            life.draw(screen)

        self.handle_collisions()
        self.mostrar_estadisticas(screen)
        
        

