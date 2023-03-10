import pygame

pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

height = 400
width = 1200

is_moving_forward = False
is_moving_back = False

is_hit = False
leben = 3
hit_timer = 0
death_timer = 1

left_border = -0
right_border = 1200

enemy_pos_x = 1100
enemy1_speed = 4
enemy2_speed = 4

seconds_passed = 0
ticks = 0
total_time = "0"

is_jumping = False
still_jumping  = True
gravity = 10

display_surface = pygame.display.set_mode((width, height))

forest_Background = pygame.image.load("/home/shane/Resources/Pictures/Backgrounds/forest_long.png").convert()
grass = pygame.image.load("/home/shane/Resources/Pictures/Backgrounds/grass.png").convert_alpha()
player = pygame.image.load("/home/shane/Resources/Pictures/Character/player_1.png").convert_alpha()
enemy_1 = pygame.image.load("/home/shane/Resources/Pictures/Enemy/enemy_1.png").convert_alpha()
enemy_2 = pygame.image.load("/home/shane/Resources/Pictures/Enemy/enemy_2.png").convert_alpha()
herz = pygame.image.load("/home/shane/Resources/Pictures/Other/herz.png").convert_alpha()

player = pygame.transform.scale(player, (40,80))
player_rect = player.get_rect()
player_rect.center = (100, 350)

enemy_1 = pygame.transform.scale(enemy_1, (30, 75))
enemy_1_rect = enemy_1.get_rect()
enemy_1_rect.center = (enemy_pos_x, 350)

enemy_2 = pygame.transform.scale(enemy_2, (75, 75))
enemy_2_rect = enemy_2.get_rect()
enemy_2_rect.center = (enemy_pos_x, 350)

herz = pygame.transform.scale(herz, (50,50))

font = pygame.font.Font(None, 70)
score = font.render(total_time, False, "Black" )
score_rect = score.get_rect()
score_rect.center = (600,75)

score_text = font.render("Score:", False, "Black" )
score_text_rect = score_text.get_rect()
score_text_rect.center = (100,75)

death_text = font.render("You Died", False, "Red" )
death_text_rect = death_text.get_rect()
death_text_rect.center = (600,200)

pygame.display.set_caption('Das neue Soulslike')

while True:

    collide = pygame.Rect.colliderect(player_rect, enemy_1_rect)
    if collide and hit_timer <= 0:
        leben -= 1
        hit_timer = 30
    if int(total_time) > 50:
        collide = pygame.Rect.colliderect(player_rect, enemy_2_rect)
        if collide and hit_timer <= 0:
            hit_timer = 30
            leben -= 1

    display_surface.blit(forest_Background, (0, 0))

    display_surface.blit(player, player_rect)
    display_surface.blit(enemy_1, enemy_1_rect)
    if int(total_time) > 50: display_surface.blit(enemy_2, enemy_2_rect)

    if leben >= 3: display_surface.blit(herz,(950,50))
    if leben >= 2: display_surface.blit(herz, (1025, 50))
    if leben >= 1: display_surface.blit(herz, (1100, 50))

    display_surface.blit(grass, (350,300))
    display_surface.blit(grass, (150,300))
    display_surface.blit(grass, (-50,300))
    display_surface.blit(grass, (550,300))
    display_surface.blit(grass, (750,300))
    display_surface.blit(grass, (950,300))

    score = font.render(total_time, False, "Black")
    death = font.render("You Died", False, "Red")
    display_surface.blit(score, score_rect)
    display_surface.blit(score_text, score_text_rect)

    if death_timer == 0:
        is_hit = True

    if leben == 0:
        display_surface.blit(death, death_text_rect)
        death_timer -= 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if player_rect.centerx > 0: player_rect.x -= 4
    if keys[pygame.K_RIGHT]:
        if player_rect.centerx < 1200:player_rect.x += 4

    if not is_jumping:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_jumping = True
    else:
        if player_rect.centery > 150 and still_jumping:
            player_rect.centery -= gravity
            if player_rect.centery == 150: still_jumping = False
        elif player_rect.centery <= 150 or not still_jumping:
            player_rect.centery += gravity
            if player_rect.centery >= 350:
                is_jumping = False
                still_jumping = True

    if int(total_time) > 50: enemy_2_rect.x -= enemy2_speed
    enemy_1_rect.x -= enemy1_speed

    if enemy_1_rect.centerx <= left_border: enemy1_speed *= -1
    if enemy_1_rect.centerx >= right_border: enemy1_speed *= -1
    if enemy_2_rect.centerx <= left_border: enemy2_speed *= -1
    if enemy_2_rect.centerx >= right_border: enemy2_speed *= -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    if not is_hit : pygame.display.update()

    ticks += 1
    hit_timer -= 1

    if ticks == 60:
        ticks %= 60
        seconds_passed += 1

        temp = int(total_time)
        temp += 1
        total_time = str(temp)

    if int(total_time) > 50:
        if seconds_passed == 10:
            if 20 >= enemy2_speed > 0:
                enemy2_speed += 1
            elif -20 <= enemy2_speed < 0:
                enemy2_speed -= 1

    if seconds_passed == 10:
        seconds_passed = 0
        if 20 >= enemy1_speed > 0:
            enemy1_speed += 1
        elif -20 <= enemy1_speed < 0:
            enemy1_speed -= 1

    fpsClock.tick(FPS)