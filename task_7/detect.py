import cv2 as cv
from resize import resizing


def detect_and_display(frame):
    face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
    eyes_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_gray = cv.equalizeHist(frame_gray)

    faces = face_cascade.detectMultiScale(frame_gray)

    for (x, y, w, h) in faces:
        center = (x + w // 2, y + h // 2)
        frame = cv.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
        face_roi = frame_gray[y:y+h, x:x+w]

        eyes = eyes_cascade.detectMultiScale(face_roi)
        for (x2, y2, w2, h2) in eyes:
            eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
            radius = int(round((w2 + h2) / 4))

            frame = cv.circle(frame, eye_center, radius, (255, 0, 0), 4)

    frame = resizing(frame, 400)
    cv.imshow('capture face detection', frame)
