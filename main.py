# import
import cv2
import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import load_model, Model
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout, BatchNormalization
from tensorflow.keras.applications.resnet_v2 import ResNet50V2, preprocess_input
import camera

import catScanner
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

cam = camera.Camera()

# cam.update_camera()
    # cv2.waitKey(1)


class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1

        return self.window

if __name__ == "__main__":
    SayHello().run()

# initializer variables
image_size = 224
batch_size = 64
encoder = LabelEncoder()

# training images directory
train_folder = 'train/'

# get panda to read the label
df_labels = pd.read_csv("labelsCats.csv")

# create a list dictionary of each breed label
breed_dictionary = list(df_labels['breed'].value_counts().keys())

# print each unique cat type reading the breeds
print("Total number of unique Cat Breeds:", len(df_labels.breed.unique()))


## model creation starts
# input_for_model = np.zeros((len(df_labels), image_size, image_size, 3), dtype='float32')
#
# for i, id in enumerate(df_labels['id']):
#
#     temp_image = cv2.resize(cv2.imread(train_folder + id + ".jpg", cv2.IMREAD_COLOR), ((image_size, image_size)))
#
#     image_list = preprocess_input(np.expand_dims(np.array(temp_image[..., ::-1].astype(np.float32)).copy(), axis=0))
#
#     input_for_model[i] = image_list
#
# target_for_model = encoder.fit_transform(df_labels["breed"].values)
#
# x_trainingModel, x_testModel, y_trainingModel, y_testModel = train_test_split(input_for_model, target_for_model, test_size=0.2, random_state=42)
#
# train_data_generator = ImageDataGenerator(rotation_range = 45,
#                                          width_shift_range = 0.2,
#                                          height_shift_range = 0.2,
#                                          shear_range = 0.2,
#                                          zoom_range = 0.25,
#                                          horizontal_flip = True,
#                                          fill_mode = 'nearest')
#
# train_image_generator = train_data_generator.flow(x_trainingModel,
#                                              y_trainingModel,
#                                              batch_size=batch_size)
#
# test_data_generator = ImageDataGenerator()
#
# test_generator = test_data_generator.flow(x_testModel,
#                                           y_testModel,
#                                           batch_size=batch_size)
#
# resnet = ResNet50V2(input_shape=[image_size, image_size, 3], weights='imagenet', include_top=False)
#
# for layer in resnet.layers:
#     layer.trainable = False
#
# x = resnet.output
# x = BatchNormalization()(x)
# x = GlobalAveragePooling2D()(x)
# x = Dropout(0.5)(x)
#
# x = Dense(1024, activation='relu')(x)
# x = Dropout(0.5)(x)
#
# predictions = Dense(12, activation='softmax')(x)
#
# model = Model(inputs=resnet.input, outputs=predictions)
#
# epochs = 20
#
# learning_rate = 1e-3
#
# optimizer = RMSprop(learning_rate=learning_rate, rho=0.9)
# model.compile(optimizer=optimizer,
#               loss='sparse_categorical_crossentropy',
#               metrics=["accuracy"])
#
# model.fit(train_image_generator,
#           steps_per_epoch=x_trainingModel.shape[0] // batch_size,
#           epochs=epochs,
#           validation_data=test_generator,
#           validation_steps=x_testModel.shape[0] // batch_size)
#
# model.save("model")

## model training and creation ends ##
catScan = catScanner.CatScanner("model", 'images/c1.jpg', image_size, breed_dictionary)

catScan.scan_cat()
