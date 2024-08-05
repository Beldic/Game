# Archivo de ejemplo que muestra un bucle del juego básico en pygame. 

import pygame

#Configuración de pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt = 0 

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:

    # Recuento de eventos
    # El evento pygame.QUIT significa que el usuario a hecho click en la x de la ventana 

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    # Rellena la pantalla con un color para limpiar del todo del anterior frame

    screen.fill("purple")
    
    # AQUÍ SE RENDERIZA EL JUEGO

    pygame.draw.circle(screen,"red",player_pos,40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() voltea el contenido para mostrarlo por pantalla 
    pygame.display.flip()

    
    
    # Limita los frames por segundo (FPS) a 60

    # dt es el delta time en segundos desde el último frame, se usa para los cuadros por segundo independiente de las físicas
    
    dt = clock.tick(60) / 1000





pygame.quit()