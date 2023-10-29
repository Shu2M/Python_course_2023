import cv2 as cv
from resize import resizing
from detect import detect_and_display

cap = cv.VideoCapture('examples/video_1.mp4')

while cap.isOpened():
    read, frame = cap.read()
    if not read:
        print('невозможно получить кадр')
        break

    frame = resizing(frame, 400)
    detect_and_display(frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
