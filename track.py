"""
赛道 - 环形椭圆赛道
"""
import pygame
import math

class Track:
    def __init__(self, center_x, center_y, width=400, height=300, road_width=120):
        self.cx = center_x
        self.cy = center_y
        self.road_w = road_width
        self.road_h = height
        self.width = width
        self.height = height
        self.border_w = 4

    def draw_to_surface(self, surface, camera_offset):
        """绘制赛道，接受摄像机偏移"""
        # 变换赛道路径点
        self.draw(surface, camera_offset)

    def draw(self, surface, camera_offset=(0, 0)):
        ox, oy = camera_offset
        cx, cy = self.cx + ox, self.cy + oy
        a = self.width // 2
        b = self.height // 2

        # 草地背景（全屏）
        surface.fill((34, 139, 34))

        # 绘制多层椭圆实现立体道路效果
        layers = 3
        for i in range(layers):
            color = (50 + i*5, 50 + i*5, 50 + i*5)
            w = self.road_w + i * 10
            h = self.road_h + i * 10
            rect = pygame.Rect(cx - w//2, cy - h//2, w, h)
            pygame.draw.ellipse(surface, color, rect)

        # 绘制白色边框（内外）
        border_color = (255, 255, 255)
        outer_w = self.road_w
        outer_h = self.road_h
        outer_rect = pygame.Rect(cx - outer_w//2, cy - outer_h//2, outer_w, outer_h)
        pygame.draw.ellipse(surface, border_color, outer_rect, self.border_w)

        inner_w = self.road_w - self.border_w * 2
        inner_h = self.road_h - self.border_w * 2
        inner_rect = pygame.Rect(cx - inner_w//2, cy - inner_h//2, inner_w, inner_h)
        pygame.draw.ellipse(surface, border_color, inner_rect, self.border_w)

        # 中心虚线
        dash_len = 30
        gap_len = 20
        for angle in range(0, 360, dash_len + gap_len):
            rad = math.radians(angle)
            x1 = cx + math.cos(rad) * (self.road_w//2 - self.border_w - 1)
            y1 = cy + math.sin(rad) * (self.road_h//2 - self.border_w - 1)
            x2 = cx + math.cos(rad) * (self.road_w//2 - self.border_w - 1 - dash_len)
            y2 = cy + math.sin(rad) * (self.road_h//2 - self.border_w - 1 - dash_len)
            pygame.draw.line(surface, (255, 255, 255), (x1, y1), (x2, y2), 2)

        # 绘制终点线
        start_angle = math.radians(0)
        end_x = cx + math.cos(start_angle) * (self.road_w//2 - 10)
        end_y = cy + math.sin(start_angle) * (self.road_h//2 - 10)
        pygame.draw.line(surface, (255, 0, 0), (end_x, end_y), (end_x - 20, end_y), 4)
