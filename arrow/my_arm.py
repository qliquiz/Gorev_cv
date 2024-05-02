import cv2
import matplotlib.pyplot as plt

image = cv2.imread("./arrow/my_arm.jpg")
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
hsv = hsv[:, :, 1]
_, thresh = cv2.threshold(hsv, 60, 255, cv2.THRESH_BINARY)
thresh[thresh > 0] = 2
thresh[thresh == 0] = 1
thresh[thresh == 2] = 0
binary = cv2.dilate(thresh, None, iterations=8)

cnts, _ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

finger = cnts[0]

cv2.drawContours(image, cnts, 0, (255, 0, 0), 3)

cv2.namedWindow("Image", cv2.WINDOW_GUI_NORMAL)
plt.imshow(binary)
plt.show()
cv2.imshow("Image", image)
cv2.waitKey(0)