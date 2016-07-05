import cv2
import sys
import numpy as np

class video:
    def __init__(self, registry):
        self.config = registry.get("config")
        self.report = registry.get("log")
        print " Video Sensor Start"
        pass
    def whiteAndBlackImage(self,image,throshold):
        dimensional = np.array(image)
        (d1, d2) = np.shape(dimensional)
        for i in range(d1):
            for j in range(d2):
                if image[i][j] < throshold:
                    image[i][j] = 0
                else:
                    image[i][j] = 255
        return image
    def onlineVideo(self):
        cap = cv2.VideoCapture(0)
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

    def doEncoding(self,image,quality):
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        result, encimg = cv2.imencode('.jpg', image, encode_param)
        if False == result:
            print " Encoding Error"
            self.report.error("file", "Encoding Error", "engine/static/video", True)
            quit()
        return encimg

    def doDecoding(self,image):
        decimg = cv2.imdecode(image, 1)
        return decimg

    def drowImage(self, title, image):
        cv2.imshow(title, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        pass

    def onlineImage(self, mode = "rgb"):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        if mode is "gray":
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        if mode is "BlackAndWhite":
            gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            (thresh, im_bw) = cv2.threshold(gray, 0, 210, 1 | cv2.THRESH_OTSU)
        cap.release()
        cv2.destroyAllWindows()
        if mode is "gray":
            return gray
        elif mode is "BlackAndWhite":
            return im_bw
        return frame
