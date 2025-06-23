# Import necessary libraries
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models, datasets
from tensorflow.keras.utils import to_categorical
import matplotlib.pyplot as plt 

#load the MNIST datasets
(train_images, train_lables), (test_images, test_lables)=datasets.mnist.load_data()

#Preprocessing : Normalize the pixel values to be between 0 and 1
train_images=train_images/255.0
test_images=test_images/255.0

#reshaape the images to (28, 28, 1) as they are grayscale 
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

# Convert labels to categorical one-hot encode formate
train_labels = to_categorical(train_lables)
test_lables = to_categorical(test_lables)

# Build the CNN model
model =models.Sequential()

#First Convolutional layer
model.add(layers.Conv2D(32,(3,3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2,2)))

#Second Convolutional layer
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))

#Third Convolutional layer
model.add(layers.Conv2D(64,(3,3), activation='relu'))

#Flatter the 3d output to 1D and add a Dense layer\
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))

#output layer with 10 neurons for 10 digit classes
model.add(layers.Dense(10, activation='softmax'))

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_data=(test_images, test_lables))

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_lables)
print(f'Test accuracy: {test_acc * 100:.2f}%', f'Test loss: {test_loss * 100:.2f}%')

#Make predictions           
predictions = model.predict(test_images)
print(f'Predicted class for first test image: {np.argmax(predictions[0])}')

plt.imshow(test_images[0].reshape(28, 28), cmap='gray')
plt.title(f'Predicted: {predictions[0].argmax()}, Actual: {test_lables[0]}')
plt.show()
