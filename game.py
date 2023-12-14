import pygame   
from stage import Stage
from button import Button
from create_screen import CreateScreen
from constants import (FPS,WIDTH_SCREEN_PAUSE,HIGH_SCREEN_PAUSE,
                       WIDTH_WINDOW,HIGH_WINDOW,
                       WIDTH_BUTTON_MAIN_MENU,HIGH_BUTTON_MAIN_MENU,
                       PATH_SCREEN_PAUSE,PATH_BUTTON_CONTINUE,PATH_BUTTON_QUIT,
                       PATH_MISSION_COMPLETE_SOUND,PATH_IMAGE_MISION_COMPLETE,
                       WIDTH_IMAGE_MISION_COMPLETE,HIGH_IMAGE_MISION_COMPLETE,
                       PATH_VICTORY_SOUND,PATH_VICTORY_IMAGE,
                       PATH_GAME_OVER_SOUND,PATH_GAME_OVER_IMAGE)

class Game():
    def __init__(self,screen:pygame.surface.Surface):
        pygame.init()
        self.__game_screen = screen
        pygame.display.set_caption("Metal Slug")
        
        self.__running_game = True
        self.__game_time_limit = 1000
        self.__number_of_levels = 3
        self.__current_stage = 1
        self.__paused = False

        self.__sound_mision_complete = pygame.mixer.Sound(PATH_MISSION_COMPLETE_SOUND)
        self.__sound_victory = pygame.mixer.Sound(PATH_VICTORY_SOUND)
        self.__sound_game_over = pygame.mixer.Sound(PATH_GAME_OVER_SOUND)

    @property
    def current_stage(self):
        return self.__current_stage

    @current_stage.setter
    def current_stage(self, current_stage):
         self.__current_stage = current_stage

    
    def game_over(self):
        self.__image_game_over = pygame.image.load(PATH_GAME_OVER_IMAGE).convert_alpha()
        self.__game_over = pygame.transform.scale(self.__image_game_over,(WIDTH_WINDOW,HIGH_WINDOW))
        self.__game_screen.blit(self.__game_over,(0,0))
        self.__sound_game_over.play()
        pygame.display.flip() 
        pygame.time.delay(7000)
        self.__current_game_time = 0

    def game_win(self):
        self.__image_game_win = pygame.image.load(PATH_VICTORY_IMAGE).convert_alpha()
        self.__game_win = pygame.transform.scale(self.__image_game_win,(WIDTH_WINDOW,HIGH_WINDOW))
        self.__game_screen.blit(self.__game_win,(0,0))
        self.__sound_victory.play()
        pygame.display.flip() 
        pygame.time.delay(7000)
        self.__current_game_time = 0

    def transition_mision_complete(self):
        self.__image_mision_complete = pygame.image.load(PATH_IMAGE_MISION_COMPLETE).convert_alpha()
        self.__mision_complete = pygame.transform.scale(self.__image_mision_complete,
                                                        (WIDTH_IMAGE_MISION_COMPLETE,HIGH_IMAGE_MISION_COMPLETE))
        self.__x = (WIDTH_WINDOW - WIDTH_IMAGE_MISION_COMPLETE) // 2
        self.__y = (HIGH_WINDOW - HIGH_IMAGE_MISION_COMPLETE) // 2
        self.__game_screen.blit(self.__mision_complete,(self.__x,self.__y))
        self.__sound_mision_complete.play()
        pygame.display.flip() 
        pygame.time.delay(7000)
        self.__current_game_time = 0

    

    def levels(self, current_time):
        if self.__current_stage <= self.__number_of_levels:
            if self.__stage.flag_enemies_eliminate:
                self.__current_stage += 1
                if self.__current_stage <= self.__number_of_levels:
                    self.__stage = Stage(self.__game_screen, stage=f"stage_{self.__current_stage}")
                    self.transition_mision_complete()
                else:
                    self.game_win()
                    self.__running_game = False
            elif self.__stage.player.life == 0 or current_time >= self.__game_time_limit:
                self.game_over()
                self.__running_game = False

                

    def pause_screen(self):
        self.__pause_screen = CreateScreen(path=PATH_SCREEN_PAUSE,width=WIDTH_SCREEN_PAUSE,high=HIGH_SCREEN_PAUSE)
        self.__pause_screen.draw(self.__game_screen)


    def pause_buttons_generator(self):
        self.__button_contiue = Button(pos_x=525,pos_y=250,path=PATH_BUTTON_CONTINUE,
                                       width=WIDTH_BUTTON_MAIN_MENU,high=HIGH_BUTTON_MAIN_MENU)
        self.__button_quit = Button(pos_x=525,pos_y=350,path=PATH_BUTTON_QUIT,
                                    width=WIDTH_BUTTON_MAIN_MENU,high=HIGH_BUTTON_MAIN_MENU)
        self.__buttons_screen_pause = [self.__button_contiue,self.__button_quit]
        return self.__buttons_screen_pause
    

    def draw_button(self):
        for buttons in self.pause_buttons_generator():
            buttons.draw(self.__game_screen)
    

    def keyboard_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.__paused = not self.__paused
                if self.__paused:
                    self.pause_screen()
                    self.draw_button()


    def mouse_events(self, event, mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.__button_contiue.mouse_over_button(mouse_pos, mouse_button=0):  
                self.__paused = False
            elif self.__button_quit.mouse_over_button(mouse_pos, mouse_button=0):
                pygame.display.set_caption("Main Menu")
                self.__running_game = False


    def run_game(self):
        self.__clock = pygame.time.Clock()
        self.__stage = Stage(self.__game_screen, stage=f"stage_{self.__current_stage}")


        while self.__running_game:
            self.__current_game_time = pygame.time.get_ticks() // 1000
            self.__teclas_presionadas = pygame.key.get_pressed()
            self.__mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                self.keyboard_events(event)
                self.mouse_events(event, self.__mouse_pos)
                if event.type == pygame.QUIT:
                    self.__running_game = False
                              
            if not self.__paused:
                
                self.__stage.player.keyboard_events(self.__teclas_presionadas)
                self.levels(self.__current_game_time)
                    
                delta_ms = self.__clock.tick(FPS)
                self.__stage.run_stage(delta_ms, self.__current_game_time)
            else:
                self.__paused

            pygame.display.flip()
           
        
       

