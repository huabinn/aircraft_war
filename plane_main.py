# @Time : 2022/3/2 9:41
# @Author : binn
# @File : plane_main

import pygame
from plane_spites import *


class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        print("游戏初始化")
        # 创建游戏窗口
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        # 创建游戏时钟
        self.clock = pygame.time.Clock()
        # 调用私有方法，精灵和精灵组的创建
        self.__create_sprites()
        # 设置定时器事件 - 创建敌机 1s
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000)
        pygame.time.set_timer(HERO_FIRE_EVENT, 100)

    def __create_sprites(self):

        # 创建背景精灵和精灵组
        bg1 = BackGround()
        bg2 = BackGround(True)
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

        # 创建英雄的精灵组
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

    def start_game(self):
        print("游戏开始")
        while True:
            # 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)
            # 事件监听
            self.__event_handler()
            # 碰撞检测
            self.__check_collide()
            # 更新/绘制精灵组
            self.__update_sprites()
            # 更新显示
            pygame.display.update()

    # 事件监听
    def __event_handler(self):
        for event in pygame.event.get():
            # 判断事件类型是否是退出事件
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                # print("敌机出现")
                # 创建敌机精灵组
                enemy = Enemy()
                # 将敌机精灵添加到敌机精灵组
                self.enemy_group.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
            # elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            #     print("向右移动")
        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.speed = 4
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.speed = -4
        else:
            self.hero.speed = 0

    # 碰撞检测
    def __check_collide(self):
        # 子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)
        # 敌机撞毁英雄
        enemies = pygame.sprite.groupcollide(self.hero_group, self.enemy_group, False, True)
        if len(enemies) > 0:
            self.hero.kill()
            PlaneGame.__game_over()

    # 更新/绘制精灵组
    def __update_sprites(self):
        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

    @staticmethod
    def __game_over():
        print("游戏结束")
        pygame.quit()
        exit()


if __name__ == "__main__":

    # 创建游戏对象
    game = PlaneGame()

    # 开始游戏
    game.start_game()
