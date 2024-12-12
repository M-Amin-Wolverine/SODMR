import numpy as np  
from PIL import ImageGrab  
import datetime  
import time  
import os  

# Set the file name for saving training data  
file_name = 'training_data.npy'  

# Load previous training data if it exists  
if os.path.isfile(file_name):  
    print('File exists, loading previous data!')  
    training_data = list(np.load(file_name, allow_pickle=True))  
else:  
    print('File does not exist, starting fresh!')  
    training_data = []  

def main():  
    # Countdown before starting  
    for i in range(4, 0, -1):  
        print(i)  
        time.sleep(1)  

    paused = False  
    while True:  
        if not paused:  
            # Capture the screen in the specified region  
            screen = np.array(ImageGrab.grab(bbox=(0, 40, 960, 560)))  
            timing = datetime.datetime.now()  

            # Append the captured screen and the timestamp to the training data  
            training_data.append([screen, timing])  

            # Save training data every 100 entries  
            if len(training_data) % 100 == 0:  
                print(f'Saved {len(training_data)} entries.')  
                np.save(file_name, training_data)  

        # Optional: Add a way to pause the capturing process  
        if cv2.waitKey(1) & 0xFF == ord('p'):  # Press 'p' to pause  
            paused = not paused  
            print('Paused!' if paused else 'Resumed!')  

# Start the main function  
if __name__ == "__main__":  
    main()
