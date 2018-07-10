#pytesseract图片识别的库，image_to_string把图片识别成文字
from pytesseract import image_to_string
#PIL图片加载库
from PIL import Image

image = Image.open("./images/test.png")

#把要识别的图片传入
result_text = image_to_string(image)

print("识别出来的文字为：\n",result_text)
