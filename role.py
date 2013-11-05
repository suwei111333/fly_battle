
import pygame
import random
import math
SCREEN_WIDTH = 480
SCREEN_HEIGHT = 640

TYPE_S = 1
TYPE_M = 2
TYPE_B = 3

class Bullet(pygame.sprite.Sprite):
        def __init__(self, bullet_img, init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = bullet_img
            self.rect = self.image.get_rect()
            self.rect.midbottom = init_pos
            self.speed = 10

        def move(self):
            self.rect.top -= self.speed


class Player(pygame.sprite.Sprite):
        def __init__(self, plane_img, player_rect, init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = []
            for i in player_rect:
                self.image.append(plane_img.subsurface(i).convert_alpha())
            self.rect = player_rect[0]
            self.rect.topleft = init_pos
            self.speed = 8
            self.bullets = pygame.sprite.Group()
            self.img_index = 0
            self.is_hit = False
            self.equ = 1
            self.Big_bomb = 0

        def shoot(self, bullet_img):
            bullet_width = 20
            if self.equ == 1:
                bullet = Bullet(bullet_img, (self.rect.midtop[0], self.rect.midbottom[1]))
                self.bullets.add(bullet)
            elif self.equ == 2:
                bullet1 = Bullet(bullet_img, (self.rect.midtop[0] - bullet_width/2, self.rect.midbottom[1]))
                bullet2 = Bullet(bullet_img, (self.rect.midtop[0] + bullet_width/2, self.rect.midbottom[1]))
                self.bullets.add(bullet1)
                self.bullets.add(bullet2)
            elif self.equ == 3:
                bullet1 = Bullet(bullet_img, (self.rect.midtop[0] - bullet_width, self.rect.midbottom[1]))
                bullet2 = Bullet(bullet_img, (self.rect.midtop[0], self.rect.midbottom[1]))
                bullet3 = Bullet(bullet_img, (self.rect.midtop[0] + bullet_width, self.rect.midbottom[1]))
                self.bullets.add(bullet1)
                self.bullets.add(bullet2)
                self.bullets.add(bullet3)
        def destory(self):
            self.Big_bomb -= 1
        def moveup(self):
            if self.rect.top <= 0:
                self.rect.top = 0
            else:
                self.rect.top -= self.speed
        def movedown(self):
            if self.rect.bottom >= SCREEN_HEIGHT:
                self.rect.bottom = SCREEN_HEIGHT
            else:
                self.rect.bottom += self.speed
        def moveleft(self):
            if self.rect.left <= 0:
                self.rect.left = 0
            else:
                self.rect.left -= self.speed
        def moveright(self):
            if self.rect.right >= SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH
            else:
                self.rect.right += self.speed

class Enemy(pygame.sprite.Sprite):
        def __init__(self, enemy_img, enemy_down_imgs, init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = enemy_img
            self.rect = self.image.get_rect()
            self.rect.topleft = init_pos
            self.down_imgs = enemy_down_imgs
            self.speed = 3
            self.down_index = 0
        def move(self):
            self.rect.top += self.speed
            
class Enemy_m(pygame.sprite.Sprite):
        def __init__(self, enemy_m_img, enemy_m_down_imgs, init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = enemy_m_img
            self.rect = self.image.get_rect()
            self.rect.topleft = init_pos
            self.down_imgs = enemy_m_down_imgs
            self.speed = 4
            self.down_index = 0
            self.life = 2
        def move(self):
            angle = 0
            velx = self.speed * math.cos((3.14/180) * angle)
            #vely =  math.sin(3.14/180 * angle)
            #print velx, vely
            self.rect.top += velx
            #if random.randint(0,1):
            #    self.rect.left += vely
            #else:
            #    self.rect.left -= vely
            

class Enemy_1(pygame.sprite.Sprite):
        def __init__(self, enemy_1_img, enemy_1_down_imgs, init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = enemy_1_img
            self.rect = self.image.get_rect()
            self.rect.topleft = init_pos
            self.down_imgs = enemy_1_down_imgs
            self.speed = 1
            self.down_index = 0
            self.life = 10
        def move(self):
            angle = 0 #random.randint(30, 60)
            velx = self.speed * math.cos(3.14/180 * angle)
            #vely = self.speed * math.sin(3.14/180 * angle)
            self.rect.top += velx
            #self.rect.left += vely

class Bomb(pygame.sprite.Sprite):
        def __init__(self, bomb_img, init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = bomb_img
            self.rect = self.image.get_rect()
            self.rect.midbottom = init_pos
            self.speed = 3
        def move(self):
            self.rect.top += self.speed
            self.rect.left += self.speed/4*random.randint(-3, 3)

class Big_bomb(pygame.sprite.Sprite):
        def __init__(self, Big_bomb_img, init_pos):
            pygame.sprite.Sprite.__init__(self)
            self.image = Big_bomb_img
            self.rect = self.image.get_rect()
            self.rect.midbottom = init_pos
            self.speed = 3
        def move(self):
            self.rect.top += self.speed
            self.rect.left += self.speed/4*random.randint(-3, 3)


class Ufo2(pygame.sprite.Sprite):
    def __init__(self, ufo2_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = ufo2_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 3
    def move(self):
        self.rect.bottom += self.speed
        self.rect.left += self.speed/4*random.randint(-3, 3)

class Ufo1(pygame.sprite.Sprite):
    def __init__(self, ufo1_img, init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = ufo1_img
        self.rect = self.image.get_rect()
        self.rect.topleft = init_pos
        self.speed = 3
    def move(self):
        self.rect.bottom += self.speed
        self.rect.left += self.speed/4*random.randint(-3, 3)



