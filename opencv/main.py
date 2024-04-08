import cv2
import numpy as np
import matplotlib.pyplot as plt


""" arr = np.random.random_sample((1000, 1000))

cv2.namedWindow('Image')
cv2.imshow('Image', arr)

while True:
    key = cv2.waitKey(5)
    if key == ord('w'):
        break

cv2.destroyAllWindows() """

""" mushroom = cv2.imread('./opencv/mushroom.jpg')
logo = cv2.imread('./opencv/cvlogo.png')
logo = cv2.resize(logo, (logo.shape[0] // 2, logo.shape[1] // 2))
# mushroom[:logo.shape[0], :logo.shape[1]] = logo
rows, cols, channels = logo.shape

logo_gray = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(logo_gray, 10, 255, cv2.THRESH_BINARY)

roi = mushroom[:rows, :cols]

bg = cv2.bitwise_and(roi, roi, mask=cv2.bitwise_not(mask))
fg = cv2.bitwise_and(logo, logo, mask=mask)

combined = cv2.add(bg, fg)

mushroom[:rows, :cols] = combined


# cv2.namedWindow('Image', cv2.WINDOW_FULLSCREEN)
cv2.imshow('Image', mushroom)
cv2.waitKey() """

rose = cv2.imread('./opencv/rose.jpg')

hsv = cv2.cvtColor(rose, cv2.COLOR_BGR2HSV)

lower = np.array([0, 150, 50])
upper = np.array([0, 255, 255])

mask = cv2.inRange(hsv, lower, upper)

result = cv2.bitwise_and(rose, rose, mask=mask)

cv2.imshow('Image', result)
cv2.waitKey()
# plt.subplot(131)
# plt.title('Hue')
# plt.imshow(hsv[:,:,0], 'hot')
# plt.subplot(132)
# plt.title('Saturation')
# plt.imshow(hsv[:,:,1], 'hot')
# plt.subplot(133)
# plt.title('Value')
# plt.imshow(hsv[:,:,2], 'hot')
# plt.show()