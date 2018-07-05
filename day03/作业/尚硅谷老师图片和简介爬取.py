import requests
import re


def main():
    url = 'http://www.atguigu.com/teacher.shtml'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
    response = requests.get(url, headers=headers)
    html = response.content.decode()
    pattern = re.compile('<div class="teacher_content" style="border-top:none;">.*')


if __name__ == '__main__':
    main()
