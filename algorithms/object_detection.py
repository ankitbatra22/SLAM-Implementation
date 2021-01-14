import torch
import torchvision
import matplotlib.pyplot as plt

import cv2
from torchvision import transforms
from detecto import core, utils, visualize


def draw_boxes(original_image, new_image):
    model = core.Model()
    labels, boxes, scores = model.predict_top(original_image)
    print(labels, boxes, scores)

    for i, box in enumerate(boxes):
        if scores[i] > 0.6:
            x, y, x_low, y_low = box
            w = x_low - x
            h = y_low - y

            cv2.rectangle(new_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)

    return new_image
