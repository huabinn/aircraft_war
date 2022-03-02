# @Time : 2022/3/1 17:00
# @Author : binn
# @File : plane_spites.py

import random
import pygame


# 屏幕大小的常量
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)
# 刷新帧率显示
FRAME_PER_SEC = 60
# 创建敌机的定时器常量
CREATE_ENEMY_EVENT = pygame.USEREVENT
# 创建敌机的定时器常量
HERO_FIRE_EVENT = pygame.USEREVENT + 1


# 游戏精灵类
class GameSprite(pygame.sprite.Sprite):
    """飞机大战游戏精灵"""

    def __init__(self, image_name, speed=1):
        # 调用父类的方法
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):

        # 在屏幕上垂直移动
        self.rect.y += self.speed


# 背景类
class BackGround(GameSprite):

    def __init__(self, is_alt=False):
        super().__init__("./images/background.png")
        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        # 调用父类的方法
        super().update()

        # 判断是否移出屏幕，如果移出屏幕，轮播
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -SCREEN_RECT.height


# 敌机类
class Enemy(GameSprite):
    def __init__(self):
        # 调用父类方法，创建敌机精灵，同时指定敌机图片
        super().__init__("./images/enemy1.png")
        # 指定敌机的初始随机速度
        self.speed = random.randint(1, 3)
        # 指定敌机的初始位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0, SCREEN_RECT.width - self.rect.width)

    def update(self):

        # 调用父类方法，保持垂直飞行
        super().update()
        # 判断是否飞出屏幕，飞出，删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()


# 英雄精灵
class Hero(GameSprite):

    def __init__(self):
        # 调用父类方法，设置image及速度
        super().__init__("./images/me1.png", 0)
        # 设置英雄的初始位置
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        # 创建子弹的精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        self.rect.x += self.speed

        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.right >= SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right

    def fire(self):

        for i in (0, 1, 2):
            # 创建子弹精灵
            bullets = Bullet()
            # 设置精灵的位置
            bullets.rect.bottom = self.rect.y - i*10
            bullets.rect.centerx = self.rect.centerx
            self.bullets.add(bullets)


class Bullet(GameSprite):

    def __init__(self):
        super().__init__("./images/bullet1.png", -10)

    def update(self):
        
        super(Bullet, self).update()
        if self.rect.bottom <= 0:
            self.kill()
