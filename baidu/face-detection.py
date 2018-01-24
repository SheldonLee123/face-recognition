# -*- coding: UTF-8 -*-  

from aip import AipFace
import cv2
import matplotlib.pyplot as plt

# 定义常量
APP_ID = '10724207'
API_KEY = 'SMX2M0Hi7TZp7PpK4NoX6hW2'
SECRET_KEY = '3rM1LCiTpvxzwOxGfWXKpstX3FPOtkXT'

# 初始化AipFace对象  
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

# 读取图片  
filePath = "../img/image.jpg"


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

        # 定义参数变量


options = {
    'max_face_num': 1, # 图像数量
    'face_fields': "age,beauty,expression,faceshape,gender",
}
# 调用人脸属性检测接口  
result = aipFace.detect(get_file_content(filePath), options)

#print(result)
#print(type(result))

# 解析位置信息
location=result['result'][0]['location']
left_top=(location['left'],location['top'])
right_bottom=(left_top[0]+location['width'],left_top[1]+location['height'])

age = result['result'][0]['age']
beauty = result['result'][0]['beauty']
gender = result['result'][0]['gender']
expression = result['result'][0]['expression']
faceshape = result['result'][0]['faceshape'][0]['type']
print "age:",age
print "beauty:",beauty
print "gender:",gender
print "expression:",expression    #表情，0，不笑；1，微笑；2，大笑。
print "facetype:",faceshape

img=cv2.imread(filePath)
cv2.rectangle(img,left_top,right_bottom,(0,0,255),2)

cv2.imshow('img',img)
cv2.waitKey(0)
# plt.imshow(img,"gray")
# plt.show()
