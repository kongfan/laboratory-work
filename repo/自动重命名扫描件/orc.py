# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 09:20:00 2018

@author: Administrator
"""


# -*- coding: UTF-8 -*-
 
from aip import AipOcr
import os, sys
import json
 
# 定义常量
APP_ID = '11715414'
API_KEY = '2UlZHG26l1ZZqzfU18YHqjTC'
SECRET_KEY = '781VDLxvKVtTCoebiM1QkCD858C5uGMs'
 
# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)
 
# 读取图片
dir = os.listdir(r'C:\Users\Administrator\Desktop\images')

for filePath in dir:
    
    filePath = 'images\\' + filePath
#filePath = "001_03 副本.jpg"
    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()
 
# 定义参数变量
    options = {
      'detect_direction': 'true',
      'language_type': 'CHN_ENG',
}
 
# 调用通用文字识别接口
    result = aipOcr.basicGeneral(get_file_content(filePath), options)
    #result = result['words_result'][5]

    content = ''
    for i in result['words_result']:
        content=content+'_'+i['words']
        content = content.strip()
    
    #print(i['words'])
#print(content)
    start =content.find('姓')+2
    end = content.find('名')+4
    filename = content[start:end]+".jpg"
    filename = filename.replace(":","")
    filename = filename.replace(">","")
    filename = filename.replace("<","")
    filename = filename.strip()


    print(filename)

    os.rename(filePath,filename)


#print(result['words_result'])
