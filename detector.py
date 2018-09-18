import cv2,os
import numpy as np
from PIL import Image
import pickle

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer/trainer.yml')
cascadePath = "face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path = 'dataSet'

cam = cv2.VideoCapture(0)
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (1,0, 1, 1)

def predictor():
    while True:
        ret, im =cam.read()
        im = cv2.flip(im,1)
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=15, minSize=(50, 50), flags=cv2.CASCADE_SCALE_IMAGE)
        for(x,y,w,h) in faces:
            nbr_predicted, conf = recognizer.predict(gray[y:y+h,x:x+w])
            cv2.rectangle(im,(x-50,y-50),(x+w+50,y+h+50),(225,0,0),2)

            #cv2.putText(im,str(nbr_predicted)+"--"+str(conf), (x,y+h), fontface,1,(225,225,225)) #Draw the text
            cv2.putText(im,str(nbr_predicted), (x,y+h), fontface,1,(225,225,225))
            cv2.imshow('im',im)
        if cv2.waitKey(10) & 0xFF== 27:
            break
    cam.release()
    cv2.destroyAllWindows()

