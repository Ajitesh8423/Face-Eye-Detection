import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('E:\Projects\haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('E:\Projects\haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (250,0,0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,250,1), 2)

    cv2.imshow('img', img)
    k = cv2.waitKey(40) & 0xff
    if k== 37:
        break

cap.release()
cv2.destroyAllWindows()
