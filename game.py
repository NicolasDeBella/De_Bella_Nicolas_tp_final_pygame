import pygame   
from constants import *
from auxiliar import *
from stage import Stage


pygame.init()
screen = pygame.display.set_mode((WIDTH_WINDOW, HIGH_WINDOW))
imagen_fondo = pygame.image.load(r"assets\graphics\background\background_level_1.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, (WIDTH_WINDOW, HIGH_WINDOW))

running_game = True
clock = pygame.time.Clock()


stage = Stage()

while running_game:
    teclas_presionadas = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Estoy CERRANDO el JUEGO')
            running_game = False
            break
            
    stage.player.keyboard_events(teclas_presionadas)   
    
    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    stage.run(delta_ms,screen)


    pygame.display.flip()
    
    
    

    

pygame.quit()
