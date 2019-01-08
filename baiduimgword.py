# -*- coding: utf-8 -*-
"""
接百度图片文字识别api来识别图片中的文字
"""
# @Time    : 2018/
# @Author  : Macus
# @Email   : 13720433512@163.com    
# @Site    : http://www.wei1011.club
# @File    : baiduimgword.py
# @Software: PyCharm

from aip import AipOcr


def baiduOCR(APP_ID, filename, API_Key, Secret_Key):
    # 识别图片
    client = AipOcr(APP_ID, API_Key, Secret_Key)
    i = open(filename, 'rb')
    print('正在识别: %s'%filename)
    message = client.basicAccurate(i.read())
    print("识别成功")
    i.close()
    for i in message.get('words_result'):
        print(i.get('words'))


if __name__ == "__main__":
    filename = '*.jpg'       # 要识别的图片名
    APP_ID = '*'      # 百度ai中心应用管理里获取
    API_Key = '*'     # 百度ai中心应用管理里获取
    Secret_Key = '*'    # 百度ai中心应用管理里获取
    # access_token = get_token(API_Key, Secret_Key)
    baiduOCR(APP_ID, filename, API_Key, Secret_Key)



