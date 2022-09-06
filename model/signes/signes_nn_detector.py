import cv2
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np


class SignesNnDetector:
    def __init__(self) -> None:
        self.model_path = "./model/model_files/detector.h5"
        self.model = load_model(self.model_path)

    def detect(self, img):
        image = cv2.resize(img, (224, 224), interpolation=cv2.INTER_LINEAR)
        image = img_to_array(image)
        image = np.expand_dims(image, axis=0)
        # make bounding box predictions on the input image
        preds = self.model.predict(image)[0]
        startX = int(round(preds[0] * img.shape[1]))
        startY = int(round(preds[1] * img.shape[0]))
        endX = int(round(preds[2] * img.shape[1]))
        endY = int(round(preds[3] * img.shape[0]))
        if startX > endX:
            startX, endX = endX, startX
        if startY > endY:
            startY, endY = endY, startY
        return startX, startY, endX, endY
