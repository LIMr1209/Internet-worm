import requests
from lxml import etree
import os

#第二个信息
def save(img_url, desc):
    response = requests.get(img_url)
    if not os.path.exists('images'):
        os.mkdir('images')
    if not os.path.exists('text'):
        os.mkdir('text')

    img_url = img_url.split('/')
    image_file_name = img_url[len(img_url) - 1]#保存图片的名称
    file_name = image_file_name.replace('jpg', 'txt')#保存文本的名称
	 #保存图片信息
    with open('images/' + image_file_name, 'wb') as f:
        f.write(response.content)


	 #老师的信息
    with open('text/' + file_name, 'w') as f:
        f.write(desc)
    print('保存成功', image_file_name)
    print('保存成功', file_name)


def main():
    url = 'http://www.atguigu.com/teacher.shtml'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
    response = requests.get(url, headers=headers)
    html_obj = etree.HTML(response.content)
	 #老师所以的图片
    result_list = html_obj.xpath('//div[@class="teacher_content"]/img/@src')

    for i in range(len(result_list)):
        print(i)
		  #找对应老师的文本信息
        img_url = 'http://www.atguigu.com/' + result_list[i]#图片链接
        xpath = '//div[@class="teacher_content"][' + str(i + 1) + ']/text()'
        print("xpath===",xpath)
        result_list1 = html_obj.xpath(xpath)
        print(result_list1)
        desc = "".join(result_list1).lstrip()#某一个老师的信息
        # print('\r\n'.join(result_list1))
        # print(desc)
        print(img_url)
        save(img_url, desc)


if __name__ == '__main__':
    main()