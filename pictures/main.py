import cv2
import numpy as np


image = cv2.imread('pictures/my_picture.png')
video = cv2.VideoCapture('pictures/pictures.mp4')

result = 0

while (video.isOpened()):
    _, frame = video.read()
    if frame is not None:
        image = cv2.resize(image, (frame.shape[1], frame.shape[0]))
    else:
        break

    difference = cv2.absdiff(image, frame)
    coincidence = (np.count_nonzero(difference) * 100) / difference.size

    if coincidence < 50:
        result += 1

print(f'Найдено совпадений: {result}')


video.release()
cv2.destroyAllWindows()