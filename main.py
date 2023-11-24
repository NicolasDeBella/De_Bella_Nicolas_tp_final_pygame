import pygame   
from constants import *
from auxiliar import *
from player import Player
from enemy import Enemy


pygame.init()
screen = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
imagen_fondo = pygame.image.load(r"assets\graphics\background\background_level_1.jpg")
imagen_fondo = pygame.transform.scale(imagen_fondo, (ANCHO_VENTANA, ALTO_VENTANA))

running_game = True
clock = pygame.time.Clock()

player_marco = Player(x=0,y=475,speed_walk=4,gravity=20,jump_power=15,frame_animacion_rate_ms=80,frame_movimiento_rate_ms=20)
enemigo = Enemy(x=1400, y=475, x_limit_left=0, x_limit_right=ANCHO_VENTANA, speed=5,frame_animacion_rate_ms=80,frame_movimiento_rate_ms=20)


while running_game:
    teclas_presionadas = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Estoy CERRANDO el JUEGO')
            running_game = False
            break
            
    player_marco.keyboard_events(teclas_presionadas)   
    
    delta_ms = clock.tick(FPS)
    screen.blit(imagen_fondo,imagen_fondo.get_rect())
    player_marco.update(delta_ms) 
    player_marco.draw(screen)
    enemigo.update(delta_ms,screen)
    enemigo.draw(screen)
    


    pygame.display.flip()
    
    
    

    

pygame.quit()
