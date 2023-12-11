import pygame
from constants import (WIDTH_MAIN_MENU,HIGH_MAIN_MENU,WIDTH_WINDOW,HIGH_WINDOW)
from button import Button
from game import Game

class MainMenu():
    def __init__(self):
        pygame.init()
        self.__screen = pygame.display.set_mode((WIDTH_WINDOW,HIGH_WINDOW))
        pygame.display.set_caption("Main Menu")
        self.__running_menu = True
        self.start_menu_background()
        self.start_menu_image()
        self.button_generator()

    def start_menu_background(self):
        self.__background_main_menu = pygame.image.load(r"assets\graphics\main_menu\bakground_main_menu.png").convert_alpha()
        self.__image_background_menu = pygame.transform.scale(self.__background_main_menu,(WIDTH_WINDOW,HIGH_WINDOW))
           
    def start_menu_image(self):
        self.__image = pygame.image.load(r"assets\graphics\main_menu\options.png").convert_alpha()
        self.__background_image = pygame.transform.scale(self.__image,(WIDTH_MAIN_MENU,HIGH_MAIN_MENU))
        self.__rect = self.__background_image.get_rect()
        self.__rect.x = (WIDTH_WINDOW - WIDTH_MAIN_MENU) / 2
        self.__rect.y = (HIGH_WINDOW - HIGH_MAIN_MENU) / 2
       
    def button_generator(self):
        self.__button_play = Button(pos_x=550,pos_y=210,path=r"assets\graphics\main_menu\button_play\play_button.png")
        self.__button_setting = Button(pos_x=550,pos_y=320,path=r"assets\graphics\main_menu\button_options\options_button.png")
        self.__button_exit = Button(pos_x=550,pos_y=430,path=r"assets\graphics\main_menu\button_quit\quit_button.png")
        self.__buttons = [self.__button_play,self.__button_setting,self.__button_exit]


    def print_main_menu(self):
        self.__screen.blit(self.__image_background_menu,(0,0))
        self.__screen.blit(self.__background_image,self.__rect)


    def mouse_events (self,event,mouse_pos):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.__button_play.mouse_over_button(mouse_pos, mouse_button=0):
                self.__game = Game(self.__screen)
                self.__game.run_game() 

            if self.__button_exit.mouse_over_button(mouse_pos, mouse_button=0):
                self.__running_menu = False
                print("SALISTE DEL JUEGO")


    def main_menu(self):
        
        while self.__running_menu:
            self.print_main_menu()
            self.__mouse_pos = pygame.mouse.get_pos()

            for button in self.__buttons:
                button.draw(self.__screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.__running_menu = False
                self.mouse_events(event,self.__mouse_pos)
            
            pygame.display.flip()
        pygame.quit()

main_menu = MainMenu()
main_menu.main_menu()
