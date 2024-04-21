import cv2
from time import perf_counter
import random
cv2.namedWindow('Image', cv2.WINDOW_GUI_NORMAL)

position = []

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    raise RuntimeError('Camera is not working!')

_, image = camera.read()


colors = {
    'red': {
        'lower': (150, 120, 110),
        'upper': (195, 255, 255),
    },
    'green': {
        'lower': (50, 70, 80),
        'upper': (80, 255, 255),
    },
    'blue': {
        'lower': (89,100,100),
        'upper': (109,255,255),
    },
    'yellow': {
        'lower': (22, 150, 150),
        'upper': (35, 255, 255),
    }
}

rnd = list(colors)
random.shuffle(rnd)

rnd2 = [
    [rnd[0], rnd[1]],
    [rnd[2], rnd[3]]
]

d = 7.37
r = 1

while True:
    _, image = camera.read()

    curr_time = perf_counter()
    blurred =cv2.GaussianBlur(image, (11, 11), 0)

    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    points = []

    for color in colors:
        mask = cv2.inRange(hsv, colors[color]['lower'], colors[color]['upper'])
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.dilate(mask, None, iterations=2)
        key = cv2.waitKey(10)

        cntrs = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
        if len(cntrs) > 0:
            c = max(cntrs, key=cv2.contourArea)
        
            (curr_x, curr_y), r = cv2.minEnclosingCircle(c)

            if r > 10:
                points.append({ 'position': (int(curr_x), int(curr_y)), 'color': color} )
                cv2.circle(image, (int(curr_x), int(curr_y)), int(r), (0, 255, 255), 2)


    cv2.putText(image, f'Нужный порядок: {','.join(rnd)}', 
            (10, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))

    if len(points) == 4:
        points.sort(key=lambda p: p['position'][1])

        points2 = [
            [points[0], points[1]],
            [points[2], points[3]],
        ]

        for p in points2:
            p.sort(key=lambda p: p['position'][0])

        points3 = [points2[0][0], points2[0][1], points2[1][0], points2[1][1]]
        
        cv2.putText(image, f'Порядок: {','.join([i['color'] for i in points3])}', 
                (10, 60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))
    
        correct = True

        for i, p in enumerate(points3):
            if p['color'] != rnd[i]:
                correct = False

        cv2.putText(image, (correct and 'Правильный' or 'Неправильный') + ' порядок', 
                (10, 90), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0))

    if key == ord('q'):
        break

    cv2.imshow('Image', image)


camera.release()
cv2.destroyAllWindows()