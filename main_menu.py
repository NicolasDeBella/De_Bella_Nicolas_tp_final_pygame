import pygame
from game import Game
from button import Button
from create_screen import CreateScreen
from volume import Volume

from constants import (WIDTH_SCREEN_MAIN_MENU,HIGH_SCREEN_MAIN_MENU,WIDTH_WINDOW,HIGH_WINDOW,
                       WIDTH_BUTTON_MAIN_MENU,HIGH_BUTTON_MAIN_MENU,WIDTH_BUTTON_NIVEL_SELECT,HIGH_BUTTON_NIVEL_SELECT,
                       WIDTH_BUTTON_SOUND,HIGH_BUTTON_SOUND,
                       PATH_BACKGROUN_MENU,
                       PATH_BUTTON_PLAY,PATH_BUTTON_LEVEL_SELECT,PATH_BUTTON_QUIT_GAME,PATH_BUTTON_SCORE,PATH_SCREEN_MAIN_MENU,
                       PATH_SCREEN_LEVEL_SELECT,PATCH_LEVEL_1,PATCH_LEVEL_2,PATCH_LEVEL_3,
                       PATCH_SCREEN_SCORE,
                       PATCH_SCREEN_VOLUME,PATCH_BUTTON_SOUND_ON,PATCH_BUTTON_SOUND_OF,
                       PATCH_BUTTON_SETTING_VOLUME,PATCH_BUTTON_LESS,PATCH_BUTTON_FURTHER,
                       PATH_BACKGROUND_SOUND)

class MainMenu():
    def __init__(self):
        pygame.init()
        self.__screen_main_menu = pygame.display.set_mode((WIDTH_WINDOW,HIGH_WINDOW))
        pygame.display.set_caption("Main Menu")

        self.__running_menu = True
        self.__current_screen = "main_menu"

        self.__sound = Volume(path_sound=PATH_BACKGROUND_SOUND)
        self.__sound.play_sound()


    def start_menu_background(self):
        self.__background_main_menu = pygame.image.load(PATH_BACKGROUN_MENU).convert_alpha()
        self.__image_background_menu = pygame.transform.scale(self.__background_main_menu,(WIDTH_WINDOW,HIGH_WINDOW))
        self.__screen_main_menu.blit(self.__image_background_menu,(0,0))
           
    def main_menu_screen(self):
        self.__main_menu_screen = CreateScreen(path=PATH_SCREEN_MAIN_MENU,width=WIDTH_SCREEN_MAIN_MENU,high=HIGH_SCREEN_MAIN_MENU)
        self.__main_menu_screen.draw(self.__screen_main_menu)

    def levels_screen(self):
        self.__levels_screen = CreateScreen(path=PATH_SCREEN_LEVEL_SELECT,width=WIDTH_SCREEN_MAIN_MENU,high=HIGH_SCREEN_MAIN_MENU)
        self.__levels_screen.draw(self.__screen_main_menu)
    
    def score_screen(self):
        self.__score_screen = CreateScreen(path=PATCH_SCREEN_SCORE,width=WIDTH_SCREEN_MAIN_MENU,high=HIGH_SCREEN_MAIN_MENU)
        self.__score_screen.draw(self.__screen_main_menu)
    
    def setting_volume_screen(self):
        self.__setting_volume_screen = CreateScreen(path=PATCH_SCREEN_VOLUME,width=WIDTH_SCREEN_MAIN_MENU,high=HIGH_SCREEN_MAIN_MENU)
        self.__setting_volume_screen.draw(self.__screen_main_menu)

    def main_menu_buttons_generator(self):
        self.__button_play = Button(pos_x=520,pos_y=180,path=PATH_BUTTON_PLAY,width=WIDTH_BUTTON_MAIN_MENU,high=HIGH_BUTTON_MAIN_MENU)
        self.__button_level_select = Button(pos_x=520,pos_y=260,path=PATH_BUTTON_LEVEL_SELECT,
                                            width=WIDTH_BUTTON_MAIN_MENU,high=HIGH_BUTTON_MAIN_MENU)
        self.__button_score = Button(pos_x=520,pos_y=340,path=PATH_BUTTON_SCORE,
                                     width=WIDTH_BUTTON_MAIN_MENU,high=HIGH_BUTTON_MAIN_MENU)
        self.__button_quit_game = Button(pos_x=520,pos_y=475, path=PATH_BUTTON_QUIT_GAME,
                                         width=WIDTH_BUTTON_MAIN_MENU,high=HIGH_BUTTON_MAIN_MENU)
        self.__button_sound_on = Button(pos_x=560,pos_y=415,path=PATCH_BUTTON_SOUND_ON,width=WIDTH_BUTTON_SOUND,high=HIGH_BUTTON_SOUND)
        self.__button_sound_of = Button(pos_x=620,pos_y=415,path=PATCH_BUTTON_SOUND_OF,width=WIDTH_BUTTON_SOUND,high=HIGH_BUTTON_SOUND)
        self.__button_setting_volume = Button(pos_x=680,pos_y=415,path=PATCH_BUTTON_SETTING_VOLUME,width=WIDTH_BUTTON_SOUND,high=HIGH_BUTTON_SOUND)
        
        self.__buttons_main_menu = [
            self.__button_play,
            self.__button_level_select,
            self.__button_score,
            self.__button_quit_game,
            self.__button_sound_on,self.__button_sound_of,self.__button_setting_volume
        ]
        return self.__buttons_main_menu
        
    def levels_buttons_generator(self):
        self.__button_level_1 = Button(pos_x=475,pos_y=180,path=PATCH_LEVEL_1,
                                       width=WIDTH_BUTTON_NIVEL_SELECT,high=HIGH_BUTTON_NIVEL_SELECT)
        self.__button_level_2 = Button(pos_x=665,pos_y=180, path=PATCH_LEVEL_2,
                                       width=WIDTH_BUTTON_NIVEL_SELECT,high=HIGH_BUTTON_NIVEL_SELECT)
        self.__button_level_3 = Button(pos_x=570,pos_y=340, path=PATCH_LEVEL_3,
                                       width=WIDTH_BUTTON_NIVEL_SELECT,high=HIGH_BUTTON_NIVEL_SELECT)
        self.__buttons_screen_levels = [self.__button_level_1,self.__button_level_2,self.__button_level_3]
        return self.__buttons_screen_levels
    
    def setting_volume_buttons_generator(self):
        self.__button_further = Button(pos_x=575,pos_y=400,path=PATCH_BUTTON_FURTHER,width=WIDTH_BUTTON_SOUND,high=HIGH_BUTTON_SOUND)
        self.__button_less = Button(pos_x=675,pos_y=400,path=PATCH_BUTTON_LESS,width=WIDTH_BUTTON_SOUND,high=HIGH_BUTTON_SOUND)
        self.__buttons_screen_setting_volume = [self.__button_further,self.__button_less]
        return self.__buttons_screen_setting_volume
    
    def draw_button(self):
        if self.__current_screen == "main_menu":
            for button in self.main_menu_buttons_generator():
                button.draw(self.__screen_main_menu)
                
        elif self.__current_screen == "levels_screen":
            for button in self.levels_buttons_generator():
                button.draw(self.__screen_main_menu)
        
        elif self.__current_screen == "setting_volume_screen":
            for button in self.setting_volume_buttons_generator():
                button.draw(self.__screen_main_menu)
        
    def draw_screens(self):
        self.start_menu_background()
        if self.__current_screen == "main_menu":
            self.main_menu_screen()
            if self.__sound.sound_status:
                self.__sound.draw_volume_text(self.__screen_main_menu,"Game volume: ON",True)
            else:
                self.__sound.draw_volume_text(self.__screen_main_menu,"Game volume: OFF",True)

        elif self.__current_screen == "levels_screen":
            self.levels_screen()
        elif self.__current_screen == "score_screen":
            self.score_screen()
           
        elif self.__current_screen == "setting_volume_screen":
            self.setting_volume_screen()
            self.__sound.draw_volume_text(self.__screen_main_menu,"Volumen del juego:",on_of=False)  
            
    
    def mouse_events (self,event,mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.__current_screen == "main_menu":
                if self.__button_play.mouse_over_button(mouse_pos, mouse_button=0):
                    self.__game = Game(self.__screen_main_menu)
                    self.__game.run_game()

                elif self.__button_level_select.mouse_over_button(mouse_pos, mouse_button=0):
                    self.__current_screen = "levels_screen"
                
                elif self.__button_score.mouse_over_button(mouse_pos, mouse_button=0):
                    self.__current_screen = "score_screen"
                
                elif self.__button_sound_on.mouse_over_button(mouse_pos, mouse_button=0):
                    self.__sound.play_sound()

                elif self.__button_sound_of.mouse_over_button(mouse_pos, mouse_button=0):
                    self.__sound.stop_sound()
                    
                elif self.__button_setting_volume.mouse_over_button(mouse_pos, mouse_button=0):
                    self.__current_screen = "setting_volume_screen"
                    
                elif self.__button_quit_game.mouse_over_button(mouse_pos, mouse_button=0):
                    self.__running_menu = False
                    print("SALISTE DEL JUEGO")

            elif self.__current_screen == "levels_screen":
                if self.__button_level_1.mouse_over_button(mouse_pos, mouse_button=0):
                    self.__game = Game(self.__screen_main_menu)
                    self.__game.current_stage=1
                    self.__game.run_game()

                elif self.__button_level_2.mouse_over_button(mouse_pos, mouse_button=0):
                    self.__game = Game(self.__screen_main_menu)
                    self.__game.current_stage=2
                    self.__game.run_game()

                elif self.__button_level_3.mouse_over_button(mouse_pos, mouse_button=0):
                    self.__game = Game(self.__screen_main_menu)
                    self.__game.current_stage=3
                    self.__game.run_game()
            
            elif self.__current_screen == "setting_volume_screen":
                if self.__button_further.mouse_over_button(mouse_pos, mouse_button=0):
                    self.__sound.increase_volume()
                
                elif self.__button_less.mouse_over_button(mouse_pos, mouse_button=0):
                     self.__sound.decrease_volume()
                     
        
    def run_main_menu(self):
        
        while self.__running_menu:
            self.draw_screens()
            self.__mouse_pos = pygame.mouse.get_pos()
            self.draw_button()
        
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.__current_screen = "main_menu"
                else:
                    self.mouse_events(event, self.__mouse_pos)
                
            pygame.display.flip()
        

