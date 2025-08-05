import time
import threading
import tkinter as tk
import keyboard
from pynput import mouse
from pynput.mouse import Button

timer_running = False
start_time = None
overlay_window = None

def toggle_timer():
    global timer_running, start_time
    if timer_running:
        timer_running = False
        print("Timer stopped")
    else:
        timer_running = True
        start_time = time.time()
        print("Timer Started.")

def reset_timer():
    global timer_running, start_time
    timer_running = False
    start_time = None
    if overlay_window:
        overlay_window.label.config(text="Reset")
    print("Timer Reset.")

def update_timer_label():
    global overlay_window
    if not overlay_window:
        return
    
    if timer_running and start_time is not None:
        elapsed = int(time.time() - start_time)

        if elapsed < 60:
            overlay_window.label.config(text=f"{elapsed}s")
        else:
            minutes = elapsed // 60
            seconds = elapsed % 60
            overlay_window.label.config(text=f"{minutes}:{seconds:02d}")

    elif start_time is None:
        overlay_window.label.config(text="Reset")
    else:
        overlay_window.label.config(text="Stopped")

    overlay_window.after(500, update_timer_label)

def create_overlay():
    global overlay_window
    root = tk.Tk()
    overlay_window = root
    root.title("Timer Overlay")
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.geometry("+100+100")
    root.configure(bg='black')
    root.wm_attributes("-transparentcolor", "black")
    root.wm_attributes("-alpha", 0.7)

    label = tk.Label(root, text="Stopped", font=("Helvetica", 24), fg="lime", bg="black")
    label.pack()
    root.label = label

    update_timer_label()
    root.mainloop()

def on_click(x, y, button, pressed):
    if pressed:
        if button == Button.x1:
            toggle_timer()
        elif button == Button.x2:
            reset_timer()

def listen_for_hotkey():
    keyboard.add_hotkey("F9", toggle_timer)
    keyboard.add_hotkey("F10", reset_timer)
    print("Press F9 to start/stop the timer.")
    print("Press F10 to reset the timer.")

    mouse.Listener(on_click=on_click).start()

    keyboard.wait()

threading.Thread(target=create_overlay, daemon=True).start()
threading.Thread(target=listen_for_hotkey, daemon=True).start()

while True:
    time.sleep(1)


