# locateButtons.py
# locateButtons.py  
import pyautogui  

def click_play_button_off():  
    """  
    Double-click the "play_button_off.PNG" match.  
    Move the mouse cursor off the button to prevent obscuring the button in later checks.  
    """  
    # Locate the button on the screen and double-click it  
    button = pyautogui.locateOnScreen(r'screenshots/play_button_off.PNG')  
    if button is not None:  
        pyautogui.doubleClick(button)  
        pyautogui.moveTo(1000, 1000, duration=0)  # Move cursor away  
    else:  
        print("Play button off not found on the screen.")  

def click_stop_button_off():  
    """  
    Double-click the "stop_button_off.PNG" match.  
    Move the mouse cursor off the button to prevent obscuring the button in later checks.  
    """  
    # Locate the button on the screen and double-click it  
    button = pyautogui.locateOnScreen(r'screenshots/stop_button_off.PNG')  
    if button is not None:  
        pyautogui.doubleClick(button)  
        pyautogui.moveTo(1000, 1000, duration=0)  # Move cursor away  
    else:  
        print("Stop button off not found on the screen.")  

def detect_play_button_on():  
    """  
    Check if the "play_button_on.PNG" can be found, meaning that the macro is running.  
    """  
    return pyautogui.locateOnScreen(r'screenshots/play_button_on.PNG') is not None  

def detect_stop_button_on():  
    """  
    Check if the "stop_button_on.PNG" can be found, meaning that the macro is not running.  
    """  
    return pyautogui.locateOnScreen(r'screenshots/stop_button_on.PNG') is not None
