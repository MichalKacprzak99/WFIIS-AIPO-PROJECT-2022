import cv2


class ImageLoader:
    def __init__(self, image_path):
        self.img_path = image_path
        self.image = cv2.imread(image_path)
