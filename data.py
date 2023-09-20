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
    "WIDTH": 300,
    "HEIGHT": 300
}

bot_list = list()
bullet_boss_list = list()

ads_path = os.path.abspath(__file__ + "/..") + "\\images\\"
bot_images = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(ads_path + "bot_1.png"), (setting_bot["WIDTH"], setting_bot["HEIGHT"])), False, True),
              pygame.transform.flip(pygame.transform.scale(pygame.image.load(ads_path + "bot_1_2.png"), (setting_bot["WIDTH"], setting_bot["HEIGHT"])), False, True)]
hero_images = [pygame.image.load(ads_path + "hero1.png"),
              pygame.image.load(ads_path + "hero1_1.png")]
boss_images = [pygame.transform.flip(pygame.transform.scale(pygame.image.load(ads_path + "bot_1.png"), (setting_boss["WIDTH"], setting_boss["HEIGHT"])), False, True),
               pygame.transform.flip(pygame.transform.scale(pygame.image.load(ads_path + "bot_1_2.png"), (setting_boss["WIDTH"], setting_boss["HEIGHT"])), False, True)]
              
bullet_image = pygame.image.load(ads_path + "bullet.png")
HP_image = pygame.image.load(ads_path + "HP.png")
bg_image = pygame.image.load(ads_path + "фон1.png")