"""
This file is to detect lanes in the highway.mp4 test video using canny edge detection.
"""

import cv2
import numpy as np


def apply_canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 110, 190)
    return canny


def region_of_interest(image):
    height = image.shape[0]
    polygon = np.array([[(230, height), (1050, height), (640, 420)]])
    mask = np.zeros_like(image)
    # FILL MASK WITH TRIANGE USING fillpoly(image, shape, color)
    cv2.fillPoly(mask, polygon, 255)
    masked_image = cv2.bitwise_and(image, mask)
    return masked_image






