import numpy as np
import cv2
import sys

def faceDetection():
    cap = cv2.VideoCapture(0)
    while(cap.isOpened()):

        ret, img = cap.read()
        img = cv2.flip(img,1)

        face_cascade = cv2.CascadeClassifier('data\haarcascades\haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier('data\haarcascades\haarcascade_eye.xml')

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for (x,y,w,h) in faces:
            img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)


        cv2.imshow('img',img)

        k=cv2.waitKey(10)
        #if cv2.getWindowProperty('img',cv2.WND_PROP_VISIBLE) < 1:
         #   break
        if k == 27 or k == 1048603 :
            break


