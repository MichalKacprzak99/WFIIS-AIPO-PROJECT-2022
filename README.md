# WFIIS-AIPO-PROJECT-2022

##
Project setup:

1. Run console command: python -m spacy download en_core_web_sm

2. Run console command: python model/lang_and_location/download\_packages.py

3. Download tesseract exe from https://github.com/UB-Mannheim/tesseract/wiki.

4. Install this exe in 'C:/Users/YOUR_WINDOWS_USER_NAME/AppData/Local/Programs/Tesseract-OCR'

5. Run console command: pip install pytesseract

6. In the line 11 of model/lang_and_location/detect_langs.py set: 


    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\YOUR_WINDOWS_USER_NAME\AppData\Local\Tesseract-OCR\tesseract"
