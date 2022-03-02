# @Time : 2022/3/1 14:57
# @Author : binn
# @File : main

import pygame
from plane_spites import *

pygame.init()

# 创建游戏窗口, 宽480，高700
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
bg = pygame.image.load("./images/background.png")
hero = pygame.image.load("./images/me1.png")
# 加载背景图像数据
screen.blit(bg, (0, 0))
screen.blit(hero, (150, 300))

# 更新屏幕上的显示
pygame.display.update()

# 创建时钟对象
clock = pygame.time.Clock()

# 定义飞机的初始位置
hero_Rect = pygame.Rect(150, 300, 102, 126)

# 创建敌机精灵
enemy = GameSprite("./images/enemy1.png")
# 创建敌机精灵组
enemy_group = pygame.sprite.Group(enemy)

while True:
    # 每秒执行60次
    clock.tick(60)
    # 监听事件
    for event in pygame.event.get():
        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    hero_Rect.y -= 5
    if hero_Rect.y <= -126:
        hero_Rect.y = 700

    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_Rect)

    # 让精灵组调用两个方法
    enemy_group.update()
    #
    enemy_group.draw(screen)

    pygame.display.update()


pygame.quit()
