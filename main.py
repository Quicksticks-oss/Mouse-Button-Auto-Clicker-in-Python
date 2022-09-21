from pynput.mouse import Button, Controller, Listener
import threading
import time

auto_btn = None
pressed_btn = False
started = False

def on_click(x, y, button, pressed):
    global auto_btn
    global pressed_btn
    if auto_btn != None:
        if auto_btn == button:
            pressed_btn = pressed
            print(pressed_btn)
    else:
        auto_btn = button
        print('Set button to:', button)

def auto_click():
    global pressed_btn
    mouse = Controller()

    while not started:
        time.sleep(0.1)
    while True:
        while pressed_btn:
            mouse.click(Button.left)
            time.sleep(0.01)
        time.sleep(0.25)

for x in range(2):
    t = threading.Thread(target=auto_click)
    t.start()
    print(x, end='\r')

started = True

print('Press any mouse button to set as autoclick hotkey.')

with Listener(on_click=on_click) as listener:
    listener.join()
