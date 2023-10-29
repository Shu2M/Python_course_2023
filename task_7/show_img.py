import cv2 as cv


img = cv.imread('examples/img_1.jpg')

if img is None:
    raise Exception('no img')

res_img = cv.resize(img, (500, 900))

cv.imshow('show img', img)
cv.waitKey(0)
