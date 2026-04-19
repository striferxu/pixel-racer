"""
主程序 - 集成所有系统
"""
import pygame
import sys
import os
import math
import random

sys.path.insert(0, os.path.dirname(__file__))

from game import Game
from config import *
from input_handler import InputHandler
from physics import PhysicsWorld, CarPhysics
from renderer import CarRenderer
from track import Track
from camera import Camera
from particles import ParticleSystem

class RacingGame(Game):
    def __init__(self):
        super().__init__()
        # 赛道中心
        self.track = Track(WIDTH // 2, HEIGHT // 2, width=400, height=300, road_width=120)
        self.physics_world = PhysicsWorld()
        self.car = CarPhysics(self.physics_world, self.track.cx, self.track.cy + self.track.height//2 - 30)
        self.input_handler = InputHandler()
        self.renderer = CarRenderer()
        self.camera = Camera(WIDTH, HEIGHT)
        self.particles = ParticleSystem()

    def update(self, dt):
        self.input_handler.update()

        # 事件处理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False

        # 输入映射
        keys_bool = {
            'accel': self.input_handler.is_pressed('accel'),
            'brake': self.input_handler.is_pressed('brake'),
            'left': self.input_handler.is_pressed('left'),
            'right': self.input_handler.is_pressed('right'),
            'drift': self.input_handler.is_pressed('drift'),
        }

        # 物理更新
        self.car.update(dt, keys_bool)
        self.physics_world.step(dt)

        pos = self.car.get_position()
        angle = self.car.get_angle()
        speed = self.car.get_speed()

        # 摄像机更新
        self.camera.follow(pos, angle, speed)
        self.camera.update(dt)

        # 粒子效果
        self.particles.update(dt)

        # 漂移时从后轮发射烟雾
        if keys_bool['drift'] and speed > 30:
            fl = self._get_wheel_pos(pos, angle, -1, -1)  # 左后
            fr = self._get_wheel_pos(pos, angle,  1, -1)  # 右后
            self.particles.emit(fl[0], fl[1], count=2, type='smoke')
            self.particles.emit(fr[0], fr[1], count=2, type='smoke')

        # 高速时发射速度线
        if speed > 200 and random.random() < 0.5:
            self.particles.emit(pos.x, pos.y, count=3, type='speed')

    def _get_wheel_pos(self, car_pos, car_angle, side, frontback):
        side_offset = side * 12
        fwd_offset  = frontback * 18
        rel_x = math.cos(car_angle) * fwd_offset - math.sin(car_angle) * side_offset
        rel_y = math.sin(car_angle) * fwd_offset + math.cos(car_angle) * side_offset
        return car_pos.x + rel_x, car_pos.y + rel_y

    def draw(self, surface):
        surface.fill(COLOR_SKY)

        # 赛道（带摄像机偏移）
        self.track.draw(surface, self.camera.offset)

        # 粒子
        self.particles.draw(surface, self.camera.offset)

        # 赛车
        self.renderer.draw(surface, self.car.body, self.camera.offset)

        # UI
        self._draw_ui(surface)

    def _draw_ui(self, surface):
        font = pygame.font.Font(None, 36)
        speed = int(self.car.get_speed())
        text = font.render(f"Speed: {speed} km/h", True, (255, 255, 255))
        surface.blit(text, (10, 10))
        if self.car.drifting:
            drift = font.render("DRIFTING!", True, (255, 200, 0))
            surface.blit(drift, (10, 50))
        # 小地图（简单）
        minimap = pygame.Surface((150, 150))
        minimap.fill((34, 139, 34))
        px = int(75 + (self.car.get_position().x - self.track.cx) / (self.track.width/2) * 70)
        py = int(75 + (self.car.get_position().y - self.track.cy) / (self.track.height/2) * 70)
        pygame.draw.circle(minimap, (255, 0, 0), (px, py), 4)
        surface.blit(minimap, (WIDTH - 160, 10))

if __name__ == "__main__":
    game = RacingGame()
    game.run()
