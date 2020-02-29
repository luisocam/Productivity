'''
Title: Image to text
Description: Converts an image into text (EN) using OCR
Author: Luis Ocampo
'''
import os
from PIL import Image
import pytesseract

# Set current working directory
working_dir = os.getcwd()
# Define input image path
image_path = os.path.join(working_dir, 'images', 'scanned_test.png')


# Install tesseract from https://github.com/tesseract-ocr/tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\locampo\AppData\Local\Tesseract-OCR\tesseract.exe'

# Get text from image
output_text = pytesseract.image_to_string(Image.open(image_path), lang='eng')
# Get additional data from texr converted from image
output_df = pytesseract.image_to_data(Image.open(image_path), lang='eng', output_type='data.frame')

# Wrie the text output into a file 
with open('output_text.txt', 'w') as f:
    f.writelines(output_text)

# Save additional data from image to text conversion into an Excel
output_df.to_excel('output_data.xlsx')
