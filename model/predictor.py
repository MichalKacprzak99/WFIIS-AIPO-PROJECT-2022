from copy import deepcopy
from model.plate_recognizer import PlateRecognizer
from model.signes.signes_fc_detector import SignesFcDetector
from model.signes.signes_nn_detector import SignesNnDetector
from model.road_side_detector import RoadSideDetector;
from model.lang_and_location_detector import LangAndLocationDetector
from model.utils import *
from model.country_dictionary import COUNTRY_DICTIONARY;
from langcodes import *

class Predictor:
    def __init__(self) -> None:
        self.signes_fc_detector = SignesFcDetector()
        self.signes_nn_detector = SignesNnDetector()
        self.plate_recognizer = PlateRecognizer()
        self.road_side_detector = RoadSideDetector()
        self.lang_and_location_detector = LangAndLocationDetector()

        self.plate_predition_weight = 2.0
        self.signe_predition_weight = 1.0
        
        self.lang_weight = 1.0
        self.country_weight = 1.0
        self.country_city_weight = 1.0
        self.country_region_weight = 0.5 

        self.road_side_additional_weight = 0.5


    def set_up(self) -> None:
        pass
            
    def clear(self) -> None:
        pass

    def predict_for_images(self, image_list):
        predition = dict()
        for img in image_list:
            print("=" * 50)
            # neural network sometimes returns truncated signe
            # to deal with this issue analythic detector is used to extend rectangle area
            signe_rectangle = self.signes_nn_detector.detect(img)
            res_fc = self.signes_fc_detector.detect(img)
            original_signe_rect = deepcopy(signe_rectangle)

            for rect in res_fc:
                if rectangle_overlap(original_signe_rect, rect):
                    signe_rectangle = expand_rectanle_whit_rect(signe_rectangle, rect)

            signe_res = dict()
            if signe_rectangle[0] == signe_rectangle[2] or signe_rectangle[1] == signe_rectangle[3]:
                print("NIE WYKRYTO ZNAKU")
            else:
                signe = img[signe_rectangle[1]:signe_rectangle[3], signe_rectangle[0]:signe_rectangle[2]]
                signe_res = self.lang_and_location_detector.detect(signe)

            whole_img_res = self.lang_and_location_detector.detect(img)

            if signe_res:
                self.lang_weight = self.lang_weight / 2.0
                self.country_city_weight = self.country_city_weight / 2.0
                self.country_region_weight = self.country_region_weight / 2.0
                for c in  COUNTRY_DICTIONARY:
                    if 'lang' in signe_res:
                        if COUNTRY_DICTIONARY[c]["language"] == Language.get(signe_res['lang']).display_name('en').lower():
                            if c in predition:
                                predition[c] = predition[c] + self.lang_weight
                            else:
                                predition[c] = self.lang_weight
                    if 'country_regions' in signe_res and c in signe_res['country_regions']:
                        for c in signe_res['country_regions']:
                            if c in predition:
                                predition[c] = predition[c] + self.country_region_weight
                            else:
                                predition[c] = self.country_region_weight
                    if 'country_cities' in signe_res and c in signe_res['country_cities']:
                        for c in signe_res['country_cities']:
                            if c in predition:
                                predition[c] = predition[c] + self.country_city_weight
                            else:
                                predition[c] = self.country_city_weight

            for c in  COUNTRY_DICTIONARY:
                if 'lang' in whole_img_res:
                    if COUNTRY_DICTIONARY[c]["language"] == Language.get(whole_img_res['lang']).display_name('en').lower():
                        if c in predition:
                            predition[c] = predition[c] + self.lang_weight
                        else:
                            predition[c] = self.lang_weight
                if 'country_regions' in whole_img_res and c in whole_img_res['country_regions']:
                    if c in predition:
                        predition[c] = predition[c] + self.country_region_weight
                    else:
                        predition[c] = self.country_region_weight
                if 'country_cities' in whole_img_res and c in whole_img_res['country_cities']:
                    if c in predition:
                        predition[c] = predition[c] + self.country_city_weight
                    else:
                        predition[c] = self.country_city_weight
                            
            if signe_res:
                self.lang_weight = self.lang_weight * 2.0
                self.country_city_weight = self.country_city_weight * 2.0
                self.country_region_weight = self.country_region_weight * 2.0


            print(f"singe_rs :{signe_res}")
            print(f"whole_img_res :{whole_img_res}")


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
            print(f"Road side: {road_side}")
            for p in predition:
                if COUNTRY_DICTIONARY[p]['road'] == road_side:
                    predition[p] = predition[p] + self.road_side_additional_weight

        return predition
            

