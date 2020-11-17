"""
This file is to open and process the mp4 video to detect the lanes
"""

import cv2
import numpy as np
from laneDetection import apply_canny
from laneDetection import region_of_interest


def show_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            print(x1,x2,y1,y2)
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
            #cv2.addWeighted(image, 0.8, line_image, 1, 0)

    return line_image

#def mapLines()


def open_video():
    cap = cv2.VideoCapture("highway.mp4")
    while cap.isOpened():
        ret, frame = cap.read()
        canny_image = apply_canny(frame)
        cropped_image = region_of_interest(canny_image)
        lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180, 100, np.array([]), 40, 5)


        line_image = show_lines(frame, lines)
        combo_image = cv2.addWeighted(frame, 0.8, line_image, 1, 1)
        #cv2.imshow("lines", line_image)
        cv2.imshow("highlighted", combo_image) #Shows original video with detected lane lines.
        # cv2.imshow("cropped", cropped_image)
        #cv2.imshow("ROI AREA", region_of_interest(cropped_image))
        # cv2.imshow("canny", canny_image)
        # cv2.imshow("video", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


open_video()
