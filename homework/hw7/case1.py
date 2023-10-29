import cv2 as cv


class FaceDetector:
    def __init__(self, path: str):
        self.path = path
        self.capture = None

    def preprocess(self):
        self.capture = cv.VideoCapture(self.path)

    @staticmethod
    def detect(frame):
        face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eyes_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gray = cv.equalizeHist(frame_gray)

        faces = face_cascade.detectMultiScale(frame_gray)

        for (x, y, w, h) in faces:
            center = (x + w // 2, y + h // 2)
            frame = cv.ellipse(frame, center, (w // 2, h // 2), 0, 0, 360, (255, 0, 255), 4)
            face_roi = frame_gray[y:y + h, x:x + w]
            eyes = eyes_cascade.detectMultiScale(face_roi)

            for (x2, y2, w2, h2) in eyes:
                eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
                radius = int(round((w2 + h2) / 4))

                frame = cv.circle(frame, eye_center, radius, (255, 0, 0), 4)

        return frame

    def show(self, **kwargs):
        while self.capture.isOpened():
            read, frame = self.capture.read()

            frame = self.resizing(
                frame,
                new_width=kwargs.get('new_width', None),
                new_height=kwargs.get('new_height', None),
            )
            self.detect(frame)
            cv.imshow(kwargs.get('winname', 'FaceDetector'), frame)

            if cv.waitKey(1) == ord('q'):
                break

        self.capture.release()
        cv.destroyAllWindows()

    @staticmethod
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


fd = FaceDetector('video_1.mp4')
fd.preprocess()
fd.show(new_width=400)
