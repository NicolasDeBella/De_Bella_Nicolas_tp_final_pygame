import pygame   
from constants import (WIDTH_WINDOW,HIGH_WINDOW,FPS)
from stage import Stage


class Game(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.__current_stage = 1
        self.__time_limit_level = 20
     
        
    def levels(self,screen,time):
        if self.__current_stage <= 3:  # Cambia este valor al número total de niveles
            if self.__stage.flag_enemies_eliminate:
                print(f'¡Has superado el nivel {self.__current_stage}!')
                
                self.__current_stage += 1
                self.__stage = Stage(screen, stage=f"stage_{self.__current_stage}")

            elif self.__stage.player.life == 0 or time >= self.__time_limit_level:
                
                print("perdiste")
                return True
                
        

    def run_game(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((WIDTH_WINDOW, HIGH_WINDOW))
        self.__running_game = True
        self.__clock = pygame.time.Clock()
        
        self.__stage = Stage(self.__screen, stage=f"stage_{self.__current_stage}")
        
        while self.__running_game:
            self.__start_time = pygame.time.get_ticks() // 1000
            teclas_presionadas = pygame.key.get_pressed()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Estoy CERRANDO el JUEGO')
                    self.__running_game = False
                    break              
            
            self.__stage.player.keyboard_events(teclas_presionadas) 
            
            if self.levels(self.__screen,self.__start_time):
                break
            
            delta_ms = self.__clock.tick(FPS)
            self.__stage.run_stage(delta_ms)
            print(self.__start_time)
            pygame.display.flip()

        pygame.quit()
        

game = Game()
game.run_game()
