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
    image = cv2.imread("a4/a4.jpg")

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (7, 7), 0)
    mask = cv2.Canny(gray, lower, upper)
    cnts, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(image, cnts, -1, (0, 0, 0), 1)

    eps = 0.01 * cv2.arcLength(cnts[0], True)
    approx = cv2.approxPolyDP(cnts[0], eps, True)
    for p in approx:
        cv2.circle(image, tuple(*p), 6, (0, 255, 0), 2)

    shape = np.float32([[640, 0], [0, 0], [0, 640], [640, 877]])
    mask = cv2.getPerspectiveTransform(approx[:, 0, :].astype("float32"), shape)
    paper = cv2.warpPerspective(image, mask, (640, 480))

    cv2.putText(paper, "Hello world", (90, 60), cv2.FONT_HERSHEY_SIMPLEX, 2, (127, 255, 255), 4)

    mask = cv2.getPerspectiveTransform(shape, approx[:, 0, :].astype("float32"))
    text = cv2.warpPerspective(paper, mask, (640, 480))
    text[np.all(text < 150, axis=2)] = image[np.all(text < 150, axis=2)]

    # cv2.imshow("Image", image)
    cv2.imshow("Text", text)

    key = cv2.waitKey(10)
    if key == ord("q"):
        break


cv2.destroyAllWindows()