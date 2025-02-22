import pytesseract
import os
from PIL import Image

# ekhne teeseract open korar jonno ekta cmd command hobye

def convert():
    img = Image.open('img.jpg')
    text = pytesseract.image_to_string(img)
    print(text)

convert()