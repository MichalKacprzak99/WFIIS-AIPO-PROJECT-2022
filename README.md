# WFIIS-AIPO-PROJECT-2022

##
Project setup:
1. Download model - https://drive.google.com/file/d/1sGCZGuL3v4Cq5fDq4DgG99wskgDaWubD/view?usp=sharing and add to folder model/model_files

2. Run console command: python -m spacy download en_core_web_sm

3. Run console command: python model/lang_and_location/download\_packages.py

4. Download tesseract exe from https://github.com/UB-Mannheim/tesseract/wiki.

5. Install this exe in 'C:/Users/YOUR_WINDOWS_USER_NAME/AppData/Local/Programs/Tesseract-OCR'

6. Run console command: pip install pytesseract

7. In the line 11 of model/lang_and_location/detect_langs.py set: 


    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\YOUR_WINDOWS_USER_NAME\AppData\Local\Tesseract-OCR\tesseract"
