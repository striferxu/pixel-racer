# 赛车游戏 (Pixel Racer)

像素风格的2D赛车游戏，模拟真实物理力学，支持漂移和粒子效果。

## 在 Windows 上运行

### 1. 安装 Python
- 去 https://www.python.org/downloads/ 下载 Python 3.12+
- 安装时 **勾选 "Add Python to PATH"** 

### 2. 安装游戏依赖
打开命令提示符（CMD），进入游戏文件夹，运行：

```cmd
pip install pygame pymunk
```

### 3. 运行游戏

```cmd
python main.py
```

### 4. 操作
- **↑** 加速
- **← →** 转向  
- **空格** 漂移
- **ESC** 退出

## 游戏目录上传到Windows
直接把整个 `racing_game` 文件夹复制到你的 Windows 电脑上就行。

## 文件清单
- `main.py` - 游戏主程序
- `game.py` - 游戏基类
- `config.py` - 物理/控制/颜色配置
- `input_handler.py` - 键盘输入
- `physics.py` - 物理引擎（Pymunk）
- `renderer.py` - 赛车像素画
- `track.py` - 椭圆赛道
- `camera.py` - 摄像机跟随
- `particles.py` - 粒子系统（烟雾/速度线）

## 调整手感
编辑 `config.py`：
- `ENGINE_FORCE` - 引擎动力，越大越快
- `GRIP_NORMAL` - 地面抓地力（0-1越大越稳）
- `GRIP_DRIFT` - 漂移抓地力
- `TURN_SPEED` - 转向灵敏度
