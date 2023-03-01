import pygame

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

height = 400
width = 1200

is_moving_forward = False
is_moving_back = False

left_border = -100
right_border = 1300

enemy_pos_x = 1100
enemy_speed = 4

seconds_passed = 0
ticks = 0

display_surface = pygame.display.set_mode((width, height))

forest_Background = pygame.image.load("/home/shane/Resources/Pictures/Backgrounds/forest_long.png").convert()
grass = pygame.image.load("/home/shane/Resources/Pictures/Backgrounds/grass.png").convert_alpha()
player = pygame.image.load("/home/shane/Resources/Pictures/Character/player_1.png").convert_alpha()
enemy_1 = pygame.image.load("/home/shane/Resources/Pictures/Enemy/enemy_1.png").convert_alpha()

player = pygame.transform.scale(player, (40,80))
player_rect = player.get_rect()
player_rect.center = (100, 350)

enemy_1 = pygame.transform.scale(enemy_1, (30, 75))
enemy_1_rect = enemy_1.get_rect()
enemy_1_rect.center = (enemy_pos_x, 350)

pygame.display.set_caption('RandomGame')

while True:

    collide = pygame.Rect.colliderect(player_rect, enemy_1_rect)

    display_surface.blit(forest_Background, (0, 0))

    display_surface.blit(player, player_rect)
    display_surface.blit(enemy_1, enemy_1_rect)

    display_surface.blit(grass,(350,300))
    display_surface.blit(grass,(150,300))
    display_surface.blit(grass,(-50,300))
    display_surface.blit(grass,(550,300))
    display_surface.blit(grass,(750,300))
    display_surface.blit(grass,(950,300))

    if collide: enemy_1_rect.x = enemy_pos_x

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player_rect.x -= 4
    if keys[pygame.K_d]:
        player_rect.x += 4

    enemy_1_rect.x -= enemy_speed

    if enemy_1_rect.x <= left_border: enemy_1_rect.x = right_border

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()

    ticks += 1

    if ticks == 60:
        ticks %= 60
        seconds_passed += 1
    if seconds_passed == 10:
        seconds_passed = 0
        if enemy_speed < 20:
            enemy_speed += 1

    fpsClock.tick(FPS)