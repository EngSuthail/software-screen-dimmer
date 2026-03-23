import tkinter as tk
import ctypes

def make_click_through(window):
    window.update()
    inner_hwnd = window.winfo_id()
    hwnd = ctypes.windll.user32.GetParent(inner_hwnd)
    if hwnd == 0:
        hwnd = inner_hwnd
        
    WS_EX_LAYERED = 0x00080000
    WS_EX_TRANSPARENT = 0x00000020
    GWL_EXSTYLE = -20

    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongW(
        hwnd, 
        GWL_EXSTYLE, 
        style | WS_EX_LAYERED | WS_EX_TRANSPARENT
    )

def change_dimness(value):
    # Convert the slider value (0 to 90) into a decimal (0.0 to 0.9)
    # We cap it at 90 so you don't accidentally make the screen 100% pitch black!
    alpha = float(value) / 100.0
    overlay.attributes('-alpha', alpha)

# --- 1. The Control Panel (Main Window) ---
root = tk.Tk()
root.title("Dimmer")
root.geometry("300x80")
root.attributes('-topmost', True) # Keep the slider always visible
root.resizable(False, False)

# The Slider (Scale) widget
slider = tk.Scale(
    root, 
    from_=0, 
    to=90, 
    orient=tk.HORIZONTAL, 
    label="Adjust Darkness %",
    command=change_dimness
)
slider.set(40) # Set default darkness to 40%
slider.pack(fill=tk.X, padx=10, pady=5)

# --- 2. The Dark Overlay (Secondary Window) ---
overlay = tk.Toplevel(root)
overlay.configure(bg='black')
overlay.attributes('-fullscreen', True)
overlay.attributes('-topmost', True)

# Apply the click-through fix ONLY to the overlay
make_click_through(overlay)

# Run the application
root.mainloop()