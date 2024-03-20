from skimage.morphology import binary_erosion
import matplotlib.pyplot as plt
import numpy as np


struct = np.array([[0, 1, 0], [0, 1, 0], [0, 1, 0]])


def checking(image):
    number = 1
    for y in range(image.shape[0]):
        count = 0
        flag = False
        for x in range(image.shape[1] - 1):
            if image[y, x] != 0 and image[y, x + 1] == 0:
                count += 1
            if image[y, x] != 0 and image[y + 1, x] == 0:
                flag = True
        if flag:
            if count == 0:
                print(f'Провод {number} цел.')
            else:
                print(f'Провод {number} порван на {count + 1} кусков.')
            number += 1


image = np.load('wires/wires5.npy.txt')
checking(binary_erosion(image, struct))
plt.imshow(image)
plt.show()