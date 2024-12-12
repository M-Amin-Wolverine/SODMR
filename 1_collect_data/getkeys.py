# Citation: Box Of Hats (https://github.com/Box-Of-Hats )

import win32api as wapi  

# Define a list of keys to check for. Start with backspace.  
keyList = ["\b"]  

# Add the characters you want to monitor  
keyList.extend("ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'£$/\\")  # Using extend for clarity  

def key_check():  
    """  
    Checks which keys from the keyList are currently pressed.  
    
    :return: A list of currently pressed keys.  
    """  
    keys = []  
    for key in keyList:  
        if wapi.GetAsyncKeyState(ord(key)) < 0:  # Check if the key is pressed  
            keys.append(key)  
    return keys  # No colon at the end of the return statement
