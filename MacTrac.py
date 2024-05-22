import rumps
from pynput import keyboard, mouse
import json
import os

rumps.debug_mode(True)  # Hide the Dock icon

SAVE_FILE = os.path.expanduser("~/MacTrac.json")

class KeyClickCounterApp(rumps.App):
    def __init__(self):
        super(KeyClickCounterApp, self).__init__("KeyClickCounter", icon=None, template=None)
        self.keystrokes = 0
        self.left_clicks = 0
        self.right_clicks = 0
        self.load_counts()

        self.menu = [
            "Keystrokes: 0",
            "Left Clicks: 0",
            "Right Clicks: 0"
        ]

    def load_counts(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, 'r') as f:
                data = json.load(f)
                self.keystrokes = data.get('keystrokes', 0)
                self.left_clicks = data.get('left_clicks', 0)
                self.right_clicks = data.get('right_clicks', 0)

    def save_counts(self):
        data = {
            'keystrokes': self.keystrokes,
            'left_clicks': self.left_clicks,
            'right_clicks': self.right_clicks
        }
        with open(SAVE_FILE, 'w') as f:
            json.dump(data, f)

    def update_menu(self):
        self.menu["Keystrokes: 0"].title = f"Keystrokes: {self.keystrokes}"
        self.menu["Left Clicks: 0"].title = f"Left Clicks: {self.left_clicks}"
        self.menu["Right Clicks: 0"].title = f"Right Clicks: {self.right_clicks}"
        self.save_counts()

    def start_listeners(self):
        def on_press(key):
            self.keystrokes += 1
            self.update_menu()

        def on_click(x, y, button, pressed):
            if pressed:
                if button == mouse.Button.left:
                    self.left_clicks += 1
                elif button == mouse.Button.right:
                    self.right_clicks += 1
                self.update_menu()

        self.keyboard_listener = keyboard.Listener(on_press=on_press)
        self.mouse_listener = mouse.Listener(on_click=on_click)

        self.keyboard_listener.start()
        self.mouse_listener.start()

if __name__ == "__main__":
    app = KeyClickCounterApp()
    app.start_listeners()
    app.run()
