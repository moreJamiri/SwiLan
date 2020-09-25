from pynput import keyboard
from pynput.keyboard import Key, Controller
import clipboard
import platform
import time

kb = Controller()

def SwitchLang():
    os = platform.system().lower()
    if os == 'windows':
        with kb.pressed(Key.alt_l):
            kb.press(Key.shift)
            kb.release(Key.shift)
        return False
    else:
        with kb.pressed(Key.cmd):
            kb.press(Key.space)
            kb.release(Key.space)
        return False

def on_activate():
    print('Global hotkey activated!')
    time.sleep(.5)
    with kb.pressed(Key.ctrl):
        kb.press('a')
        kb.release('a')
        kb.press('c')
    kb.release(Key.ctrl)

    kb.press(Key.backspace)
    kb.release(Key.backspace)

    text = clipboard.paste()
    # Swich Language
    SwitchLang()

    kb.type(text)


def for_canonical(f):
    return lambda k: f(l.canonical(k))

hotkey = keyboard.HotKey(
    keyboard.HotKey.parse('<ctrl>+l'),
    on_activate)
with keyboard.Listener(
        on_press=for_canonical(hotkey.press),
        on_release=for_canonical(hotkey.release)) as l:
    l.join()