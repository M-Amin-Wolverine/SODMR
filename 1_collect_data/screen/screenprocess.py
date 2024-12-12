import numpy as np  
from PIL import ImageGrab  
import cv2  
import time  

def process_img(image):  
    """Process the image: convert to grayscale and apply edge detection."""  
    # Convert to gray  
    processed_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  
    # Edge detection  
    processed_img = cv2.Canny(processed_img, threshold1=200, threshold2=300)  
    return processed_img  

def main():  
    last_time = time.time()  
    while True:  
        # Capture the screen  
        screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 480)))  
        
        # Process the captured image  
        new_screen = process_img(screen)  

        # Display the processed image  
        cv2.imshow('Processed Image', new_screen)  

        # Print the time taken for the frame (optional)  
        print('Frame took {} seconds'.format(time.time() - last_time))  
        last_time = time.time()  

        # Exit the loop if 'q' is pressed  
        if cv2.waitKey(25) & 0xFF == ord('q'):  
            cv2.destroyAllWindows()  
            break  

# Start the main function  
if __name__ == "__main__":  
    main()
