"""
物理引擎 - 带侧向抓地力的真实赛车物理
"""
import pygame
import pymunk
import math
from config import CAR_MASS, ENGINE_FORCE, BRAKE_FORCE, GRIP_NORMAL, GRIP_DRIFT, AIR_DRAG, TURN_SPEED, TURN_SPEED_DRIFT

class PhysicsWorld:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)

    def step(self, dt):
        self.space.step(dt)

class CarPhysics:
    def __init__(self, world, x, y):
        self.world = world
        self.drifting = False
        self.drift_timer = 0  # 漂移持续时间

        # 刚体
        moment = pymunk.moment_for_box(CAR_MASS, (40, 20))
        self.body = pymunk.Body(CAR_MASS, moment)
        self.body.position = x, y

        # 形状
        shape = pymunk.Poly.create_box(self.body, (40, 20))
        shape.friction = 0.1  # 基础摩擦，实际由侧向力控制
        world.space.add(self.body, shape)
        self.shape = shape

        # 车辆参数
        self.engine_power = ENGINE_FORCE
        self.brake_power = BRAKE_FORCE
        self.turn_speed_normal = TURN_SPEED
        self.turn_speed_drift = TURN_SPEED_DRIFT
        self.side_grip_normal = GRIP_NORMAL
        self.side_grip_drift = GRIP_DRIFT

    def update(self, dt, keys):
        # 加速
        if keys['accel']:
            fx = math.cos(self.body.angle) * self.engine_power
            fy = math.sin(self.body.angle) * self.engine_power
            self.body.apply_force_at_local_point((fx, fy), (0, 0))

        # 刹车/倒车
        if keys['brake']:
            vx, vy = self.body.velocity
            speed = math.sqrt(vx*vx + vy*vy)
            if speed > 5:
                bx = -vx / speed * self.brake_power
                by = -vy / speed * self.brake_power
                self.body.apply_force((bx, by))
            else:
                fx = math.cos(self.body.angle + math.pi) * self.engine_power * 0.3
                fy = math.sin(self.body.angle + math.pi) * self.engine_power * 0.3
                self.body.apply_force_at_local_point((fx, fy), (0, 0))

        # 转向
        if keys['left']:
            turn_speed = self.turn_speed_drift if self.drifting else self.turn_speed_normal
            self.body.angular_velocity = -turn_speed
        if keys['right']:
            turn_speed = self.turn_speed_drift if self.drifting else self.turn_speed_normal
            self.body.angular_velocity = turn_speed

        # 漂移模式
        if keys['drift']:
            self.start_drift()
        else:
            self.end_drift()

        # 侧向抓地力（关键物理）
        self.apply_side_grip(dt)

        # 空气阻力
        vx, vy = self.body.velocity
        speed = math.sqrt(vx*vx + vy*vy)
        if speed > 5:
            drag_x = -vx * AIR_DRAG * speed
            drag_y = -vy * AIR_DRAG * speed
            self.body.apply_force((drag_x, drag_y))

    def apply_side_grip(self, dt):
        """施加侧向力来模拟轮胎抓地力"""
        # 计算侧向向量（垂直于车头方向）
        angle = self.body.angle
        side_vector = pygame.Vector2(-math.sin(angle), math.cos(angle))  # 左手法则

        # 当前速度向量
        vel = pygame.Vector2(self.body.velocity.x, self.body.velocity.y)

        # 计算侧向速度分量
        side_vel = vel.dot(side_vector)

        # 抓地力系数（漂移时低，正常时高）
        grip = self.side_grip_drift if self.drifting else self.side_grip_normal

        # 侧向回复力：阻止侧向滑动
        side_force = -side_vel * grip * CAR_MASS * 2.0

        # 应用侧向力到刚体中心
        fx = side_vector.x * side_force
        fy = side_vector.y * side_force
        self.body.apply_force_at_local_point((fx, fy), (0, 0))

        # 如果漂移，增加一点角动量衰减（模拟甩尾）
        if self.drifting:
            self.body.angular_velocity *= 0.98

    def start_drift(self):
        if not self.drifting:
            self.drifting = True
            self.shape.friction = GRIP_DRIFT
            self.body.angular_damping = 0.5

    def end_drift(self):
        if self.drifting:
            self.drifting = False
            self.shape.friction = GRIP_NORMAL
            self.body.angular_damping = 0.3

    def get_speed(self):
        vx, vy = self.body.velocity
        return math.sqrt(vx*vx + vy*vy) * 3.6

    def get_position(self):
        return self.body.position

    def get_angle(self):
        return self.body.angle
