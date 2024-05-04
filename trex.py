import mss
import cv2
import numpy as np
import pyautogui

def capture_screen(monitor):
    with mss.mss() as sct:
        return np.array(sct.grab(monitor))

def detect_obstacles(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def main():
    monitor = {"top": 400, "left": 400, "width": 600, "height": 150}  # Область захвата экрана

    while True:
        screen = capture_screen(monitor)
        obstacles = detect_obstacles(screen)

        for obstacle in obstacles:
            x, y, w, h = cv2.boundingRect(obstacle)
            if h > 50:  # Если препятствие достаточно высокое, прыгаем
                pyautogui.press('space')
            elif w > 50:  # Если препятствие широкое, пригибаемся
                pyautogui.press('down')

if __name__ == "__main__":
    main()