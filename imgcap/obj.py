#obj.py

import cvlib as cv
from cvlib.object_detection import draw_bbox
import sys
import cv2
import os
import face_recognition
filename = "trumph.jpg"
image = cv2.imread(filename)
bbox, label, conf = cv.detect_common_objects(image)

print (bbox, label, conf)

# draw bounding box over detected objects
out = draw_bbox(image, bbox, label, conf)

savename = "trumph_obj.png"
cv2.imwrite(savename, out)
#cv2.destroyAllWindows()



#image = face_recognition.load_image_file("my_picture.jpg")
#face_landmarks_list = face_recognition.face_landmarks(image)

def drawbox():
    count = 0
    for filename in os.listdir("./2019-10-18"):
        print ("origin name: ", filename)
        truename = "./2019-10-18/" + filename
        print ("file name: ", truename)
        image = cv2.imread(truename)
        bbox, label, conf = cv.detect_common_objects(image)
        print (bbox, label, conf)
        out = draw_bbox(image, bbox, label, conf)
        savename = "./2019-10-18-obj/" + filename
        print ("save name: ", savename)
        cv2.imwrite(savename, out)
        count += 1

if __name__ == "__main__":
    drawbox()
