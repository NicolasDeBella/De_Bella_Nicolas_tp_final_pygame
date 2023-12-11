import pygame   
from constants import (FPS)
from stage import Stage

class Game():
    def __init__(self,screen:pygame.surface.Surface):
        self.__game_screen = screen
        
        
        
    def levels(self,current_time):
        if self.__current_stage <= self.__number_of_levels:  
            if self.__stage.flag_enemies_eliminate:
                print(f'¡Has superado el nivel {self.__current_stage}!')
                self.__current_stage += 1
                self.__stage = Stage(self.__game_screen, stage=f"stage_{self.__current_stage}")
            elif self.__stage.player.life == 0 and current_time >= self.__game_time_limit:
                print("perdiste")
                self.__running_game = False
      
                
        
    
    def run_game(self):
        pygame.init()
        self.__game_screen 
        pygame.display.set_caption("Metal Slug")
        
        self.__running_game = True
        self.__number_of_levels = 3 
        self.__current_stage = 1
        self.__game_time_limit = 200
    
        self.__stage = Stage(self.__game_screen, stage=f"stage_{self.__current_stage}")
        self.__clock = pygame.time.Clock()
        
        while self.__running_game:

            teclas_presionadas = pygame.key.get_pressed()
            self.__current_game_time = pygame.time.get_ticks() // 1000
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running_game = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.display.set_caption("Main Menu")
                        self.__running_game = False
                        return

            self.__stage.player.keyboard_events(teclas_presionadas)
            self.levels(self.__current_game_time)
                
            delta_ms = self.__clock.tick(FPS)
            self.__stage.run_stage(delta_ms, self.__current_game_time)

            pygame.display.flip()
        pygame.quit()

        

