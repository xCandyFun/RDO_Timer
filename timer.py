import time
import threading
import tkinter as tk
import keyboard
import sys
import os
from pynput import mouse
from pynput.mouse import Button

from timer_menu import OverlayMenuSettings

OverlayMenuSettings.load_settings()

timer_running = False
start_time = None
overlay_window = None
exit_flag = False
mouse_listener = None

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
    root.wm_attributes("-alpha", OverlayMenuSettings.last_transparency)

    label = tk.Label(root, 
                     text="Stopped", 
                     font=("Helvetica", OverlayMenuSettings.last_font_size), 
                     fg=OverlayMenuSettings.last_color, 
                     bg="black"
                     )
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

def exit_program():
    global overlay_window, exit_flag, mouse_listener
    print("Exiting...")

    exit_flag = True

    try:
        if mouse_listener:
            mouse_listener.stop()
        if overlay_window:
            overlay_window.after(0, overlay_window.quit)
    except Exception as e:
        print(f"Error during exit: {e}")

    #os._exit(0)
    sys.exit(0)

def listen_for_hotkey():
    global mouse_listener
    keyboard.add_hotkey("F9", toggle_timer)
    keyboard.add_hotkey("F10", reset_timer)
    keyboard.add_hotkey("right shift", exit_program)
    keyboard.add_hotkey("F11", lambda: OverlayMenuSettings.open_settings_menu(overlay_window, exit_program))

    print("Press F9 to start/stop the timer.")
    print("Press F10 to reset the timer.")
    print("Press F11 to open Settings menu.")

    mouse_listener = mouse.Listener(on_click=on_click)
    mouse_listener.start()

    while not exit_flag:
        time.sleep(0.1)

overlay_thread = threading.Thread(target=create_overlay)
overlay_thread.start()
threading.Thread(target=listen_for_hotkey, daemon=True).start()
overlay_thread.join()

while not exit_flag:
    time.sleep(1)


