import mss
import cv2
import numpy as np
import pyautogui
import time


def grab_screen(region=None):
    with mss.mss() as sct:
        monitor = sct.monitors[1]
        if region:
            monitor['top'] = region['top']
            monitor['left'] = region['left']
            monitor['width'] = region['width']
            monitor['height'] = region['height']
        img = np.array(sct.grab(monitor))
        return img[:, :, :3]

def detect_obstacles(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    obstacles = []
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        if w > 10 and h > 10:
            obstacles.append((x, y, w, h))
    return obstacles

def jump():
    pyautogui.press('space')

def duck():
    pyautogui.keyDown('down')
    time.sleep(0.05)
    pyautogui.keyUp('down')

region = {'top': 280, 'left': 600, 'width': 600, 'height': 30}

while True:
    screen = grab_screen(region)
    obstacles = detect_obstacles(screen)
    
    if obstacles:
        obstacle = obstacles[0]
        x, y, w, h = obstacle

        # print(obstacle)
        
        if x < 250 and w != 1200:
            jump()
    
    # cv2.rectangle(np.array(screen), (obstacle[0], obstacle[1]), (obstacle[0] + obstacle[2], obstacle[1] + obstacle[3]), (0, 255, 0), 2)
    # cv2.imshow('screen', screen)
    # if cv2.waitKey(25) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()
    #     break