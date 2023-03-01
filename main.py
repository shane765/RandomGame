import pygame

pygame.init()

height = 400
width = 600

display_surface = pygame.display.set_mode((width, height))

forest_Background = pygame.image.load("/home/shane/Resources/Pictures/Backgrounds/forestBackground.png").convert()
grass1 = pygame.image.load("/home/shane/Resources/Pictures/Backgrounds/grass.png").convert_alpha()
grass2 = pygame.image.load("/home/shane/Resources/Pictures/Backgrounds/grass.png").convert_alpha()
grass3 = pygame.image.load("/home/shane/Resources/Pictures/Backgrounds/grass.png").convert_alpha()


pygame.display.set_caption('RandomGame')

while True:
    display_surface.blit(forest_Background, (0, 0))
    display_surface.blit(grass1,(350,300))
    display_surface.blit(grass2,(150,300))
    display_surface.blit(grass3,(-50,300))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()