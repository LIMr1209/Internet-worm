import requests
from lxml import etree
import json


# 网络请求数据
def get_data():
    url = "https://www.qiushibaike.com/8hr/page/1/"
    response = requests.get(url)
    text = response.text
    return text


# 把html页面的数据，提取我们想要的--xpath
def handle_data(html):
    # xpath获取数据
    html = etree.HTML(html)
    # 把数据加入列表
    items = []
    # 得到所以的节点
    node_list = html.xpath('//div[contains(@id,"qiushi_tag")]')
    for node in node_list:
        # 字典
        item = {}
        items.append(item)  # 可以
        # 遍历每个节点，从节点取出用户头像，和用户，段子，点赞和评论数
        user_image = node.xpath('./div/a/img/@src')
        # 用户名
        user_name = node.xpath('./div/a/h2/text()')
        # 段子
        content = node.xpath('./a/div/span/text()')
        # 点赞
        dianzhan = node.xpath('./div[@class="stats"]/span/i/text()')
        # 评论
        commont = node.xpath('./div[@class="stats"]/span/a/i/text()')

        if len(user_image) > 0:
            iamge_url = user_image[0]
            item["iamge_url"] = iamge_url
        # print(iamge_url)

        if len(user_name) > 0:
            user_name = user_name[0]
            item["user_name"] = user_name
        # print(user_name)

        if len(content) > 0:
            content = "".join(content)
            item["content"] = content
        # print(content)

        if len(dianzhan) > 0:
            dianzhan = dianzhan[0]
            # print(dianzhan)
            item["dianzhan"] = dianzhan

        if len(commont) > 0:
            commont = commont[0]
            # print(commont)
            item["commont"] = commont

    print(items)
    return items


# 保存数据
def save(items):
    f = open("qiushi.txt", "w")
    json.dump(items, f, ensure_ascii=False)


def main():
    # 网络得到数据
    text = get_data()
    # 提取数据
    items = handle_data(text)
    # 保存数据
    save(items)


if __name__ == "__main__":
    main()
