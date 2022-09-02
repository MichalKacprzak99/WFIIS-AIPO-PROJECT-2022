import cv2
import requests
import pandas as pd
import json
from model.utils import plate_convert, safeget

class PlateRecognizer:
    def __init__(self) -> None:
        # Gathering data from .csv file
        data = pd.read_csv('./model/model_files/rg_codes.csv', sep = ';', header=None).to_numpy()
        # Removing the first item (obsolete header)
        indexArray = [i for i in range(1,len(data))]
        data = data[indexArray]
        print(data)

        self.region_codes = plate_convert(data, {})

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
            if plate_region_code == None:
                return None
            return self.region_codes[plate_region_code]
