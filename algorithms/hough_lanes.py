"""
This file is to open and process the mp4 video to detect the lanes
"""

import cv2
import numpy as np
from utils.laneDetection import apply_canny
from utils.laneDetection import region_of_interest
import os


def show_lines(image, lines):
    line_image = np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            print(x1, x2, y1, y2)
            cv2.line(line_image, (x1, y1), (x2, y2), (0, 255, 0), 10)
            # cv2.addWeighted(image, 0.8, line_image, 1, 0)

    return line_image


def generate_lines(image):
    canny_image = apply_canny(image)
    cropped_image = region_of_interest(canny_image)
    lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180, 100, np.array([]), 40, 5)

    line_image = show_lines(image, lines)
    combo_image = cv2.addWeighted(image, 0.8, line_image, 1, 1)
    return combo_image

