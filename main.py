# import
import pandas as pd
import cv2
from sklearn.preprocessing import LabelEncoder
import catScanner
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.boxlayout import BoxLayout


class SayHello(App):
    def build(self):
        df_labels = pd.read_csv("labelsCats.csv")
        self.breed_dictionary = list(df_labels["breed"].value_counts().keys())
        self.camera_obj = Camera()
        self.camera_obj.resolution = (800, 800)

        button_obj = Button(text="Click Here")
        button_obj.size_hint = (0.5, 0.2)
        button_obj.pos_hint = {"x": 0.25, "y": 0.25}
        button_obj.bind(on_press=self.take_selfie)

        layout = BoxLayout()
        layout.add_widget(self.camera_obj)
        layout.add_widget(button_obj)
        return layout

    def take_selfie(self, *args):
        print("I AM TAKING A SELFIE")
        self.camera_obj.export_to_png("images/selfie.jpg")
        catScan = catScanner.CatScanner(
            "model", "images/selfie.jpg", 224, self.breed_dictionary
        )
        catScan.scan_cat()


if __name__ == "__main__":
    SayHello().run()
# initializer variables
image_size = 224

encoder = LabelEncoder()

# training images directory
train_folder = "train/"

# get panda to read the label


# create a list dictionary of each breed label


# print each unique cat type reading the breeds
# print("Total number of unique Cat Breeds:", len(df_labels.breed.unique()))




