import cv2
import numpy as np

class Camera:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)

    def updateCamera(self):
        ret, frame = self.capture.read()
        cv2.imshow('frame', frame)
