# import
import pandas as pd
import cv2
from sklearn.preprocessing import LabelEncoder
import catScanner
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


class SayHello(App):
    def build(self):
        df_labels = pd.read_csv("labelsCats.csv")
        self.breed_dictionary = list(df_labels["breed"].value_counts().keys())
        self.camera_obj = Camera()
        self.camera_obj.resolution = (800, 800)

        self.cat_breed_name = "Nothing"

        self.image = Image(source="ui_pictures/catfunnyimage2.png")

        button_obj = Button(text="Click Here")
        button_obj.size_hint = (0.5, 0.2)
        button_obj.pos_hint = {"x": 0.25, "y": 0.25}
        button_obj.bind(on_press=self.take_selfie)

        self.exit_button = Button(text="Exit")

        self.greeting = Label(text=self.cat_breed_name, font_size=18, color="#00FFCE")

        layout = FloatLayout()
        layout.add_widget(self.camera_obj)
        layout.add_widget(button_obj)
        layout.add_widget(self.greeting)
        layout.add_widget(self.image)

        return layout

    def take_selfie(self, *args):
        self.camera_obj.export_to_png("images/selfie.jpg")
        catScan = catScanner.CatScanner(
            "model", "images/selfie.jpg", 224, self.breed_dictionary
        )
        self.cat_breed_name = catScan.scan_cat()
        self.greeting.text = self.cat_breed_name


if __name__ == "__main__":
    SayHello().run()
# initializer variables
image_size = 224

encoder = LabelEncoder()

# training images directory
train_folder = "train/"
