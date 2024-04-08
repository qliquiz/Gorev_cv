import cv2
import os

def detect_pencils(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Невозможно загрузить изображение: {image_path}")
        return -1

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150, apertureSize=3)

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    pencils_count = len(contours)

    return pencils_count

images_dir = './pencils/'

total_pencils = 0
pencils_per_image = {}

for image_name in os.listdir(images_dir):
    image_path = os.path.join(images_dir, image_name)
    pencils_count = detect_pencils(image_path)
    
    if pencils_count != -1:
        pencils_per_image[image_name] = pencils_count
        total_pencils += pencils_count

for image_name, pencils_count in pencils_per_image.items():
    print(f"Количество карандашей на изображении {image_name}: {pencils_count}")

print(f"Общее количество карандашей на всех изображениях: {total_pencils}")