# -*- coding: utf-8 -*-
import cv2
# type: ignore

#cap = cv2.VideoCapture('../videos/highway.mp4')
#car_cascade = cv2.CascadeClassifier('../utils/cars.xml')
upper_left = (20, 380)
bottom_right = (1250, 700)

"""while True:
 # reads frames from a video
 ret, frames = cap.read()
 print(frames)
 #Draw rectangle (region of interest)
 #r = cv2.rectangle(frames, upper_left, bottom_right, (100, 50, 200), 5)
 # frames -> rectangle only
 rect_img = frames[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]
 # convert to gray scale of each frames
 gray = cv2.cvtColor(rect_img, cv2.COLOR_BGR2GRAY)
 # Detects cars of different sizes in the input image
 cars = car_cascade.detectMultiScale(gray, 1.1, 4, minSize=(12,12))
 # To draw a rectangle in each cars
 for (x, y, w, h) in cars:
  cv2.rectangle(rect_img,(x, y),(x + w,y + h),(0, 0, 255), 2)
  font = cv2.FONT_HERSHEY_DUPLEX
  cv2.putText(rect_img, 'Car', (x + 6, y - 6), font, 0.5, (0, 0, 255), 1)
 # Display frames in a window
 cv2.imshow('Car Detection', frames)
 # Wait for Enter key to stop
 if cv2.waitKey(33) == 13:
  break"""


def draw_car_boxes(frames, processed_image):
  rect_img = frames[upper_left[1] : bottom_right[1], upper_left[0] : bottom_right[0]]
  gray = cv2.cvtColor(rect_img, cv2.COLOR_BGR2GRAY)
  car_cascade = cv2.CascadeClassifier('utils/cars.xml')
  cars = car_cascade.detectMultiScale(gray, 1.1, 4, minSize=(12,12))
  
  for (x, y, w, h) in cars:
    cv2.rectangle(processed_image,(x, y),(x + w,y + h),(0, 0, 255), 2)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(processed_image, 'Car', (x + 6, y - 6), font, 0.5, (0, 0, 255), 1)

  return processed_image




