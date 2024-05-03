''' import cv2
import numpy as np


def result_image_occurrences(video, image):
    # Загрузка изображения и преобразование в grayscale
    image_template = cv2.imread(image, cv2.IMREAD_GRAYSCALE)

    w, h = image_template.shape[::-1]

    # Открытие видеофайла
    cap = cv2.VideoCapture(video)

    # Инициализация счетчика совпадений
    result = 0

    while True:
        # Чтение кадра из видео
        ret, frame = cap.read()
        if not ret:
            break

        # Преобразование кадра в grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Поиск совпадений изображения в кадре
        res = cv2.matchTemplate(gray_frame, image_template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= 0.5)

        # Подсчет совпадений
        result += len(loc[0])

    # Освобождение ресурсов
    cap.release()
    cv2.destroyAllWindows()

    return result

# Пример использования
video = 'pictures/pictures.mp4'
image = 'pictures/my_picture.png'

result = result_image_occurrences(video, image)
print(f'Изображение найдено в {result} кадрах') '''

''' import cv2
import numpy as np

def result_image_occurrences(video, image, threshold=0.5139):
    cap = cv2.VideoCapture(video)
    template = cv2.imread(image, 0)  # grayscale
    w, h = template.shape[::-1]
    result = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)

        loc = np.where(res >= threshold)

        for pt in zip(*loc[::-1]):
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 255), 2)
            result += 1

    cap.release()
    return result

# Пример использования
video = 'pictures/pictures.mp4'
image = 'pictures/my_picture.png'
result = result_image_occurrences(video, image)
print('Количество появлений:', result) '''





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