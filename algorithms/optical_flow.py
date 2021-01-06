import cv2
import numpy as np


def compute_optical_flow(image1, image2):
    prvs = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    hsv = np.zeros_like(image1)
    hsv[..., 1] = 255

    next = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(prvs, next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    mag, ang = cv2.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return rgb
