import requests
from PIL import Image
from pytesseract import  image_to_string

image_url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1531069812139&di=8a2850cd07cd1231ace9fa6e4190a1a5&imgtype=0&src=http%3A%2F%2Fs4.sinaimg.cn%2Fmw690%2F003bsgbmgy6R6efoOr1c3"

#请求网络图片
content = requests.get(image_url).content

image_name = "code.jpg"
#保存图片
with open(image_name,"wb") as f:
	f.write(content)

#加载保存过来的图片
image = Image.open(image_name)
#识别后的文本
result_text =  image_to_string(image)

print(result_text)


