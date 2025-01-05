import numpy as np
from alexnet import alexnet

# Configuration
WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
MODEL_NAME = f'pygta5-car-fast-{LR}-alexnetv2-{EPOCHS}-epochs-300K-data.model'

# Initialize the model
model = alexnet(WIDTH, HEIGHT, LR)

# Load training data
train_data_path = "pygta5-motorcycle-training-data-and-model/training_data/training_data-1-balanced.npy"
train_data = np.load(train_data_path, allow_pickle=True)

# Split data into training and testing sets
train = train_data[:-100]
test = train_data[-100:]

# Prepare training data
X = np.array([i[0] for i in train]).reshape(-1, WIDTH, HEIGHT, 1)
Y = [i[1] for i in train]

# Prepare testing data
test_x = np.array([i[0] for i in test]).reshape(-1, WIDTH, HEIGHT, 1)
test_y = [i[1] for i in test]

# Train the model
model.fit(
    {'input': X}, {'targets': Y},
    n_epoch=EPOCHS,
    validation_set=({'input': test_x}, {'targets': test_y}),
    snapshot_step=500,
    show_metric=True,
    run_id=MODEL_NAME
)

# Save the model
model.save(MODEL_NAME)

print("Training complete.")
print("Model saved as:", MODEL_NAME)

# Command to run TensorBoard
print("Run the following command to launch TensorBoard:")
print("tensorboard --logdir=D:\\devel\\gta\\log")
