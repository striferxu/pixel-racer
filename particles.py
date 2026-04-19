"""
粒子系统 - 用于漂移烟雾、速度线等效果
"""
import pygame
import random
import math

class Particle:
    def __init__(self, x, y, vx, vy, life, color, size=3):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.life = life
        self.max_life = life
        self.color = color
        self.size = size

    def update(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.life -= dt

    def is_alive(self):
        return self.life > 0

    def draw(self, surface, camera_offset=(0, 0)):
        alpha = int(255 * (self.life / self.max_life))
        color = (*self.color, alpha) if len(self.color) == 3 else self.color
        # 使用带alpha的surface
        pos = (int(self.x + camera_offset[0]), int(self.y + camera_offset[1]))
        if 0 <= pos[0] < surface.get_width() and 0 <= pos[1] < surface.get_height():
            pygame.draw.circle(surface, color[:3], pos, self.size)

class ParticleSystem:
    def __init__(self):
        self.particles = []

    def emit(self, x, y, count=1, type='smoke'):
        """发射粒子"""
        if type == 'smoke':
            for _ in range(count):
                angle = random.uniform(math.pi, 2 * math.pi)  # 向后喷
                speed = random.uniform(20, 60)
                vx = math.cos(angle) * speed
                vy = math.sin(angle) * speed
                life = random.uniform(0.5, 1.2)
                color = (150, 150, 150)  # 灰色烟雾
                size = random.randint(2, 5)
                self.particles.append(Particle(x, y, vx, vy, life, color, size))
        elif type == 'speed':
            for _ in range(count):
                angle = random.uniform(0, math.pi * 2)
                speed = random.uniform(100, 200)
                vx = math.cos(angle) * speed
                vy = math.sin(angle) * speed
                life = random.uniform(0.2, 0.5)
                color = (255, 255, 200)
                size = random.randint(1, 2)
                self.particles.append(Particle(x, y, vx, vy, life, color, size))

    def update(self, dt):
        for p in self.particles[:]:
            p.update(dt)
            if not p.is_alive():
                self.particles.remove(p)

    def draw(self, surface, camera_offset=(0, 0)):
        for p in self.particles:
            p.draw(surface, camera_offset)

    def clear(self):
        self.particles = []
