import cv2 as cv
from detect import detect_and_display


img = cv.imread('examples/img_3.jpg')

if img is None:
    raise Exception('no img')

detect_and_display(img)
cv.waitKey(0)
