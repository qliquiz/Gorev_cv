import numpy as np
import matplotlib.pyplot as plt
from skimage.measure import label
from scipy.ndimage import morphology


data = np.load("figures/ps.npy.txt")

labeled = label(data)

mask1 = np.array([
        [1,1,1,1],
        [1,1,1,1],
        [1,1,0,0],
        [1,1,0,0],
        [1,1,1,1],
        [1,1,1,1]])

mask2 = np.array([
        [1,1,1,1],
        [1,1,1,1],
        [0,0,1,1],
        [0,0,1,1],
        [1,1,1,1],
        [1,1,1,1]])

mask3 =  np.array([
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1]])

mask4 = np.array([
        [1, 1, 0, 0, 1, 1],
        [1, 1, 0, 0, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]])

mask5 = np.array([
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1]])

erosed1 = morphology.binary_erosion(data, mask1)
dilation = morphology.binary_dilation(erosed1, mask1)
data -= dilation
print(label(dilation).max())

erosed2 = morphology.binary_erosion(data, mask2)
dilation2 = morphology.binary_dilation(erosed2, mask2)
data -= dilation2
print(label(dilation2).max())

erosed3 = morphology.binary_erosion(data, mask3)
dilation3 = morphology.binary_dilation(erosed3, mask3)
data -= dilation3
print(label(dilation3).max())

erosed4 = morphology.binary_erosion(data, mask4)
dilation4 = morphology.binary_dilation(erosed4, mask4)
data -= dilation4
print(label(dilation4).max())

erosed5 = morphology.binary_erosion(data, mask5)
dilation5 = morphology.binary_dilation(erosed5, mask5)
data -= dilation5
print(label(dilation5).max())

plt.title(f"Всего {labeled.max()}")
plt.imshow(labeled)
plt.show()