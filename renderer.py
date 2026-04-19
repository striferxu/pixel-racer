"""
渲染器 - 绘制赛车精灵
"""
import pygame
import math

class CarRenderer:
    def __init__(self):
        self.car_surface = self._create_car_sprite()

    def _create_car_sprite(self):
        surf = pygame.Surface((40, 20), pygame.SRCALPHA)
        # 车壳
        pygame.draw.rect(surf, (220, 20, 20), (2, 6, 36, 8))
        pygame.draw.rect(surf, (200, 20, 20), (4, 8, 32, 4))
        # 车顶
        pygame.draw.rect(surf, (180, 20, 20), (10, 2, 20, 8))
        # 车窗
        pygame.draw.rect(surf, (30, 60, 120), (12, 4, 16, 4))
        # 车轮（四个轮子）
        wheel_w, wheel_h = 6, 4
        pygame.draw.rect(surf, (30, 30, 30), (0, 4, wheel_w, wheel_h))
        pygame.draw.rect(surf, (30, 30, 30), (0, 12, wheel_w, wheel_h))
        pygame.draw.rect(surf, (30, 30, 30), (34, 4, wheel_w, wheel_h))
        pygame.draw.rect(surf, (30, 30, 30), (34, 12, wheel_w, wheel_h))
        return surf

    def draw(self, surface, body, camera_offset):
        pos = body.position
        pos_screen = pygame.Vector2(pos.x, pos.y) + pygame.Vector2(camera_offset.x, camera_offset.y)
        angle = body.angle

        rotated = pygame.transform.rotozoom(self.car_surface, -math.degrees(angle), 1)
        rect = rotated.get_rect(center=(int(pos_screen.x), int(pos_screen.y)))
        surface.blit(rotated, rect.topleft)

        # 漂移时在轮胎位置画烟雾（简单版本：不依赖粒子系统）
        if self._get_car_state(body).get('drifting', False):
            pass  # 粒子系统会处理，这里省略

    def _get_car_state(self, body):
        # 临时方法，实际应从car引用获取drifting状态
        return {}
