import time
import subprocess
import platform
from pynput.mouse import Controller

def open_teams_in_edge():
    # Check if the operating system is macOS
    if platform.system() == "Darwin":
        # Open Microsoft Teams in Microsoft Edge
        subprocess.Popen(["/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
                          "https://teams.microsoft.com"])

def bring_edge_to_front():
    # Use AppleScript to bring Microsoft Edge to the front on macOS
    if platform.system() == "Darwin":
        applescript = '''
        tell application "Microsoft Edge"
            activate
        end tell
        '''
        subprocess.run(["osascript", "-e", applescript])

def keep_active():
    mouse = Controller()  # Create a mouse controller object

    try:
        while True:
            # Simulate mouse movement to avoid inactivity
            current_position = mouse.position
            mouse.move(1, 1)  # Move the mouse slightly
            mouse.position = current_position  # Move it back to the original position
            # Wait for 5 minutes (300 seconds) before repeating the operation
            time.sleep(300)
    except KeyboardInterrupt:
        print("Interrupted by user.")

if __name__ == "__main__":
    open_teams_in_edge()
    print("Microsoft Teams opened in Microsoft Edge.")
    time.sleep(5)  # Wait for the browser to open fully
    bring_edge_to_front()  # Bring Microsoft Edge to the front
    print("Microsoft Edge is now the active window.")
    print("Keeping active on Teams...")
    keep_active()
