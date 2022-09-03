# WFIIS-AIPO-PROJECT-2022

## TODO

- create class to load user's video

## License plate recognition
https://colab.research.google.com/drive/1OFPxE2K5ug0fvS6l1qhk-kKq2R95HesL?usp=sharing

##
Aby zadziałało potrzebujesz pliku detector.h5 (zapytaj Pawła jeśli nie masz dostępu). Plik ten należy wrzucić do folderu model/model\_files.

Potem zrób to:
python -m spacy download en\_core\_web\_sm
python model/lang\_and\_location/download\_packages.py
Download tesseract exe from https://github.com/UB-Mannheim/tesseract/wiki.
Install this exe in 'C:/Users/YOUR\_FANCY\_WINDOWS\_USER\_NAME/AppData/Local/Programs/Tesseract-OCR'
pip install pytesseract
In the line 11 of model/lang\_and\_location/detect\_langs.py set: pytesseract.pytesseract.tesseract\_cmd = r"C:\Users\YOUR\_FANCY\_WINDOWS\_USER\_NAME\AppData\Local\Tesseract-OCR\tesseract"
