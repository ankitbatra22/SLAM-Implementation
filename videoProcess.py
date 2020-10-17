"""
This file is to open and process the mp4 video to detect the lanes
"""

import cv2
import laneDetection
from laneDetection import apply_canny
from laneDetection import region_of_interest



def openVideo():

    cap = cv2.VideoCapture("highway.mp4")
    while cap.isOpened():
        ret, frame = cap.read()
        canny_image = apply_canny(frame)
        cropped_image = region_of_interest(canny_image)
        cv2.imshow("cropped", cropped_image)
        #cv2.imshow("ROI AREA", region_of_interest(canny_image))
        #cv2.imshow("canny", canny_image)
        #cv2.imshow("video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

openVideo()