import cv2 as cv


def resizing(img_res, new_width=None, new_height=None):
    h, w = img_res.shape[:2]

    if new_width is None and new_height is None:
        return img_res

    if new_width is None:
        ratio = new_height / h
        dimension = (int(w * ratio), new_height)
    else:
        ratio = new_width / w
        dimension = (new_width, int(h * ratio))

    return cv.resize(img_res, dimension)
