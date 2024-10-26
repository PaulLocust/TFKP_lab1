import time

import numpy as np
import matplotlib.pyplot as plt

# Параметры изображения
width, height = 800, 800
samples = 1000000  # Число случайных точек для генерации Буддаброта

# Создаем массив для хранения "посещаемости" точек
budda_image = np.zeros((height, width), dtype=int)


# Масштабирование координат в пределах окна
def scale(value, min_val, max_val, scale_min, scale_max):
    return int((value - min_val) / (max_val - min_val) * (scale_max - scale_min) + scale_min)


# Параметры окна (область видимости фрактала)
x_min, x_max = -2.0, 1.0
y_min, y_max = -1.5, 1.5


# Генерация Буддаброта
def generate_buddhabrot(max_iter):
    print("Starting generation...")
    start_time = time.time()

    for _ in range(samples):
        # Генерируем случайную точку
        zx, zy = np.random.uniform(x_min, x_max), np.random.uniform(y_min, y_max)
        cx, cy = zx, zy
        trajectory = []

        # Проверка, входит ли точка в множество Мандельброта
        for i in range(max_iter):
            zx2, zy2 = zx * zx, zy * zy
            if zx2 + zy2 > 4.0:
                # Если точка "вылетела", добавляем её путь в массив
                for tx, ty in trajectory:
                    x = scale(tx, x_min, x_max, 0, width - 1)
                    y = scale(ty, y_min, y_max, 0, height - 1)
                    if 0 <= x < width and 0 <= y < height:
                        budda_image[y, x] += 1
                break
            trajectory.append((zx, zy))
            zy = 2 * zx * zy + cy
            zx = zx2 - zy2 + cx

    end_time = time.time()
    final_time = end_time - start_time
    print("Generation done! Время выполнения: " + str(final_time) + "c\n")


# Визуализация Буддаброта
def show_buddhabrot(max_iter):
    generate_buddhabrot(max_iter)
    plt.imshow(np.log(budda_image + 1), cmap="hot", extent=(x_min, x_max, y_min, y_max))
    plt.colorbar(label='Итерации')
    plt.title(f"Буддаброт, {max_iter} итераций")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.show()