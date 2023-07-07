import pygame
from data import *
from shooter import *
from random import randint 

pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("Shooter")

def run():
    game = True
    time_start = 0
    time_end = 0

    hero = Nero(100, 100, 100, 100, speed= 5, color= (132, 33, 77), image= hero_images)
    #bot = Bot(500, 0 - 100, 100, 100, speed= 2, image= bot_images)
    clock = pygame.time.Clock()

    while game:
        window.fill((255, 255, 255))

        #HERO
        hero.move(window)

        #BOT
        time_end = pygame.time.get_ticks()
        if time_end - time_start > 2500:
            bot_list.append(Bot(randint(0, setting_win["WIDTH"] - setting_bot["WIDTH"]), 0 - setting_bot["HEIGHT"], setting_bot["WIDTH"], setting_bot["HEIGHT"],  speed= 2, image= bot_images))
            time_start = time_end

        for bot in bot_list:    
            bot.move(window)
        #pygame.draw.rect(window, hero.COLOR, hero)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = True
                if event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = True
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = True
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    hero.MOVE["UP"] = False
                if event.key == pygame.K_s:
                    hero.MOVE["DOWN"] = False
                if event.key == pygame.K_a:
                    hero.MOVE["LEFT"] = False
                if event.key == pygame.K_d:
                    hero.MOVE["RIGHT"] = False

        pygame.display.flip()
        clock.tick(60)

run()
