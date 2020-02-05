#!/usr/bin/env python3
# coding=utf-8
import json
import os
import os
import sys
import time
import requests
from bs4 import BeautifulSoup


def main():
    # txt_link = ("https://www.xiashu.cc/15916/read_2.html")
    c = 1
    while 1 > 0:
        txt_link = "https://www.xiashu.cc/15916/read_" + str(c) + ".html"
        time.sleep(1)
        response = requests.get(txt_link,timeout=10)
        if response.status_code == 404:
            break
        soup = BeautifulSoup(response.text, "html.parser")
        #charp = soup.find("h1").text
        #ebook_txt = str(soup.find("div", id="chaptercontent").text).replace("listtopad();", "").replace("\n","\n\t")
        #文本内容
        ebook_txt = str(soup.tagStack[0].text).split("下一章")[1][80:].replace("listtopad();", "   ").replace("上一章","__").replace("目录","--")
        # 保存
        if make_dir("txtFloder"):
            with open(file="大主宰.txt", encoding="utf-8", mode='a+') as f:
                f.write(ebook_txt)
        c += 1


DIR_PATH = r"D:\txt"


def make_dir(folder_name):
    """
    新建文件夹并切换到该目录下
    """
    path = os.path.join(DIR_PATH, folder_name)
    if os.path.exists(path):
        os.chdir(path)
        return True
    os.makedirs(path)
    print(path)
    os.chdir(path)
    return True


if __name__ == '__main__':
    main()
