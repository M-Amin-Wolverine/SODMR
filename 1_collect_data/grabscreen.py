# Done by Frannecklp

import cv2  
import numpy as np  
import win32gui  
import win32ui  
import win32con  
import win32api  

def grab_screen(region=None):  
    """  
    Captures a screenshot of the screen or a specified region.  
    
    :param region: Optional; a tuple (left, top, x2, y2) defining the rectangular region to capture.  
                   If None, capture the entire screen.  
    :return: Captured image as a NumPy array in RGB format.  
    """  
    hwin = win32gui.GetDesktopWindow()  

    if region:  
        left, top, x2, y2 = region  
        width = x2 - left + 1  
        height = y2 - top + 1  
    else:  
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)  
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)  
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)  
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)  

    hwindc = win32gui.GetWindowDC(hwin)  
    srcdc = win32ui.CreateDCFromHandle(hwindc)  
    memdc = srcdc.CreateCompatibleDC()  
    bmp = win32ui.CreateBitmap()  
    bmp.CreateCompatibleBitmap(srcdc, width, height)  
    memdc.SelectObject(bmp)  
    memdc.BitBlt((0, 0), (width, height), srcdc, (left, top), win32con.SRCCOPY)  

    # Fetch the image in an array format  
    signedIntsArray = bmp.GetBitmapBits(True)  
    img = np.frombuffer(signedIntsArray, dtype='uint8')  # Updated from np.fromstring to np.frombuffer  
    img.shape = (height, width, 4)  

    # Clean up resources  
    srcdc.DeleteDC()  
    memdc.DeleteDC()  
    win32gui.ReleaseDC(hwin, hwindc)  
    win32gui.DeleteObject(bmp.GetHandle())  

    return cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)  # Convert BGRA to RGB and return
