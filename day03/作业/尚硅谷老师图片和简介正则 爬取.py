import requests
import re
import os


def save(img_url, desc):
    response = requests.get(img_url)
    if not os.path.exists('images'):
        os.mkdir('images')
    if not os.path.exists('text'):
        os.mkdir('text')

    img_url = img_url.split('/')
    image_file_name = img_url[len(img_url) - 1]  # 保存图片的名称
    file_name = image_file_name.replace('jpg', 'txt')  # 保存文本的名称
    # 保存图片信息
    with open('images/' + image_file_name, 'wb') as f:
        f.write(response.content)

        # 老师的信息
    with open('text/' + file_name, 'w') as f:
        f.write(desc)
    print('保存成功', image_file_name)
    print('保存成功', file_name)


def main():
    url = 'http://www.atguigu.com/teacher.shtml'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
    response = requests.get(url, headers=headers)
    html = response.content.decode()
    pattern = re.compile(r'<div class="teacher_content".*?>\s*<img src="(.+?)".*?>', re.S)
    result_list = pattern.findall(html)
    pattern = re.compile(r'</div></div>([\s\S]*?)</div>', re.S)
    pattern = re.compile(r'<div >', re.S)
    content_list = pattern.findall(html)
    print(len(content_list),len(result_list))
    # for i in range(len(result_list)):
    #     img_url = 'http://www.atguigu.com/' + result_list[i]
    #     save(img_url, content_list[i])


if __name__ == '__main__':
    main()
