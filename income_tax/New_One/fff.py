import  cv2
import numpy as np
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
m=cv2.VideoCapture(0)
id=input("Enter the id")
sampleNum=0;
while(True):
    ret,img=m.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in faces:
        sampleNum+=1
        cv2.imwrite("dataSet/User."+str(id)+'.'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow('img',img)
    cv2.waitKey(0)
    if sampleNum>2:
        break
m.release()
cv2.destroyAllWindows()