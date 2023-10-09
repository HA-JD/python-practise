import requests
from bs4 import BeautifulSoup
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_response(html, proxies=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.139 Safari/537.36'
    }
    cookies = {
        'XXXXXXXX': 'XXXXXXXXXXXXXXXXXXX',
    }

    # if proxies:
    #     response = requests.get(url=html, headers=headers, cookies=cookies, proxies=proxies, verify=False)
    # else:
    response = requests.get(url=html, headers=headers, cookies=cookies, verify=False)

    resp = response.text
    return resp

if __name__ == '__main__':
    url = "https://hacg.zip/wp/"
    proxies = {
        'http': 'http://127.0.0.1:7890',
        'https': 'http://127.0.0.1:7890',
    }

    resp = get_response(html=url, proxies=proxies)

    href_list = []
    soup = BeautifulSoup(resp, 'html.parser')

    content = '#content > article > header > h1 > a'

    a = soup.select(content)
    bt = soup.select(content)

    with open('output.txt', 'w', encoding='utf-8') as file:
        for i in range(0, len(a)):
            a[i] = a[i].text
            bt[i] = bt[i]['href']
            file.write(a[i] + "\n")
            file.write(bt[i] + "\n")  # 写入每个链接的'href'属性

            # 重新请求href链接前添加1秒延迟
            time.sleep(1)

            # 重新请求href链接
            href_response = get_response(bt[i], proxies=proxies)

            # 使用BeautifulSoup解析href链接的响应
            href_soup = BeautifulSoup(href_response, 'html.parser')
            # 使用文本内容来提取所需的数据
            img_paragraphs = href_soup.find_all('p')

            for paragraph in img_paragraphs:
                img_tag = paragraph.find('img')
                if img_tag:
                    text = paragraph.get_text()
                    file.write(text + "\n" + '\n')
