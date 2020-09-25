from pynput import keyboard
from pynput.keyboard import Key, Controller
import clipboard
import platform
import time

# keyboard controller
keyboard_controller = Controller()


def SwitchLang():
    os = platform.system().lower()
    if os == 'windows':
        with keyboard_controller.pressed(Key.alt_l):
            keyboard_controller.press(Key.shift)
            keyboard_controller.release(Key.shift)
        return False
    else:
        with keyboard_controller.pressed(Key.cmd):
            keyboard_controller.press(Key.space)
            keyboard_controller.release(Key.space)
        return False
# A function to switch language


def copy_text():
    with keyboard_controller.pressed(Key.ctrl):
        keyboard_controller.press('a')
        keyboard_controller.release('a')
        keyboard_controller.press('c')
    keyboard_controller.release(Key.ctrl)
# A function to copy the text


def on_activate():
    time.sleep(.5)
    copy_text()

    keyboard_controller.press(Key.backspace)
    keyboard_controller.release(Key.backspace)

    text = clipboard.paste()
    # Swich Language
    SwitchLang()

    keyboard_controller.type(text)
# this function will run when user press hotkey


def for_canonical(f):
    return lambda k: f(l.canonical(k))


hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+<alt>+s'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()