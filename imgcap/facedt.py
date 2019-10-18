import cv2
import sys

#cascPath = sys.argv[1]


#video_capture = cv2.VideoCapture(0)


# Capture frame-by-frame
#ret, frame = video_capture.read()
filename = "trumph.jpg"
img = cv2.imread(filename)
cv2.imshow('img', img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faceCascade = cv2.CascadeClassifier("trumph.jpg")
print ("type: ", type(faceCascade))
faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the resulting frame
cv2.imshow('img', img)




# When everything is done, release the capture
#video_capture.release()
#cv2.destroyAllWindows()