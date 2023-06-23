import ctypes


def get_keyboard_layout():
    # Load the user32.dll library
    user32 = ctypes.windll.LoadLibrary("user32.dll")

    # Get the current thread's input locale identifier
    layout_id = user32.GetKeyboardLayout(user32.GetWindowThreadProcessId(user32.GetForegroundWindow(), 0))

    # Extract the keyboard layout's language identifier
    lang_id = layout_id & 0xFFFF

    return lang_id


def lang_fix():
    kb_layout_ids = {'ru': 1049, 'en': 1033}  # codes of keyboard layout languages
    lang_id = get_keyboard_layout()

    if lang_id == kb_layout_ids['ru']:
        return ['\u0434', '\u0441']  # д & c
    elif lang_id == kb_layout_ids['en']:
        return ['\u006C', '\u0063']  # l & c
    else:
        return 'unknown_language'


if __name__ == '__main__':
    print(get_keyboard_layout())
    print(lang_fix())
