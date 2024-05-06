import cv2
import numpy as np
import matplotlib.pyplot as plt
import zmq

# camera = cv2.VideoCapture(0 + cv2.CAP_DSHOW)
# camera.set(cv2.CAP_PROP_AUTO_EXPOSURE, 1)
# camera.set(cv2.CAP_PROP_EXPOSURE, -5)

cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow("Mask", cv2.WINDOW_GUI_NORMAL)
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")
port = 5055
socket.connect(f"tcp://192.168.0.113:{port}")

lower = 100
upper = 200


def lower_update(value):
    global lower
    lower = value


def upper_update(value):
    global upper
    upper = value


cv2.createTrackbar("Lower", "Mask", lower, 255, lower_update)
cv2.createTrackbar("Upper", "Mask", upper, 255, upper_update)


while True:
    bts = socket.recv()
    arr = np.frombuffer(bts, np.uint8)
    image = cv2.imdecode(arr, cv2.IMREAD_COLOR)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    mask = cv2.Canny(gray, lower, upper)
    cnts, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, cnts, -1, (0, 0, 0), 1)

    eps = 0.01 * cv2.arcLength(cnts[0], True)
    approx = cv2.approxPolyDP(cnts[0], eps, True)
    for p in approx:
        cv2.circle(image, tuple(*p), 6, (0, 255, 0), 2)
    
    rect = cv2.minAreaRect(cnts[0])
    box = cv2.boxPoints(rect)
    box = np.intp(box)
    cv2.drawContours(image, [box], 0, (0, 255, 0), 2)

    pts_bg = np.float32([[19, 25], [41, 296], [433, 56], [435, 269]])
    boxcont = []
    for i in box:
        boxcont.append(i)
    pts_fg = np.float32([box[0], box[1], box[2], box[3]])

    M = cv2.getPerspectiveTransform(pts_fg, pts_bg)

    cv2.imshow("Image", image)
    # cv2.imshow("Mask", mask)

    key = cv2.waitKey(10)
    if key == ord("q"):
        break
    if key == ord('p'):
        cv2.imwrite('screenshot.jpg', image)

cv2.destroyAllWindows()