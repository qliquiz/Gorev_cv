import cv2
from time import perf_counter
import numpy as np
import matplotlib.pyplot as plt


camera = cv2.VideoCapture(0)

cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)

if not camera.isOpened():
    raise RuntimeError('Camera is not working!')

roi = None

while camera.isOpened():
    ret, image = camera.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    key = cv2.waitKey(10)
    if key == ord('q'):
        break
    if key == ord('f'):
        x, y, w, h = cv2.selectROI('ROI selection', gray)
        roi = gray[y:y+h, x:x+w]
        cv2.imshow('ROI', roi)
        cv2.destroyWindow('ROI selection')
    cv2.imshow("Image", image)

camera.release()
cv2.destroyAllWindows()