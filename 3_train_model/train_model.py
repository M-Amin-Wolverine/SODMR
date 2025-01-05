import numpy as np
from alexnet import alexnet

# Configuration
training_dataset = "training_data_2021-02-16-1"
WIDTH = 160
HEIGHT = 120
LR = 1e-3
EPOCHS = 10
MODEL_NAME = f'gta-{LR}-alexnetv2-{EPOCHS}-epochs-{training_dataset}.model'

# Initialize the model
model = alexnet(WIDTH, HEIGHT, LR)

for epoch in range(EPOCHS):
    print(f"Epoch {epoch + 1}/{EPOCHS}")

    # Load training data
    train_data = np.load(f"training_data/{training_dataset}-balanced.npy", allow_pickle=True)

    # Split data into training and testing sets
    train = train_data[:-100]
    test = train_data[-100:]

    # Prepare training data
    X = np.array([data[0] for data in train]).reshape(-1, WIDTH, HEIGHT, 1)
    Y = [data[1] for data in train]

    # Prepare testing data
    test_x = np.array([data[0] for data in test]).reshape(-1, WIDTH, HEIGHT, 1)
    test_y = [data[1] for data in test]

    # Train the model
    model.fit(
        {'input': X}, {'targets': Y},
        n_epoch=1,
        validation_set=({'input': test_x}, {'targets': test_y}),
        snapshot_step=500,
        show_metric=True,
        run_id=MODEL_NAME
    )

    # Save the model
    model.save(f"model/{MODEL_NAME}")

print("Training complete.")

# Command to run TensorBoard
print("Run the following command to launch TensorBoard:")
print("tensorboard --logdir=foo:D:\\devel\\gta\\log")
