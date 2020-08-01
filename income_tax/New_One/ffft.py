import os
import cv2
import numpy as np
from PIL import Image
recognizer=cv2.face.LBPHFaceRecognizer_create()
path='dataSet'
def getImagesWithID(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    ids=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L')
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces.append(faceNp)
        ids.append(ID)
        cv2.imshow('trainning',faceNp)
        cv2.waitKey(2)
    return np.array(ids), faces

ids,faces=getImagesWithID(path)
recognizer.train(faces, ids)
recognizer.save('recognizer/trainningData.yml')
cv2.destroyAllWindows()