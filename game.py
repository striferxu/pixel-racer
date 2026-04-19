"""
游戏基类
"""
import pygame

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("Pixel Racer")
        self.clock = pygame.time.Clock()
        self.running = True

    def run(self):
        dt = 0
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.update(dt)
            self.draw(self.screen)

            pygame.display.flip()
            dt = self.clock.tick(60) / 1000.0

        pygame.quit()

    def update(self, dt):
        pass

    def draw(self, surface):
        surface.fill((135, 206, 235))
