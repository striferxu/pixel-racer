# 🏎️ Pixel Racer

A pixel-art racing game with realistic physics built using PyGame and Pymunk.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## Controls

| Key | Action |
|-----|--------|
| ↑ / W | Accelerate |
| ↓ / S | Brake / Reverse |
| ← / A | Turn Left |
| → / D | Turn Right |
| Space | Drift (Handbrake) |
| ESC | Quit |

## Features

- 🏁 **Realistic physics** — Pymunk physics engine with grip, drag, and drift mechanics
- 🎮 **Drift system** — Space key activates handbrake drift with smoke particles
- 🌍 **Elliptical track** — Race around an oval circuit with boundary collision
- 📊 **Speed HUD** — Real-time speedometer and mini-map
- 🎨 **Pixel art style** — Retro pixel car sprites and 2D rendering

## Installation (Windows)

1. Download the latest `pixel_racer_windows.zip` from [Releases](https://github.com/striferxu/pixel-racer/releases)
2. Extract the ZIP file
3. Run `pixel_racer.exe`

## Installation (Build from source)

### Windows
```batch
pip install pygame pymunk
python main.py
```

### Linux
```bash
pip install pygame pymunk
python main.py
```

## Auto-Build

Windows `.exe` artifacts are automatically built via GitHub Actions on every push to `main`.
Downloads are available on the [Actions](https://github.com/striferxu/pixel-racer/actions) tab.

## Project Structure

```
pixel-racer/
├── main.py           # Game entry point
├── game.py           # Game state management
├── physics.py        # Pymunk physics (car, grip, drift)
├── renderer.py       # Pixel art car rendering
├── track.py          # Elliptical track
├── camera.py         # Smooth camera follow
├── particles.py      # Drift smoke particles
├── input_handler.py  # Keyboard input
├── config.py         # Game parameters
├── requirements.txt  # Dependencies
└── .github/workflows/build.yml  # CI/CD
```

## License

MIT
