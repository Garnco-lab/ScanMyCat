import cv2
import numpy as np


class Camera:
    def __init__(self):
        self.capture = cv2.VideoCapture(0)
        self.frame = 0

    def update_camera(self):
        while True:
            ret, self.frame = self.capture.read()
            cv2.imshow('frame', self.frame)
            cv2.waitKey(1)
            if cv2.waitKey(1) & 0xFF == ord('y'):  # save on pressing 'y'
                cv2.imwrite('images/c1.png', self.frame)
                cv2.destroyAllWindows()
                break
        self.capture.release()
