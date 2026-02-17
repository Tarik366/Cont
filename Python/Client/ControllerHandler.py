from pyjoystick.sdl2 import Key, Joystick, run_event_loop
import LocalizationHandler

loc = LocalizationHandler.Localization()["controller"]

def new_joystic_plugged():
    print(loc[""])

run_event_loop()
