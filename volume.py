import pygame
from constants import BLANCO

class Volume():
    def __init__(self, path_sound: str) -> None:
        pygame.mixer.init()
        self.__sound = pygame.mixer.Sound(path_sound)
        self.__volume = 0.1
        self.__volume_increase = 0.1
        self.__sound.set_volume(self.__volume)
        self.__sound_status = True
        
    @property
    def sound_status(self):
        return self.__sound_status
    
    @property
    def volume(self):
        return self.__volume

    @volume.setter
    def volume(self, new_volume):
        self.__volume = max(0.0, min(1.0, new_volume))
        self.__sound.set_volume(self.__volume)
    
    def increase_volume(self):
        self.volume += self.__volume_increase
    
    def decrease_volume(self):
        self.volume -= self.__volume_increase
    
    def play_sound(self):
        self.__sound.play()
        self.__sound_status = True

    def stop_sound(self):
        self.__sound.stop()
        self.__sound_status = False
    
    def draw_volume_text(self,screen,text:str,on_of:True):
        if not on_of:
            font = pygame.font.Font(None, 36)
            volume_text = font.render(f"{text} {int(self.__volume * 100)}%", True, BLANCO)
            screen.blit(volume_text, (510, 500))
        else:
            font = pygame.font.Font(None, 36)
            volume_text = font.render(f"{text}", True, BLANCO)
            screen.blit(volume_text, (1000, 550))

        
