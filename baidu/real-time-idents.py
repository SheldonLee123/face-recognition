# -*- coding: UTF-8 -*-  

from aip import AipFace
import face_recognition
import cv2
#This is a demo using baidu API and opencv

# 定义常量
APP_ID = '10724207'
API_KEY = 'SMX2M0Hi7TZp7PpK4NoX6hW2'
SECRET_KEY = '3rM1LCiTpvxzwOxGfWXKpstX3FPOtkXT'

# 初始化AipFace对象  
aipFace = AipFace(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(1)

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

    #save the single frame to local
    cv2.imwrite("../img/real.jpg", rgb_small_frame)

    # Only process every other frame of video to save time
    if process_this_frame:
        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:

            images = {
                get_file_content('../img/sheldon.jpg'),
                get_file_content('../img/real.jpg')
            }

            # See if the face is a match for the known face(s)
            """ 带参数调用人脸比对 """
            result = aipFace.match(images)
            print (result)
            # 解析返回值信息
            if len(result['result']):
            	score = result['result'][0]['score']
            else:
            	score = 0

            name = "Unknown"

            if score > 60:
                name = "sheldon"

            face_names.append(name)

    process_this_frame = not process_this_frame


    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()