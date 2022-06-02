import cv2


class ImageLoader:
    def __init__(self, image_path):
        self.img_path = image_path
        self.original_image = cv2.imread(image_path)
        self.modified_image = cv2.imread(image_path)

    def resize_with_aspect_ratio(self, image, width, height, inter=cv2.INTER_AREA):

        (h, w) = image.shape[:2]

        if width is None or height is None:
            return image

        r = height / float(h)
        dim = (int(w * r), height)

        if dim[0] > width:
            r = width / float(w)
            dim = (width, int(h * r))

        return cv2.resize(image, dim, interpolation=inter)
