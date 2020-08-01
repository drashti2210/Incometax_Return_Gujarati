import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
m = cv2.VideoCapture(0)
rec=cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer\\trainningData.yml")
id=0
font = cv2.FONT_HERSHEY_SIMPLEX
sampleNum = 0;
while (True):
    ret, img = m.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)
         cv2.putText(img, "recognized", (x, y - 10), font, 0.55, (0, 255, 0), 1)
    cv2.imshow('Face', img)
    cv2.waitKey(0)
    if (cv2.waitKey(1)==ord('q')):
        break
m.release()
cv2.destroyAllWindows()
