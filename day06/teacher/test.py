import requests
from PIL import Image
from pytesseract import image_to_string

url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1531069812139&di=8a2850cd07cd1231ace9fa6e4190a1a5&imgtype=0&src=http%3A%2F%2Fs4.sinaimg.cn%2Fmw690%2F003bsgbmgy6R6efoOr1c3"

image_data = requests.get(url).content

with open('code.jpg', 'wb') as f:
    f.write(image_data)

image = Image.open('./code.jpg')

image_text = image_to_string(image)

print(image_text)
