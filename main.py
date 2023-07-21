import pygame
from data import *
from shooter import Hero, Bot, Bullet, Boss
from random import randint 

pygame.init()

window = pygame.display.set_mode((setting_win["WIDTH"], setting_win["HEIGHT"]))
pygame.display.set_caption("Shooter")

def run():
    game = True
    time_start = 0
    time_end = 0
    kill_bot_lvl = 0

    font_kill = pygame.font.Font(None, 40)

    hero = Hero(100, 100, 100, 100, speed= 5, color= (132, 33, 77), image= hero_images)
    #bot = Bot(500, 0 - 100, 100, 100, speed= 2, image= bot_images)
    boss = None
    clock = pygame.time.Clock()

    while game:
        window.fill((255, 255, 255))

        x = 10
        for hp in range(hero.HP):
            window.blit(HP_image, (x, 10))
            x += 80

        #HERO
        hero.move(window)
        hero.move_bullet(window)
        window.blit(font_kill.render(f"{hero.KILL}", True, (0, 0, 0)), (setting_win["WIDTH"] - 180, 10))  

        #BOT
        time_end = pygame.time.get_ticks()
        if time_end - time_start > 2000 and hero.KILL_BOT_LVL <= 3:
            bot_list.append(Bot(randint(0, setting_win["WIDTH"] - setting_bot["WIDTH"]), 0 - setting_bot["HEIGHT"], setting_bot["WIDTH"], setting_bot["HEIGHT"],  speed= 2, image= bot_images))
            time_start = time_end

        for bot in bot_list:    
            bot.move(window)
            bot.move_bullet(window, hero)

        #BOSS
        if hero >= 3:
            if not boss:
                boss = Boss(setting_win["WIDTH"] // 2- setting_boss["WIDHT"] // 2,
                            - setting_boss["HEIGHT"],
                            setting_boss["WIDHT"],
                            setting_boss["HEIGHT"],
                            image= boss_images,
                            speed = 1)
            boss.move(window)

        for bullet in bullet_boss_list:
            bullet.move_boss(window)




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
                if event.key == pygame.K_SPACE:
                    hero.BULLETS.append(Bullet(bullet_image, 8, x= hero.x + hero.width // 2 - 40, y= hero.y, width= 10, height= 20))
                    hero.BULLETS.append(Bullet(bullet_image, 8, x= hero.x + hero.width // 2 + 40, y= hero.y, width= 10, height= 20))
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
