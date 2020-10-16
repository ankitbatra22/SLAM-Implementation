import cv2
import numpy as np



def canny_video():

    cap = cv2.VideoCapture("highway.mp4")

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        canny = cv2.Canny(blur, 80, 110)

        ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)

        cv2.imshow("car", img)
        cv2.imshow("video feed", mask)

        if cv2.waitKey(1) & 0xFF ==ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

canny_video()