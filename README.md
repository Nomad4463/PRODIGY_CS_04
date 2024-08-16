# Keylogger Python Script

This project provides a simple keylogger implemented in Python using the `pynput` library. The keylogger records keystrokes and saves them to a text file. This script is intended for educational purposes and should be used responsibly.

## Features

- Logs all keystrokes.
- Saves keystrokes to a file named `keylog.txt`.
- Stops logging when the `Esc` key is pressed.

## Requirements

- Python 3.x
- `pynput` library

## Installation

1. **Install the required library:**
   ```bash
   pip install pynput
   ```

2. **Run the script:**
   ```bash
   python keylogger.py
   ```

3. **The keylogger will run in the background and log keystrokes to `keylog.txt`. To stop the keylogger, press the `Esc` key.**

4. ## Example Output

After running the keylogger, you might find a `keylog.txt` file that looks like this:

```
Hello [Shift] [a] [Shift] [b] [Enter] How are you? [Space] [World] [Enter] [Esc]
```

In this example:
- `Hello` and `How are you?` are regular text input.
- `[Shift] [a]` indicates that the `Shift` key was held down while pressing `a`.
- `[Enter]` denotes when the Enter key was pressed.
- `[Space]` is the spacebar key.
- `[World]` and `[Esc]` are additional key inputs, with `[Esc]` representing the `Esc` key press that stops the logging.## Example Output

## Important Notes

- This script is intended for educational purposes only.
- Unauthorized use of keyloggers may be illegal and unethical.
- Ensure you have permission to run this script on any machine.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
