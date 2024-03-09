labeled = label(erosion(data))
count = 0
for label in range(1, labeled.max() + 1):
    plt.figure()
    plt.imshow(labeled == label)
    count += 1
print('Всего проводов', count)
plt.show()