from copy import deepcopy
from model.plate_recognizer import PlateRecognizer
from model.signes.signes_fc_detector import SignesFcDetector
from model.signes.signes_nn_detector import SignesNnDetector
from model.utils import *

class Predictor:
    def __init__(self) -> None:
        self.signes_fc_detector = SignesFcDetector()
        self.signes_nn_detector = SignesNnDetector()
        self.plate_recognizer = PlateRecognizer()


    def set_up(self) -> None:
        pass
            
    def clear(self) -> None:
        pass

    def predict_for_images(self, image_list):
        # detect signes
        for img in image_list:
            # neural network sometimes returns truncated signe
            # to deal with this issue analythic detector is used to extend rectangle area
            signe_rectangle = self.signes_nn_detector.detect(img)
            res_fc = self.signes_fc_detector.detect(img)
            original_signe_rect = deepcopy(signe_rectangle)

            for rect in res_fc:
                if rectangle_overlap(original_signe_rect, rect):
                    signe_rectangle = expand_rectanle_whit_rect(signe_rectangle, rect)

            # TODO signe_rectangle
            if signe_rectangle[0] == signe_rectangle[2] or signe_rectangle[1] == signe_rectangle[3]:
                print("NIE WYKRYTO ZNAKU")

            plate_region = self.plate_recognizer.detect(img)
            if plate_region == None:
                print("NIE WYKRYTO REJESTRACJI")
            else:
                print(plate_region)
            

