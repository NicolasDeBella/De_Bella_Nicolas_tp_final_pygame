import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self,pos_x,pos_y,path,width,high):
        super().__init__()
        self.__original_image = pygame.image.load(path).convert_alpha()
        self.__button_image = pygame.transform.scale(self.__original_image,(width, high)) 
        self.__rect = self.__button_image.get_rect()
        self.__rect.x = pos_x
        self.__rect.y = pos_y
        
      
    @property
    def rect(self):
        return self.__rect
    
    def mouse_over_button(self, mouse_pos, mouse_button):
        return self.__rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[mouse_button]
    
    
    def draw(self,screen):
        screen.blit(self.__button_image,self.__rect)