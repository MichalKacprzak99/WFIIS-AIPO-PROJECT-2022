from model.lang_and_location.detect_langs import *

class LangAndLocationDetector:
    def detect(self, img):
        result = dict()

        image_copy = img.copy()
        
        result_text = find_text_easyocr(image_copy)
        if not result_text:
            return result

        lang = detect_lang(result_text)
        if lang:
            result['lang'] = lang
        
        place_entity = detect_location_from_text_on_sign(result_text)
        
        if place_entity != None: 
            result['countries'] = place_entity.countries
            result['country_cities'] = place_entity.country_cities
            result['country_regions'] = place_entity.country_regions
       
        return result
