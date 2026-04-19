"""
摄像机系统 - 平滑跟随赛车并支持视角动态偏移
"""
import pygame
import math

class Camera:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.offset = pygame.Vector2(0, 0)
        self.target_offset = pygame.Vector2(0, 0)
        self.position = pygame.Vector2(0, 0)
        self.smoothing = 0.1  # 跟随平滑度

    def follow(self, target_pos, target_angle, speed):
        """
        计算摄像机偏移量
        target_pos: 赛车世界坐标
        target_angle: 赛车朝向（弧度）
        speed: 当前速度
        """
        # 摄像机应该位于赛车后上方
        # 根据速度调整视角倾斜（速度越快，视角越向后）
        look_ahead = 150 + speed * 0.3  # 速度越快，跟得越后
        height_offset = 100 + speed * 0.1

        # 赛车后方向量
        back_dir = pygame.Vector2(-math.cos(target_angle), -math.sin(target_angle))

        # 目标摄像机位置 = 赛车位置 + 后方偏移 + 高度偏移
        target_pos_cam = pygame.Vector2(target_pos) + back_dir * look_ahead
        target_pos_cam.y -= height_offset  # 抬高视角

        # 摄像机位置 = 目标位置 - 屏幕中心
        self.target_offset = -target_pos_cam + pygame.Vector2(self.width / 2, self.height / 2)

    def update(self, dt):
        # 平滑插值更新摄像机偏移
        self.offset += (self.target_offset - self.offset) * self.smoothing * (dt * 60)

    def apply(self, world_pos):
        """将世界坐标转换为屏幕坐标"""
        return pygame.Vector2(world_pos) + self.offset

    def apply_rect(self, rect):
        """将矩形转换为屏幕坐标"""
        return rect.move(self.offset.x, self.offset.y)

    def inverse(self, screen_pos):
        """屏幕坐标转世界坐标"""
        return pygame.Vector2(screen_pos) - self.offset
