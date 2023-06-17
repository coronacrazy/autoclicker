import time
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode

# pretty self explanatory (toggle key for autoclicker = f)
TOGGLE_KEY = KeyCode(char='f')

# automatically starts as off
clicking = False
mouse = Controller()

# clicking action
def clicker():
    while True:
        if clicking:
            mouse.click(Button.left, 1)
        time.sleep(0.01)

# determines wether or not the clicker is on
def toggle_event(key):
    if key == TOGGLE_KEY:
        global clicking
        clicking = not clicking


click_thread = threading.Thread(target=clicker)
click_thread.start()

with Listener(on_press=toggle_event) as listener:
    listener.join()
