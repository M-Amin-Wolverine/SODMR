import numpy as np  
from PIL import ImageGrab  
import cv2  
import time  

def screen_record():   
    last_time = time.time()  
    while True:  
        # Capture the screen in the specified region  
        printscreen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 480)))  
        
        # Calculate the time taken for the loop  
        print('Loop took {:.2f} seconds'.format(time.time() - last_time))  
        last_time = time.time()  
        
        # Convert the color from BGR to RGB for display  
        cv2.imshow('Screen Capture', cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))  
        
        # Break the loop if 'q' is pressed  
        if cv2.waitKey(25) & 0xFF == ord('q'):  
            cv2.destroyAllWindows()  
            break  

# Start the screen recording function  
if __name__ == "__main__":  
    screen_record()
