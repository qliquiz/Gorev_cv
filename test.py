import numpy as np
import matplotlib.pyplot as plt
from scipy.datasets import face


""" def discretize(image, nvals):
    mn = image.min()
    mx = image.max()
    levels = np.linspace(mn, mx, nvals)
    for i in range(len(levels) - 1):
        min_level, max_level = levels[i], levels[i + 1]
        image[np.logical_and(image > min_level, image <= max_level)] = i

image = face(gray=True)

plt.subplot(1, 2, 1)
plt.imshow(image)
plt.subplot(1, 2, 2)
discretize(image, 3)
plt.imshow(image)
plt.show() """


""" def block_mean(image, ny = 10, nx = 10):
    y_size = image.shape[0] // ny
    x_size = image.shape[1] // nx
    for y in range(0, image.shape[0], y_size):
        for x in range(0, image.shape[1], x_size):
            image[y:y + y_size, x:x + x_size] = image[y:y + y_size, x:x + x_size].mean()


image = face(gray=True)
block_mean(image, 30, 30)
plt.imshow(image)
plt.show() """


""" def mse(img1, img2):
    return np.sum((img1 - img2) ** 2) / img1.size

def psnr(img1, img2):
    m = mse(img1, img2)
    return 20 * np.log10(img1.max() / m)

original = face(gray=True)
noised = original.copy()

n = 10 ** 6

x = np.random.randint(0, original.shape[1], n)
y = np.random.randint(0, original.shape[0], n)
noised[y, x] = np.random.randint(0, 255, n)

print(psnr(original, original))
print(psnr(original, noised))

plt.subplot(121)
plt.imshow(original, cmap='gray')
plt.subplot(122)
plt.imshow(noised, cmap='gray')
plt.show() """


""" def convolve(image, mask):
    result = image.copy().astype('f4')
    for y in range(1, image.shape[0]-1, 1):
        for x in range(1, image.shape[1]-1, 1):
            sub = image[y-1:y+2, x-1:x+2]
            value = (sub * mask).sum()
            result[y, x] = value
    return result[1:-1, 1:-1]

mask = np.array([[-1, -1, -1], 
                [2, 2, 2],
                [-1, -1, -1]]).transpose()
image = face(gray=True)
convolved = convolve(image, mask)

plt.subplot(121)
plt.imshow(image)
plt.subplot(122)
plt.imshow(convolved)
plt.show() """


exter_masks = np.array([[[0,0], [0, 1]],
                        [[0, 0], [1, 0]],
                        [[0, 1], [0, 0]],
                        [[1, 0], [0, 0]]])

inter_masks = np.abs(exter_masks - 1)

cross_masks = np.array([[[0, 1], [1, 0]],
                        [[1, 0], [0, 1]]])

def match(a, masks):
    for mask in masks:
        if np.all(a == mask):
            return True
    return False

def count_objects(B):
    e = 0
    i = 0
    for y in range(0, B.shape[0] - 1):
        for x in range(0, B.shape[1] - 1):
            sub = B[y:y+2, x:x+2]
            e += match(sub, exter_masks)
            i += match(sub, inter_masks)
            if match(sub, cross_masks):
                e += 2
    return (e - i) / 4

image = np.load('txt/cex2.npy.txt')
print(sum([count_objects(image[:,:,i]) for i in range(image.shape[2])]))
plt.figure()
plt.imshow(image)
plt.figure()
plt.subplot(131)
plt.imshow(image[:,:,0])
plt.subplot(132)
plt.imshow(image[:,:,1])
plt.subplot(133)
plt.imshow(image[:,:,2])
plt.imshow(image)
plt.show()