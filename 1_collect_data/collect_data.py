# M.Amin_Khodadadi  
import numpy as np  
from grabscreen import grab_screen  
import cv2  
import time  
import datetime  
from getkeys import key_check  
import os  

# Multi-hot encoding for key outputs  
key_outputs = {  
    'Z': [1, 0, 0, 0, 0, 0, 0, 0, 0],  
    'S': [0, 1, 0, 0, 0, 0, 0, 0, 0],  
    'Q': [0, 0, 1, 0, 0, 0, 0, 0, 0],  
    'D': [0, 0, 0, 1, 0, 0, 0, 0, 0],  
    'ZQ': [0, 0, 0, 0, 1, 0, 0, 0, 0],  
    'ZD': [0, 0, 0, 0, 0, 1, 0, 0, 0],  
    'SQ': [0, 0, 0, 0, 0, 0, 1, 0, 0],  
    'SD': [0, 0, 0, 0, 0, 0, 0, 1, 0],  
    'NOKEY': [0, 0, 0, 0, 0, 0, 0, 0, 1]  
}  

starting_value = 1  
training_dataset = "training_data_2021-02-16-2"  

# Determine the next available training data file  
while True:  
    file_name = f'training_data/{training_dataset}/training_data-{starting_value}.npy'  
    if os.path.isfile(file_name):  
        print('File exists, moving along', starting_value)  
        starting_value += 1  
    else:  
        print('File does not exist, starting fresh!', starting_value)  
        break  

def keys_to_output(keys):  
    """  
    Convert keys to a multi-hot array.  
    """  
    output = key_outputs['NOKEY']  # Default to NOKEY  
    key_combinations = {  
        ('Z', 'Q'): 'ZQ',  
        ('Z', 'D'): 'ZD',  
        ('S', 'Q'): 'SQ',  
        ('S', 'D'): 'SD',  
        ('Z',): 'Z',  
        ('S',): 'S',  
        ('Q',): 'Q',  
        ('D',): 'D'  
    }  

    for combo, output_key in key_combinations.items():  
        if all(key in keys for key in combo):  
            output = key_outputs[output_key]  
            break  

    return output  

def main(file_name, starting_value):  
    training_data = []  
    print('Starting in 4 seconds...')  
    for i in range(4, 0, -1):  
        print(i)  
        time.sleep(1)  

    paused = False  
    print('STARTING!!!')  

    while True:  
        if not paused:  
            screen = grab_screen(region=(0, 40, 960, 560))  
            screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)  
            screen = cv2.resize(screen, (160, 120))  

            keys = key_check()  
            output = keys_to_output(keys)  
            training_data.append([screen, output])  

            if len(training_data) % 100 == 0:  
                print(f'Training data size: {len(training_data)}')  

            if len(training_data) == 500:  
                np.save(file_name, training_data)  
                print('SAVED')  
                training_data = []  
                starting_value += 1  
                file_name = f'training_data/{training_dataset}/training_data-{starting_value}.npy'  

        keys = key_check()  
        if 'T' in keys:  
            paused = not paused  
            print('Paused!' if paused else 'Unpaused!')  
            time.sleep(1)  

# Start the main function  
main(file_name, starting_value)
