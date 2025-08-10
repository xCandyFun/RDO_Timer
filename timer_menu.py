import tkinter as tk

class OverlayMenuSettings:

    last_color = "lime"
    last_font_size = 24
    last_transparency = 0.7

    @staticmethod
    def open_settings_menu(overlay_window, exit_callback):
        """
        Opens a settings menu for the overlay.

        :param overlay_window: The Tkinter root window of the overlay
        :param exit_callback: Function to call when the 'Exit' button is clicked
        """
        if not overlay_window:
            return

        settings_win = tk.Toplevel(overlay_window)
        settings_win.title("Timer Settings")
        settings_win.geometry("300x250")
        settings_win.attributes("-topmost", True)

        color_var = tk.StringVar(value=OverlayMenuSettings.last_color)
        font_size_var = tk.IntVar(value=OverlayMenuSettings.last_font_size)
        transparency_var = tk.DoubleVar(value=OverlayMenuSettings.last_transparency)

        # --- Text Color ---
        tk.Label(settings_win, text="Text Color:").pack(pady=5)
        tk.Entry(settings_win, textvariable=color_var).pack()

        # --- Font Size ---
        tk.Label(settings_win, text="Font Size:").pack(pady=5)
        tk.Entry(settings_win, textvariable=font_size_var).pack()

        # --- Transparency ---
        tk.Label(settings_win, text="Transparency (0.1 - 1.0):").pack(pady=5)
        tk.Entry(settings_win, textvariable=transparency_var).pack()

        # --- Apply Button ---
        def apply_changes():
            try:
                OverlayMenuSettings.last_color = color_var.get()
                OverlayMenuSettings.last_font_size = font_size_var.get()
                OverlayMenuSettings.last_transparency = transparency_var.get()

                overlay_window.label.config(
                    fg=color_var.get(),
                    font=("Helvetica", font_size_var.get())
                )
                overlay_window.attributes("-alpha", transparency_var.get())
            except Exception as e:
                print(f"Error applying changes: {e}")

        tk.Button(settings_win, text="Apply", command=apply_changes).pack(pady=10)
        tk.Button(settings_win, text="Exit", command=exit_callback).pack(pady=10)