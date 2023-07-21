import pygame 
import os 

setting_win = {
    "WIDTH": 800,
    "HEIGHT": 700,
}
setting_bot = {
    "WIDTH": 100,
    "HEIGHT": 100
}

setting_boss ={
    "WIDHT": 500,
    "HEIGHT": 200
}

bot_list = list()
bullet_boss_list = list()

ads_path = os.path.abspath(__file__ + "/..") + "\\images\\"
bot_images = [pygame.transform.rotate(pygame.image.load(ads_path + "bot_1.png"), 180),
              pygame.transform.rotate(pygame.image.load(ads_path + "bot_1_2.png"), 180)]
hero_images = [pygame.image.load(ads_path + "hero1.png"),
              pygame.image.load(ads_path + "hero1_1.png")]
boss_images = [pygame.image.load(ads_path + "bot_2.png")]
              
bullet_image = pygame.image.load(ads_path + "bullet.png")
HP_image = pygame.image.load(ads_path + "HP.png")