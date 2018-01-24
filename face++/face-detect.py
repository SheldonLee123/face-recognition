# -*- coding: utf-8 -*-

import requests  
from json import JSONDecoder  
import cv2  
import os  
  
http_url ="https://api-cn.faceplusplus.com/facepp/v3/detect"  
# your key and your secret
key ="x"  
secret ="x"      
                   
filepath = "../img/image.jpg"  
data = {"api_key":key, "api_secret":secret, "return_landmark":"1"}  
files = {"image_file":open(filepath, "rb")}  
response = requests.post(http_url, data=data, files=files)  
req_con = response.content.decode('utf-8')  
req_dict = JSONDecoder().decode(req_con)  
print (len(req_dict[u'faces']))  
  
face_num = len(req_dict[u'faces'])  
frame = cv2.imread(filepath)  
for i in range(face_num):  
    box = req_dict[u'faces'][i][u'face_rectangle']  
    print(box)  
    x, y, w, h = box[u'left'], box[u'top'],box[u'width'],box[u'height']  
    color = (0, 255, 0)  
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)  
#显示图像  
cv2.imshow("faceDetecion", frame)          
c = cv2.waitKey(0)  

cv2.destroyAllWindows()   
