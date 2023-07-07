import pygame
from data import *

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

class Nero(Sprite):
    def __init__(self, x, y, widht, height, color= None, image= None, speed= None, hp= 3):
        super().__init__(x, y, widht, height, color, image, speed, hp)
        self.MOVE = {"UP": False, "DOWN":False, "LEFT": False, "RIGHT": False}

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

class Bot(Sprite):
    def __init__(self, x, y, widht, height, color= None, image= None, speed= None, hp= 3):
        super().__init__(x, y, widht, height, color, image, speed, hp)

    def move(self, window):
        self.y += self.SPEED
        window.blit(self.IMAGE, (self.x, self.y))
        self.move_images()