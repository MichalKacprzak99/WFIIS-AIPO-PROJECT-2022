from copy import deepcopy
from model.plate_recognizer import PlateRecognizer
from model.signes.signes_fc_detector import SignesFcDetector
from model.signes.signes_nn_detector import SignesNnDetector
from model.road_side_detector import RoadSideDetector;
from model.utils import *
from model.country_dictionary import COUNTRY_DICTIONARY;

class Predictor:
    def __init__(self) -> None:
        self.signes_fc_detector = SignesFcDetector()
        self.signes_nn_detector = SignesNnDetector()
        self.plate_recognizer = PlateRecognizer()
        self.road_side_detector = RoadSideDetector()

        self.plate_predition_weight = 2.0
        self.signe_predition_weight = 1.0
        self.road_side_additional_weight = 0.5


    def set_up(self) -> None:
        pass
            
    def clear(self) -> None:
        pass

    def predict_for_images(self, image_list):
        predition = dict()
        for img in image_list:
            print("================================================")
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

            plate_pred = self.plate_recognizer.detect(img)
            if plate_pred == None:
                print("NIE WYKRYTO REJESTRACJI")
            else:
                print(f"Plate prediction: {plate_pred}")
                if plate_pred in predition:
                    predition[plate_pred] = predition[plate_pred] + self.plate_predition_weight
                else:
                    predition[plate_pred] = self.plate_predition_weight

            road_side = self.road_side_detector.detect(img)
            print(f"Road Side: {road_side}")
            for p in predition:
                if COUNTRY_DICTIONARY[p]['road'] == road_side:
                    predition[p] = predition[p] + self.road_side_additional_weight

        return predition
            

