# Software Screen Dimmer 🕶️

A lightweight, Python-based software screen dimmer for Windows. 

This tool was created as a workaround for older laptops (or systems with missing/broken display drivers) where the physical hardware brightness controls no longer function. Instead of leaving you stuck at 100% blinding brightness, this app provides a fast, software-level solution.

## 🛠️ How It Works

Since custom code cannot bypass a missing driver to directly control the physical LED backlight, this app uses a two-part software trick:

1. **The "Sunglasses" Overlay:** The app uses `tkinter` to draw a borderless, pitch-black window that covers the entire screen. By adjusting the opacity (alpha channel) of this window using the slider, the screen artificially appears darker, just like putting digital sunglasses over your monitor.
2. **The "Ghost Window" Magic:** If you just put a black window over the screen, it would block all your mouse clicks. To fix this, the app uses `ctypes` to talk directly to the Windows API. It injects the `WS_EX_TRANSPARENT` style flag into the overlay. This turns the black screen into a "ghost," allowing all mouse clicks and keyboard inputs to pass straight through to the desktop and apps underneath.

## ✨ Features
* **Click-Through Design:** Work, play games, and browse the web without the dark overlay interfering with your clicks.
* **Lightweight:** Consumes minimal CPU and RAM (typically under 40MB).
* **Standalone Executable:** Can be run natively on Windows without needing Python installed.
* **Safety Limit:** Darkness is capped at 90% so you don't accidentally turn your screen completely pitch black.

## 🚀 Usage

### For Regular Users (No Python Required)
1. Go to the **Releases** tab on the right side of this repository.
2. Download the latest `dimmer.exe` file.
3. Double-click the file to run it. A small control panel will appear.
4. Adjust the slider to your preferred dimness level. Close the control panel window to exit the app.
*(Note: You can add the shortcut to your `shell:startup` folder to have it run automatically when Windows boots!)*

### For Developers (Run from Source)
1. Clone this repository.
2. Ensure you have Python installed.
3. Run the script directly:
   ```bash
   python dimmer.py

### Known Limitations
Because this is a software-level overlay, the physical hardware backlight is still running at 100% capacity. This means:

Your laptop will consume battery power at the same rate as it would at maximum brightness.

Contrast will be slightly washed out compared to true hardware dimming.

Windows may render the mouse cursor above the overlay, keeping the cursor bright.
