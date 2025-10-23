# Tic Tac Toe Computer Vision

An interactive Tic Tac Toe game controlled entirely by hand gestures, built with Python, OpenCV, MediaPipe, and cvzone.  
Play against another person or an AI opponent (random or minimax difficulty), using only your hand and a webcam.

---

## Project Overview

The project combines computer vision and simple game AI into an augmented reality experience.  
Players use hand gestures to navigate menus, choose game modes, and place moves directly on the virtual board.

---

## Project Structure

## Project Structure

- `.vscode/` – VSCode configuration files
- `docs/` – Project documentation and progress screenshots
  - [README.md](docs/README.md)
- `game/` – Game logic and AI
  - [_init_.py](game/__init__.py)
  - [ai.py](game/ai.py) – Minimax and random AI
  - [tic_tac_toe.py](game/tic_tac_toe.py) – Core game logic
- `gui/` – User interface and board rendering
  - [board_drawer.py](gui/board_drawer.py)
  - [ui_helpers.py](gui/ui_helpers.py)
- `tracker/` – Hand detection and gesture tracking
  - [hand_tracker.py](tracker/hand_tracker.py)
- [main.py](main.py) – Entry point: initializes camera, UI, and game flow
- [requirements.txt](requirements.txt) – Dependencies for Python environment
- `LICENSE` – License information
- `README.md` – This file


```
tic-tac-computer-vision/
│
├── .vscode/
├── docs/ 
│ └── README.md

├── game/ 
│ ├── __init__.py
│ ├── ai.py
│ └── tic_tac_toe.py
│
├── gui/
│ ├── board_drawer.py
│ └── ui_helpers.py
│
├── tracker/
│ └── hand_tracker.py
│
├── main.py
├── requirements.txt
├── LICENSE 
└── README.md 
```

## Installation and Setup

### Python Version

Use **Python 3.12** (recommended).  
MediaPipe and OpenCV may not be fully compatible with Python 3.13 yet.

---

### Windows

```bash
# 1. Create virtual environment
py -3.12 -m venv venv

# 2. Activate environment
venv\Scripts\Activate.ps1

```

### Linux

```bash
# 1. Create virtual environment
python3.12 -m venv venv

# 2. Activate environment
source venv/bin/activate
```

```bash
# 3. Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Run the program
python main.py
```

windows

py -3.12 -m venv venv

linus/macOS

python3.12 -m venv venv

windows
venv\Scripts\Activate.ps1

linus/macOS
source venv/bin/activate

python -m pip install --upgrade pip


pip install -r requirements.txt

C:\Users\adria\NTNU\Prosjekter\tic-tac-computer-vision\venv\Scripts\Activate.ps1