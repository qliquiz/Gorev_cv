# ping 192.168.0.111
import cv2
import zmq #pip install pyzmq
import numpy as np
import math


cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)
cv2.namedWindow("Mask", cv2.WINDOW_GUI_NORMAL)

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.setsockopt(zmq.SUBSCRIBE, b"")
port = 5055
socket.connect(f"tcp://192.168.0.113:{port}")
n = 0
while True:
    bts = socket.recv()
    n += 1
    arr = np.frombuffer(bts, np.uint8)
    image = cv2.imdecode(arr, cv2.IMREAD_COLOR)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    _,thresh = cv2.threshold(hsv[:,:,1], 70, 255, cv2.THRESH_BINARY)
    distance_map = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
    # distance_map = cv2.normalize(distance_map, None, 0, 1.0, cv2.NORM_MINMAX)
    # ret, dist_thresh = cv2.threshold(distance_map, 0.4, 255, cv2.THRESH_BINARY)
    # ret, markers = cv2.connectedComponents(dist_thresh.astype('uint8'))
    # segments = cv2.watershed(image, markers + 1)
    ret, dist_thresh = cv2.threshold(distance_map, 0.6 * np.max(distance_map), 255, cv2.THRESH_BINARY)
    confuse = cv2.subtract(thresh, dist_thresh.astype('uint8'))
    ret, markers = cv2.connectedComponents(dist_thresh.astype('uint8'))
    markers += 1
    markers[confuse==255] = 0
    segments = cv2.watershed(image, markers)
    cnts, hierarchy = cv2.findContours(segments, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    for i in range(len(cnts)):
        if hierarchy[0][i][3] == -1:
            cv2.drawContours(image, cnts, i, (0, 255, 0), 10)

    circles = 0
    squares = 0

    for c in cnts:
        (curr_x, curr_y), r = cv2.minEnclosingCircle(c)
        area = cv2.contourArea(c)
        circleArea = math.pi * r ** 2
        
        if area <= 6650:
            continue

        if area / circleArea  >= 0.9:
            circles += 1
        else:
            squares += 1

    key = cv2.waitKey(10)
    if key == ord("q"):
        break
    
    cv2.putText(image, f"Circles = {circles}, Squares = {squares}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (127, 255, 255))
    cv2.imshow("Image", image)
    cv2.imshow("Mask", confuse)
    # cv2.imshow("Mask", ((segments / segments.max()) * 255).astype('uint8'))
    # cv2.imshow("Mask", ((markers / markers.max()) * 255).astype('uint8'))

cv2.destroyAllWindows()