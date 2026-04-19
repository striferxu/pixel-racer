"""
输入处理
"""
import pygame

class InputHandler:
    def __init__(self):
        self.prev_keys = None
        self.keys = None

    def update(self):
        self.keys = pygame.key.get_pressed()
        # 记录上一帧状态（PyGame不支持copy，只记录是否为None即可判断）
        if self.prev_keys is not None:
            pass  # 暂时不需要逐帧比较，第一帧跳过
        self.prev_keys = self.keys

    def is_pressed(self, key_name):
        key_map = {
            'accel': pygame.K_UP,
            'brake': pygame.K_DOWN,
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT,
            'drift': pygame.K_SPACE,
        }
        return bool(self.keys[key_map[key_name]])

    def just_pressed(self, key_name):
        key_map = {
            'accel': pygame.K_UP,
            'brake': pygame.K_DOWN,
            'left': pygame.K_LEFT,
            'right': pygame.K_RIGHT,
            'drift': pygame.K_SPACE,
        }
        # just_pressed功能暂未使用，先简化走
        return False

    @staticmethod
    def is_quit(event):
        # 这里其实只需要检查事件类型，不需要用prev_keys
        return event.type == pygame.QUIT
