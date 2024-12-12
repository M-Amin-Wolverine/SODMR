import numpy as np  
from random import shuffle  
import os  

def load_training_data(dataset_folder):  
    """Load and concatenate all training data from the specified folder."""  
    files = os.listdir(dataset_folder)  
    data = [np.load(os.path.join(dataset_folder, file), allow_pickle=True) for file in files]  
    concatenated_data = np.concatenate(data)  
    print("Loaded Training Data: ", concatenated_data.shape)  
    return concatenated_data  

def classify_data(train_data):  
    """Classify data into different categories based on the output label."""  
    classifications = {  
        'Z': [],  
        'S': [],  
        'Q': [],  
        'D': [],  
        'ZQ': [],  
        'ZD': [],  
        'SQ': [],  
        'SD': [],  
        'NOKEY': []  
    }  

    for img, choice in train_data:  
        if choice == [1, 0, 0, 0, 0, 0, 0, 0, 0]:  
            classifications['Z'].append([img, choice])  
        elif choice == [0, 1, 0, 0, 0, 0, 0, 0, 0]:  
            classifications['S'].append([img, choice])  
        elif choice == [0, 0, 1, 0, 0, 0, 0, 0, 0]:  
            classifications['Q'].append([img, choice])  
        elif choice == [0, 0, 0, 1, 0, 0, 0, 0, 0]:  
            classifications['D'].append([img, choice])  
        elif choice == [0, 0, 0, 0, 1, 0, 0, 0, 0]:  
            classifications['ZQ'].append([img, choice])  
        elif choice == [0, 0, 0, 0, 0, 1, 0, 0, 0]:  
            classifications['ZD'].append([img, choice])  
        elif choice == [0, 0, 0, 0, 0, 0, 1, 0, 0]:  
            classifications['SQ'].append([img, choice])  
        elif choice == [0, 0, 0, 0, 0, 0, 0, 1, 0]:  
            classifications['SD'].append([img, choice])  
        elif choice == [0, 0, 0, 0, 0, 0, 0, 0, 1]:  
            classifications['NOKEY'].append([img, choice])  

    return classifications  

def balance_data(classifications):  
    """Balance the dataset based on the least available class."""  
    min_length = min(len(classifications['ZQ']), len(classifications['ZD']))  

    balanced_classes = {  
        'Z': classifications['Z'][:min_length],  
        'ZQ': classifications['ZQ'][:len(classifications['Z'])],  
        'ZD': classifications['ZD'][:min_length],  
        'NOKEY': classifications['NOKEY']  # Keep all NOKEY for training  
    }  
    
    final_data = balanced_classes['Z'] + balanced_classes['ZQ'] + balanced_classes['ZD'] + balanced_classes['NOKEY']  
    shuffle(final_data)  # Shuffle the combined data  

    return final_data  

def save_balanced_data(final_data, dataset_folder):  
    """Save the balanced training data to a .npy file."""  
    np.save(os.path.join(dataset_folder, "-balanced.npy"), final_data)  
    print("Balanced data saved.")  

def main():  
    training_dataset = "training_data_2021-02-16-1"  
    dataset_folder = os.path.join("training_data", training_dataset)  

    train_data = load_training_data(dataset_folder)  
    
    shuffle(train_data)  # Shuffle the training data before processing  
    classifications = classify_data(train_data)  
    
    final_data = balance_data(classifications)  
    save_balanced_data(final_data, dataset_folder)  

# Execute the script  
if __name__ == "__main__":  
    main()
