import pygame
from sys import exit

pygame.init()

# Tamanho da janela
screen = pygame.display.set_mode((1024, 768))
# Configurações de display e definições para o event loop
pygame.display.set_caption('School today?')
framerate = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/surfaces/Sky.png')
ground_surface = pygame.image.load('graphics/surfaces/ground.png')
player = pygame.image.load('graphics/player/boneca-parada.png')
player = pygame.transform.scale(player, (144, 256.5))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Adiciona blocos de imagem na tela
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0, 430))
    screen.blit(player, (512, 210))
    # renderiza todos os elementos
    # atualiza tudo
    pygame.display.update()
    # Trava o framerate a 60 por segundo
    framerate.tick(60)