# import
import pandas as pd
import os
import cv2
from sklearn.preprocessing import LabelEncoder
import catScanner
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.camera import Camera
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.animation import Animation
from kivy.clock import Clock
from kivy.core.audio import SoundLoader


class ImageButton(ButtonBehavior, Image):
    pass


class SayHello(App):
    def build(self):
        df_labels = pd.read_csv("labelsCats.csv")
        self.breed_dictionary = list(df_labels["breed"].value_counts().keys())
        self.camera_obj = Camera()
        self.camera_obj.resolution = (800, 800)
        self.countdown = 0
        self.cat_change_complete = False

        self.cat_breed_name = "Nothing"

        self.image = Image(
            source="ui_pictures/catfunnyimage.png", width=500, allow_stretch=True
        )

        self.button_obj = ImageButton(source="ui_pictures/emptybox.png")
        self.button_obj.size_hint = (0.5, 0.2)
        self.button_obj.pos_hint = {"x": 0.25, "y": 0.05}
        self.button_obj.bind(on_press=self.take_selfie)

        self.exit_button = Button(text="Exit")

        self.greeting = Label(text="", font_size=30, color="#00FFCE")

        self.layout = FloatLayout()
        self.layout.add_widget(self.camera_obj)

        self.layout.add_widget(self.image)

        Clock.schedule_interval(self.catChange, 1.0)
        self.layout.add_widget(self.button_obj)
        self.layout.add_widget(self.greeting)
        return self.layout

    def take_selfie(self, *args):

        self.camera_obj.export_to_png("images/selfie.jpg")
        catScan = catScanner.CatScanner(
            "model", "images/selfie.jpg", 224, self.breed_dictionary
        )
        self.cat_breed_name = catScan.scan_cat()
        self.greeting.text = "I think it's a " + str(self.cat_breed_name)
        self.image.source = "ui_pictures/catfunnyimage3.png"
        self.button_obj.source = "ui_pictures/retrybutton.png"
        self.button_obj.bind(on_press=self.restart)

    def catChange(self, *args):
        if not self.cat_change_complete:
            self.countdown += 1
            print(self.countdown)
            if self.countdown > 7:
                self.image.source = "ui_pictures/catfunnyimage2.png"
                self.button_obj.source = "ui_pictures/scancatbutton.png"
                self.cat_change_complete = True

    def restart(self, *args):
        self.image.source = "ui_pictures/catfunnyimage.png"
        self.button_obj.source = "ui_pictures/emptybox.png"
        self.countdown = 0
        self.cat_change_complete = False
        self.button_obj.bind(on_press=self.take_selfie)
        self.greeting.text = ''


if __name__ == "__main__":
    SayHello().run()
# initializer variables
image_size = 224

encoder = LabelEncoder()

# training images directory
train_folder = "train/"
