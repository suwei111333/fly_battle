# -*- coding: utf-8 -*-

import pygame
from sys import exit
from pygame.locals import *
from role import *
import random

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("plane fighting")

#load mussic
bullet_sound = pygame.mixer.Sound('resources/sound/bullet.wav')
enemy1_down_sound = pygame.mixer.Sound('resources/sound/enemy1_down.wav')
enemy2_down_sound = pygame.mixer.Sound('resources/sound/enemy2_down.wav')
enemy3_down_sound = pygame.mixer.Sound('resources/sound/enemy3_down.wav')
game_over_sound = pygame.mixer.Sound('resources/sound/game_over.wav')
bullet_sound.set_volume(0.3)
enemy1_down_sound.set_volume(0.3)
enemy2_down_sound.set_volume(0.3)
enemy3_down_sound.set_volume(0.3)
game_over_sound.set_volume(0.3)

pygame.mixer.music.load('resources/sound/game_music.wav')
pygame.mixer.music.play(-1, 0.0)
pygame.mixer.music.set_volume(0.25)

# 载入背景图
background = pygame.image.load('resources/image/background.png').convert()
game_over = pygame.image.load('resources/image/gameover.png')

filename = 'resources/image/shoot.png'
plane_img = pygame.image.load(filename)

player_rect = []
player_rect.append(pygame.Rect(0, 99, 102, 126))
player_rect.append(pygame.Rect(165, 360, 102, 126))
player_rect.append(pygame.Rect(165, 234, 102, 126))
player_rect.append(pygame.Rect(330, 624, 102, 126))
player_rect.append(pygame.Rect(330, 498, 102, 126))
player_rect.append(pygame.Rect(432, 624, 102, 126))
player_pos = [200, 600]
player = Player(plane_img, player_rect, player_pos)

bullet_rect = pygame.Rect(1004, 987, 9, 21)
bullet_img = plane_img.subsurface(bullet_rect)

#enemy1
enemy1_rect = pygame.Rect(534, 612, 57, 43)
enemy1_img = plane_img.subsurface(enemy1_rect)
enemy1_down_imgs = []
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(873, 697, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 296, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(939, 697, 57, 43)))
enemies1 = pygame.sprite.Group()
enemies_down = pygame.sprite.Group()

#enemy2
enemy2_rect = pygame.Rect(0, 0 , 69, 99)
enemy2_img = plane_img.subsurface(enemy2_rect)
enemy2_down_imgs = []
#enemy2_down_imgs.append(plane_img.subsurface(pygame.Rect(432, 525, 69, 99)))
enemy2_down_imgs.append(plane_img.subsurface(pygame.Rect(534, 655, 69, 99)))
enemy2_down_imgs.append(plane_img.subsurface(pygame.Rect(603, 655, 69, 99)))
enemy2_down_imgs.append(plane_img.subsurface(pygame.Rect(672, 653, 69, 99)))
enemy2_down_imgs.append(plane_img.subsurface(pygame.Rect(741, 653, 69, 99)))
enemies2 = pygame.sprite.Group()
enemies_m_down = pygame.sprite.Group()

#enemy3
enemy3_rect = pygame.Rect(335, 755 , 169, 258)
enemy3_img = plane_img.subsurface(enemy3_rect)
enemy3_down_imgs = []
enemy3_down_imgs.append(plane_img.subsurface(pygame.Rect(0, 486, 165, 261)))
enemy3_down_imgs.append(plane_img.subsurface(pygame.Rect(0, 225, 165, 261)))
enemy3_down_imgs.append(plane_img.subsurface(pygame.Rect(839, 748, 165, 260)))
enemy3_down_imgs.append(plane_img.subsurface(pygame.Rect(165,486, 165, 260)))
enemy3_down_imgs.append(plane_img.subsurface(pygame.Rect(673, 748, 166, 260)))
enemy3_down_imgs.append(plane_img.subsurface(pygame.Rect(0, 747, 166, 261)))
enemies3 = pygame.sprite.Group()
enemies_l_down = pygame.sprite.Group()



ufo2_rect = pygame.Rect(102, 118, 60, 107)
ufo2_img = plane_img.subsurface(ufo2_rect)
ufo2_frequency = 100
ufo2s = pygame.sprite.Group()

bomb_rect = pygame.Rect(810,691, 63, 57)
bomb_img = plane_img.subsurface(bomb_rect)
has_bomb = False
bomb_rect.left = 0
bomb_rect.top = SCREEN_HEIGHT - bomb_rect.height
bomb_used = False


ufo1_rect = pygame.Rect(267,398, 58, 88)
ufo1_img = plane_img.subsurface(ufo1_rect)
ufo1_frequency = 200
ufo1s = pygame.sprite.Group()

shoot_frequency = 0
enemy_frequency = 0

player_down_index = 16

score = 0

running = True

clock = pygame.time.Clock()

while running:
    clock.tick(60)
    #########################################################
    # move code area
    #######################################################
    
    #bullet
    if not player.is_hit:
        if shoot_frequency % 15 == 0:
            bullet_sound.play()
            player.shoot(bullet_img)
            shoot_frequency = 0
        shoot_frequency += 1
    
    for bullet in player.bullets:
        bullet.move()
        if bullet.rect.bottom < 0:
            player.bullets.remove(bullet)
    
    #enemy
    if enemy_frequency % 50 == 0:
        enemy1_pos = [random.randint(0, SCREEN_WIDTH-enemy1_rect.width), 0]
        enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos)
        enemies1.add(enemy1)
    elif enemy_frequency % 99 == 0:
        enemy2_pos = [random.randint(0, SCREEN_WIDTH - enemy2_rect.width), 0]
        enemy2 = Enemy_m(enemy2_img, enemy2_down_imgs, enemy2_pos)
        enemies2.add(enemy2)
    elif enemy_frequency % 199 == 0 and random.randint(0, 1):
        enemy3_pos = [random.randint(0, SCREEN_WIDTH - enemy3_rect.width), 0]
        enemy3 = Enemy_1(enemy3_img, enemy3_down_imgs, enemy3_pos)
        enemies3.add(enemy3)

    enemy_frequency += 1
    if enemy_frequency >= 200:
        enemy_frequency = 0

    for enemy in enemies1:
        enemy.move()
        if pygame.sprite.collide_circle(enemy, player):
            enemies_down.add(enemy)
            enemies1.remove(enemy)
            player.is_hit = True
            game_over_sound.play()
            break
        if enemy.rect.top > SCREEN_HEIGHT:
            enemies1.remove(enemy)

    enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)
    for enemy in enemies1_down:
        enemies_down.add(enemy)

    for enemy in enemies2:
        enemy.move()
        if pygame.sprite.collide_circle(enemy, player):
            enemies_m_down.add(enemy)
            enemies2.remove(enemy)
            player.is_hit = True
            game_over_sound.play()
            break
        if enemy.rect.top > SCREEN_HEIGHT:
            enemies2.remove(enemy)

    enemies1_m_down = pygame.sprite.groupcollide(enemies2, player.bullets, 0, 1)
    for enemy in enemies1_m_down:
        enemy.life -= 1
        if enemy.life <= 0:
            enemies_m_down.add(enemy)
            enemies2.remove(enemy)
    
    for enemy in enemies3:
        enemy.move()
        if pygame.sprite.collide_circle(enemy, player):
            enemies_l_down.add(enemy)
            enemies3.remove(enemy)
            player.is_hit = True
            game_over_sound.play()
            break
        if enemy.rect.top > SCREEN_HEIGHT:
            enemies3.remove(enemy)

    enemies1_l_down = pygame.sprite.groupcollide(enemies3, player.bullets, 0, 1)
    for enemy in enemies1_l_down:
        enemy.life -= 1
        if enemy.life <= 0:
            enemies_l_down.add(enemy)
            enemies3.remove(enemy)

    if bomb_used:
        for enemy in enemies1:
            enemies_down.add(enemy)
            enemies1.remove(enemy)
        for enemy in enemies2:
            enemies_m_down.add(enemy)
            enemies2.remove(enemy)
        for enemy in enemies3:
            enemies_l_down.add(enemy)
            enemies3.remove(enemy)
        bomb_used = False
        has_bomb = False

    if ufo2_frequency <= 0:
        ufo2_frequency = random.randint(500, 700)
        ufo2s.add(Ufo2(ufo2_img, [random.randint(0, SCREEN_WIDTH), 0]))
    ufo2_frequency -= 1

    for ufo2 in ufo2s:
        ufo2.move()
        if ufo2.rect.bottom >= SCREEN_HEIGHT:
            ufo2s.remove(ufo2)
        elif pygame.sprite.collide_circle(ufo2, player):
            ufo2s.remove(ufo2)
            has_bomb = True


    if ufo1_frequency <= 0:
        ufo1_frequency = random.randint(700, 2000)
        ufo1s.add(Ufo1(ufo1_img, [random.randint(0, SCREEN_WIDTH), 0]))
    ufo1_frequency -= 1

    for ufo1 in ufo1s:
        ufo1.move()
        if ufo1.rect.bottom >= SCREEN_HEIGHT:
            ufo1s.remove(ufo1)
        elif pygame.sprite.collide_circle(ufo1, player):
            ufo1s.remove(ufo1)
            if player.equ < 3:
                player.equ += 1
   ##########################################################
   # rendering object area
   ########################################################
    screen.fill(0)
    screen.blit(background, (0, 0))

    if not player.is_hit:
        screen.blit(player.image[player.img_index], player.rect)
        player.img_index = shoot_frequency /6
    else:
        player.img_index = player_down_index /6
        screen.blit(player.image[player.img_index], player.rect)
        player_down_index += 1
        if player_down_index > 6:
            running = False

    player.bullets.draw(screen)
    enemies1.draw(screen)
    enemies2.draw(screen)
    enemies3.draw(screen)

    for enemy_down in enemies_down:
        if enemy_down.down_index == 0:
            enemy1_down_sound.play()
        if enemy_down.down_index > 7:
            enemies_down.remove(enemy_down)
            score += 100
            continue
        screen.blit(enemy_down.down_imgs[enemy_down.down_index/2], enemy_down.rect)
        enemy_down.down_index += 1

    for enemy_down in enemies_m_down:
        if enemy_down.down_index == 0:
            enemy2_down_sound.play()
        if enemy_down.down_index > 7:
            enemies_m_down.remove(enemy_down)
            score += 100
            continue
        screen.blit(enemy_down.down_imgs[enemy_down.down_index/2], enemy_down.rect)
        enemy_down.down_index += 1

    for enemy_down in enemies_l_down:
        if enemy_down.down_index == 0:
            enemy3_down_sound.play()
        if enemy_down.down_index > 7:
            enemies_l_down.remove(enemy_down)
            score += 100
            continue
        screen.blit(enemy_down.down_imgs[enemy_down.down_index/2], enemy_down.rect)
        enemy_down.down_index += 1


    ufo2s.draw(screen)
    ufo1s.draw(screen)

    if has_bomb:
        screen.blit(bomb_img, bomb_rect)

    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_text, text_rect)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if has_bomb and bomb_rect.collidepoint(mouse_pos[0], mouse_pos[1]):
                bomb_used = True

    key_pressed = pygame.key.get_pressed()

    if not player.is_hit:
        if key_pressed[K_w] or key_pressed[K_UP]:
            player.moveup()
        elif key_pressed[K_s] or key_pressed[K_DOWN]:
            player.movedown()
        elif key_pressed[K_a] or key_pressed[K_LEFT]:
            player.moveleft()
        elif key_pressed[K_d] or key_pressed[K_RIGHT]:
            player.moveright()



