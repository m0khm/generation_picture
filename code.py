import random
from PIL import Image

print("Введите размер желаемой картинки")
x = int(input("Ширина: "))
y = int(input("Высота: "))

# Функция генерации случайного списка пикселей
def generate_random_pixels(width, height):
    return [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for _ in range(width * height)]

pixels = generate_random_pixels(x, y)
img = Image.new('RGB', (x, y))
img.putdata(pixels)

img.show()
