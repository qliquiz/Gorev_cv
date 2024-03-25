import matplotlib.pyplot as plt
from skimage import draw
import numpy as np
from skimage.filters import threshold_otsu 


def hist(arr):
    result = np.zeros(256)
    for y in range(arr.shape[0]):
        for x in range(arr.shape[1]):
            result[arr[y, x]] += 1
    return result

""" image = np.zeros((1000, 1000), dtype='uint8')
image[:] = np.random.randint(20, 100, size = image.shape)

rr, cc = draw.disk((250, 250), 100)
image[rr, cc] = np.random.randint(80, 120, size=len(rr))

rr, cc = draw.disk((750, 750), 200)
image[rr, cc] = np.random.randint(80, 140, size=len(rr)) """

image = plt.imread('coins.jpg')
image = np.mean(image, 2).astype('uint8')

h = hist(image)

thresh = threshold_otsu(image) * 0.9
print(thresh)

image[image > thresh] = 0
image[image > 0] = 1

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.plot(h)
plt.show()