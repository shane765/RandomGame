import pygame

pygame.init()

height = 400
width = 1200

display_surface = pygame.display.set_mode((width, height))

forest_Background = pygame.image.load("/home/shane/Resources/Pictures/Backgrounds/forest_long.png").convert()
grass = pygame.image.load("/home/shane/Resources/Pictures/Backgrounds/grass.png").convert_alpha()


pygame.display.set_caption('RandomGame')

while True:
    display_surface.blit(forest_Background, (0, 0))
    display_surface.blit(grass,(350,300))
    display_surface.blit(grass,(150,300))
    display_surface.blit(grass,(-50,300))
    display_surface.blit(grass,(550,300))
    display_surface.blit(grass,(750,300))
    display_surface.blit(grass,(950,300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()