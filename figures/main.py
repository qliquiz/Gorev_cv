import numpy as np
from skimage.measure import label
import matplotlib.pyplot as plt


data = np.load('figures/ps.npy.txt')

labeled = label(data)

type1 = type2 = type3 = type4 = 0

for label in range(1, labeled.max() + 1):
    sum+=1

print(labeled.max())

plt.imshow(labeled)
plt.show()