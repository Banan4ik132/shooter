import pygame
from data import *
from time import sleep

class Menu():
    def __init__(self):
        height = 60
        self.BUTTON1 = pygame.Rect(setting_win["WIDTH"] // 2 - 250 - 20,
                                   setting_win["HEIGHT"] // 2,
                                   230, height)
        self.BUTTON2 = pygame.Rect(setting_win["WIDTH"] // 2 + 20,
                                   setting_win["HEIGHT"] // 2,
                                   200, height)
        self.RENDER1 = pygame.font.Font(None, 40).render("ПРОДОВЖИТИ", True, (0, 0, 0))
        self.RENDER2 = pygame.font.Font(None, 40).render("ВИЙТИ", True, (0, 0, 0))

    def draw_menu(self, window):
        pygame.draw.rect(window, (100, 222, 132), self.BUTTON1)
        pygame.draw.rect(window, (100, 222, 132), self.BUTTON2)
        window.blit(self.RENDER1, (self.BUTTON1.x + 10, self.BUTTON1.y + 15))
        window.blit(self.RENDER2, (self.BUTTON2.x + 50, self.BUTTON2.y + 15))


class BackGround():
    def __init__(self, image, speed):
        self.OLD = [0, 0]
        self.NEW = [0, - setting_win["HEIGHT"]]
        self.NEW_Y = self.NEW[1]
        self.OLD_Y = 0
        self.NEW_IMAGE = image
        self.OLD_IMAGE = image
        self.SPEED = speed

    def move(self, window):
        window.blit(self.OLD_IMAGE, self.OLD)
        window.blit(self.NEW_IMAGE, self.NEW)
        self.OLD_Y += self.SPEED
        self.NEW_Y += self.SPEED
        self.OLD[1] = int(self.OLD_Y)
        self.NEW[1] = int(self.NEW_Y)
        if self.NEW[1] == setting_win["HEIGHT"]:
            self.NEW[1] = - setting_win["HEIGHT"]
            self.NEW_Y = self.NEW[1]
        if self.OLD[1] == setting_win["HEIGHT"]:
            self.OLD[1] = - setting_win["HEIGHT"]
            self.OLD_Y = self.OLD[1]
         



class Level():
    def __init__(self):
        self.LVL = 0

    def next_level(self, window):
        text = f"Ви перейшли на рівень {self.LVL}"
        font = pygame.font.Font(None, 40).render(text, True, (200, 78, 0))
        window.blit(font, (setting_win["WIDTH"] // 2 - 100, setting_win["HEIGHT"] // 2))
        pygame.display.flip()
        sleep(3)

lvl = Level()

class Bullet(pygame.Rect):
    def __init__(self, image, speed, x= 0, y= 0, width= 0, height= 0):
        super().__init__(x, y, width, height)
        self.IMAGE = image
        self.SPEED = speed

    def move_hero(self, window):
        window.blit(self.IMAGE, (self.x, self.y))
        self.y -= self.SPEED

    def move_boss(self, window, bullet= None, hero= None):
        window.blit(self.IMAGE, (self.x, self.y))
        self.y += self.SPEED
        if self.colliderect(hero):
            hero.HP -= 1
            bullet_boss_list.remove(bullet)


class Sprite(pygame.Rect):
    def __init__(self, x, y, width, height, color= None, image= None, speed= None, hp= 3):
        super().__init__(x, y, width, height)
        self.COLOR = color
        self.IMAGE_LIST = image
        self.IMAGE = self.IMAGE_LIST[0]
        self.IMAGE_COUNT = 0
        self.SPEED = speed
        self.HP = hp

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
        self.KILL_BOT_LVL = 0
        self.KILL = 0
        self.KILL_BOSS = 0

    def move(self, window, key):
        if key[pygame.K_w] and self.y > 0:
            self.y -= self.SPEED
        elif key[pygame.K_s] and self.y < setting_win["HEIGHT"]:
            self.y += self.SPEED
        if key[pygame.K_a] and self.x > 0:
            self.x -= self.SPEED
        elif key[pygame.K_d] and self.x + self.width < setting_win["WIDTH"]:
            self.x += self.SPEED
        self.move_images() 
        window.blit(self.IMAGE, (self.x, self.y))

    def move_bullet(self, window, boss):
        for bullet in self.BULLETS:
            bullet.move_hero(window)
            if bullet.y <= 0:
                self.BULLETS.remove(bullet)
                continue
            if boss:
                if bullet.colliderect(boss):
                    self.BULLETS.remove(bullet)
                    boss.HP -= 1
                    continue
            for bot in bot_list:
                if bullet.colliderect(bot):
                    bot_list.remove(bot)
                    self.BULLETS.remove(bullet)
                    self.KILL += 1
                    self.KILL_BOT_LVL += 1
                    break

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
        elif self.BULLET.y + self.BULLET.height > setting_win["HEIGHT"]:
            self.BULLET.y - self.y + self.height

class Boss(Sprite):
    def __init__(self, x, y, widht, height, color= None, image= None, speed= None, hp= 3):
        super().__init__(x, y, widht, height, color, image, speed, hp= 30)
        self.START_SHOT = pygame.time.get_ticks()

    def move(self, window):
        if self.y <= 20:
            self.y += self.SPEED
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
