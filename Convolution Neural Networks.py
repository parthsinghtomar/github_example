#Part 1 = Building the CNN 

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

#initializing the cnn
Classifier = Sequential()

#step 1 = convolution
Classifier.add(Convolution2D(32,3,3,input_shape=(64,64,3),activation='relu'))
#step 2 = Pooling
Classifier.add(MaxPooling2D(pool_size=(2,2)))
#step 3 = flattening
Classifier.add(Flatten())
#step 4 = full connection
Classifier.add(Dense(output_dim=128,activation='relu'))
Classifier.add(Dense(output_dim=1,activation='sigmoid'))
#Compiling the cnn
Classifier.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#Part 2 = Fitting the cnn to the images
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'dataset/training_set',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'dataset/test_set',
        target_size=(64,64),
        batch_size=32,
        class_mode='binary')

Classifier.fit_generator(
        training_set,
        steps_per_epoch=8000,
        epochs=25,
        validation_data=test_set,
        validation_steps=2000)