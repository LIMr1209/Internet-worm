from pytesseract import image_to_string
from PIL import Image
image = Image.open('ocr.jpg')
result = image_to_string(image)
print(result)
