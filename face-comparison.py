# -*- coding: UTF-8 -*-

from aip import AipFace

#定义常亮
APP_ID = '10724207'
API_KEY = 'SMX2M0Hi7TZp7PpK4NoX6hW2'
SECRET_KEY = '3rM1LCiTpvxzwOxGfWXKpstX3FPOtkXT'

#初始化AipFace对象
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

#读取图片
def get_file_content(filepath):
	with open(filepath, 'rb') as fp:
		return fp.read()

images = {
	get_file_content('image0.jpg'),
	get_file_content('image1.jpg')
}

'''可选参数'''
options = {
	'ext_fields': "qualities",
	'image_liveness': "faceliveness,faceliveness",
	'types': "7,7"   #12表示带水印证件照,7表示生活照,13表示证件照片
}

""" 带参数调用人脸比对 """
result = aipFace.match(images, options)

#print result

# 解析返回值信息
score = result['result'][0]['score']
faceliveness = result['ext_info']['faceliveness']
facelive = faceliveness.split(',')
face1 = facelive[0]
face2 = facelive[1] 

print "score:",score
print "image1-faceliveness:",face1
print "image2-faceliveness:",face2