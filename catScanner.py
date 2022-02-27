from tensorflow.keras.models import load_model, Model
import cv2
import numpy as np
from tensorflow.keras.applications.resnet_v2 import ResNet50V2, preprocess_input


class CatScanner:
    def __init__(self, model, image, image_size, breed_dictionary):
        self.model = load_model(model)
        self.prediction_image_path = image
        self.image_size = image_size
        self.breed_dictionary = breed_dictionary

    def scan_cat(self):
        prediction_image_list = cv2.resize(
            cv2.imread(self.prediction_image_path, cv2.IMREAD_COLOR),
            ((self.image_size, self.image_size)),
        )

        prediction_image_list = preprocess_input(
            np.expand_dims(
                np.array(prediction_image_list[..., ::-1].astype(np.float32)).copy(),
                axis=0,
            )
        )

        # feed the model with the image array for prediction
        pred_val = self.model.predict(np.array(prediction_image_list, dtype="float32"))

        # display the predicted cat breed
        pred_breed = sorted(self.breed_dictionary)[np.argmax(pred_val)]
        print("Predicted Breed for this Cat is :", pred_breed)

        return str(pred_breed)
