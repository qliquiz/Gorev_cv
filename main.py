import matplotlib.pyplot as plt
import numpy as np


""" x = np.arange(-10, 10, 0.2)
a, b, c = 2, 3, 1
y = a + b * x + c

ys = []
for i in range(1, 6):
    ys.append(x ** i)

plt.figure(figsize=(10, 5)) # в дюймах
plt.subplot(121)
plt.plot(x, y, '+r')
plt.subplot(122)
for i, y in enumerate(ys):
    plt.plot(x, y, label='$x^{}$'.format(i + 1))
plt.legend()
plt.show() """

image = np.zeros((50, 50))

image[::2, ::2] = 1
image[1::2, 1::2] = 1
plt.imshow(image)
plt.colorbar()
plt.show()