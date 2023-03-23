from keras.utils import plot_model
import tensorflow as tf
import h5py
import numpy as np

file = h5py.File("alien.h5", "r")


def print_dataset(name, obj):
    if isinstance(obj, h5py.Dataset):
        print(name, obj.shape)


print("Groups in the h5 file:")
print("-----------------------")
for group in file:
    print(group)
    print(file[group].visititems(print_dataset))
    print("\n")


# Load the model from the h5 file
model = tf.keras.models.load_model('alien.h5')


# Visualize the model architecture
# plot_model(model, to_file='model.png', show_shapes=True)

# print(model.predict(np.random.rand(1, 32, 32, 3)))

print(model.summary())
