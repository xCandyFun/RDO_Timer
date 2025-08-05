from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:
        print(f"Mouse button pressed: {button}")

with mouse.Listener(on_click=on_click) as listener:
    listener.join()