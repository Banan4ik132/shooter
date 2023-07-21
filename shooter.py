import pygame
from data import *

class Bullet(pygame.Rect):
    def __init__(self, image, speed, x= 0, y= 0, width= 0, height= 0):
        super().__init__(x, y, width, height)
        self.IMAGE = image
        self.SPEED = speed

    def move_hero(self, window):
        window.blit(self.IMAGE, (self.x, self.y))
        self.y -= self.SPEED

    def move_boss(self, window):
        window.blit(self.IMAGE, (self.x, self.y))


class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height, color= None, image= None, speed= None, hp= 3):
        super().__init__(x, y, width, height)
        self.COLOR = color
        self.IMAGE_LIST = image
        self.IMAGE = self.IMAGE_LIST[0]
        self.IMAGE_COUNT = 0
        self.SPEED = speed
        self.HP = hp
        self.KILL = 0
        self.KILL_BOT_LVL = 0

    def move_images(self):
        if self.IMAGE_COUNT == len(self.IMAGE_LIST) * 10:
            self.IMAGE_COUNT = 0
        if self.IMAGE_COUNT / 10 == self.IMAGE_COUNT // 10:
            self.IMAGE = self.IMAGE_LIST[self.IMAGE_COUNT // 10]
        self.IMAGE_COUNT += 1    

class Hero(Sprite):
    def __init__(self, x, y, widht, height, color= None, image= None, speed= None, hp= 3):
        super().__init__(x, y, widht, height, color, image, speed, hp)
        self.MOVE = {"UP": False, "DOWN":False, "LEFT": False, "RIGHT": False}
        self.BULLETS = list()

    def move(self, window):
        if self.MOVE["UP"] and self.y > 0:
            self.y -= self.SPEED
        elif self.MOVE["DOWN"] and self.y < setting_win["HEIGHT"]:
            self.y += self.SPEED
        if self.MOVE["LEFT"] and self.x > 0:
            self.x -= self.SPEED
        elif self.MOVE["RIGHT"] and self.x + self.width < setting_win["WIDTH"]:
            self.x += self.SPEED
        self.move_images() 
        window.blit(self.IMAGE, (self.x, self.y))

    def move_bullet(self, window):
        for bullet in self.BULLETS:
            bullet.move_hero(window)
            if bullet.y <= 0:
                self.BULLETS.remove(bullet)
            for bot in bot_list:
                if bullet.colliderect(bot):
                    bot_list.remove(bot)
                    self.BULLETS.remove(bullet)
                    self.KILL += 1

class Bot(Sprite):
    def __init__(self, x, y, widht, height, color= None, image= None, speed= None, hp= 3):
        super().__init__(x, y, widht, height, color, image, speed, hp)
        self.BULLET = Bullet(bullet_image, 4, self.x + self.width // 2 -5, self.y + self.height, width= 10, height= 20)

    def move(self, window):
        self.y += self.SPEED
        window.blit(self.IMAGE, (self.x, self.y))
        self.move_images()

    def move_bullet(self, window, hero):
        self.BULLET.y += self.BULLET.SPEED
        window.blit(self.BULLET.IMAGE, (self.BULLET.x, self.BULLET.y))
        if self.BULLET.colliderect(hero):
            self.BULLET.y = self.y + self.height
            hero.HP -= 1

class Boss(Sprite):
    def __init__(self, x, y, widht, height, color= None, image= None, speed= None, hp= 3):
        super().__init__(x, y, widht, height, color, image, speed, hp)
        self.START_SHOT = pygame.time.get_ticks()

    def move(self, window):
        if self.y <= 20:
            self.y += self.SPEDD
        elif self.x < 10 or self.x + self.width > setting_win["WIDTH"] - 10:
            self.SPEED *= -1
            self.x += self.SPEED
        else:
            self.x += self.SPEED
            window.blit(self.IMAGE, (self.x, self.y))
        self.move_images()
        
        if pygame.time.get_ticks() - self.START_SHOT > 1500:
            self.START_SHOT = pygame.time.get_ticks()
            bullet_boss_list.append(Bullet(bullet_image, 3, x= self.x + self.width // 2 - 50, y= self.y + self.height, width= 10, height= 20))
            bullet_boss_list.append(Bullet(bullet_image, 3, x= self.x + self.width // 2 + 40, y= self.y + self.height, width= 10, height= 20))
