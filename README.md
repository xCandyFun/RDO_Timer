# Red Dead Online Mission Timer

A lightweight overlay timer for Red Dead Online, triggered manually by keyboard or mouse buttons.

## 🚀 Features

- 🕒 Transparent overlay showing elapsed time
- ⌨️ Start/Stop with `F9` key or side mouse button (`x1`)
- 🔁 Reset timer with `F10` or second side mouse button (`x2`)
- ⏱️ Automatically switches to `MM:SS` format after 1 minute
- 🔧 Minimal, non-intrusive overlay — ideal for gameplay

## 🎮 Use Case

Designed for Red Dead Online players who want a simple visual timer during missions or other in-game activities.

## 💻 Requirements

- Python 3.10+
- Modules:
  - `keyboard`
  - `tkinter` (built-in with Python)
  - `pynput`

Install dependencies with:

```bash
pip install pynput keyboard
```

> Note: On Windows, the script may require **administrator privileges** to listen for global hotkeys.

## 🖱️ Controls

| Action         | Key/Button         |
|----------------|--------------------|
| Start/Stop     | `F9` or `Mouse X1` |
| Reset Timer    | `F10` or `Mouse X2` |
| Exit Program   | **Right Shift**     |

## 📁 File Structure

```
RDO_Timer/
├── timer.py       # Main script
└── README.md      # This file
```

## 🛠️ To Run

1. Open terminal or command prompt.
2. Navigate to the folder with `timer.py`.
3. Run:

```bash
python timer.py
```

Overlay will appear and can be toggled via hotkeys or mouse buttons.

## 🔐 Notes

- This tool is fully external and does **not modify** game files or memory.
- Safe for use with Red Dead Online, but **use at your own risk**.
- Only reads input and displays an overlay.

Made by ME (xCandyFun)
Happy riding! 🤠
