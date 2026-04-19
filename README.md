# 赛车游戏 - README

## 项目简介
一个像素风格的2D赛车游戏，模拟真实物理力学，支持漂移、粒子效果和动态摄像机。

## 核心特性
- **物理模拟**：Pymunk刚体物理引擎，包含引擎动力、刹车、空气阻力、侧向抓地力
- **漂移系统**：空格键激活低抓地力模式，实现逼真甩尾效果
- **粒子特效**：漂移时产生轮胎烟雾，高速时出现速度线
- **动态摄像机**：平滑跟随赛车，随速度偏移视角
- **椭圆赛道**：闭合环形赛道，带有边界线和终点标志

## 操作指南
- **↑ / W**：加速
- **↓ / S**：刹车 / 倒车
- **← → / A D**：左右转向
- **空格**：手刹漂移
- **ESC**：退出游戏

## 项目结构
```
racing_game/
├── main.py          # 游戏主循环
├── game.py          # 游戏基类
├── config.py        # 游戏配置
├── input_handler.py # 输入处理
├── physics.py       # 物理引擎（Pymunk）
├── renderer.py      # 赛车渲染
├── track.py         # 赛道绘制
├── camera.py        # 摄像机系统
├── particles.py     # 粒子系统
└── venv/            # Python虚拟环境
```

## 运行方法
```bash
cd ~/.Hermes/workspace/racing_game
source venv/bin/activate
python main.py
```

## 物理参数调校
可在`config.py`中修改：
- `CAR_MASS`：车重（kg）
- `ENGINE_FORCE`：引擎动力（N）
- `GRIP_NORMAL`：正常抓地力系数
- `GRIP_DRIFT`：漂移抓地力系数
- `AIR_DRAG`：空气阻力系数
- `TURN_SPEED`：转向速度（弧度/秒）

## 技术栈
- Python 3.12
- Pygame 2.6.1（图形渲染）
- Pymunk 7.2.0（物理引擎）

## 已知问题
- 当前赛道是椭圆形状，比较简单，后续可扩展更多赛道
- 无头环境下无声音输出
- 可能需要调整物理参数以获得更佳手感
