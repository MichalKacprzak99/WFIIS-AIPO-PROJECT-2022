import cv2
import os
import requests
import json
from model.utils import safeget
from model.country_dictionary import COUNTRY_DICTIONARY;

class PlateRecognizer:
    def detect(self, img):
        temp_image_file = "./temp.jpg"
        cv2.imwrite(temp_image_file, img)
        with open(temp_image_file, 'rb') as fp:
            response = requests.post(
                'https://api.platerecognizer.com/v1/plate-reader/',
                data=dict(config=json.dumps(dict(region="strict"))),
                files=dict(upload=fp),
                headers={'Authorization': 'Token 95d41d187d311815e122d84135dd9f0217b694a8'})
            plate_region_code = safeget(response.json(), 'results', 0, 'region', 'code')

            fp.close()
            os.remove(temp_image_file)

            if plate_region_code == None:
                return None
            for key, value in COUNTRY_DICTIONARY.items():
                if value['code'] == plate_region_code:
                    return key
            return None
