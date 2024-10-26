import time

import numpy as np
import matplotlib.pyplot as plt

# Параметры изображения
width, height = 800, 800  # разрешение изображения

# Параметры окна (область видимости фрактала)
x_min, x_max = -2.5, 1.5
y_min, y_max = -2.0, 2.0

# Создание двумерной сетки для отображения фрактала
x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y  # комплексные числа, представляющие каждую точку сетки
C = np.copy(Z)

# Массив для хранения информации об итерациях
mandelbrot_set = np.zeros(Z.shape, dtype=int)


# Алгоритм построения множества Мандельброта
def generate_mandelbrot(max_iter):
    print("Starting generation...")
    start_time = time.time()

    for i in range(max_iter):
        mask = np.abs(Z) <= 2  # фильтр, отсеивающий точки вне множества
        Z[mask] = Z[mask] ** 2 + C[mask]
        mandelbrot_set[mask] = i

    end_time = time.time()
    final_time = end_time - start_time

    print("Generation done! Время выполнения: " + str(final_time) + "c\n")


# Визуализация множества Мандельброта
def show_mandelbrot_set(max_iter):
    generate_mandelbrot(max_iter)
    plt.imshow(mandelbrot_set, cmap='twilight_shifted', extent=(x_min, x_max, y_min, y_max))
    plt.colorbar(label='Итерации')
    plt.title("Множество Мандельброта")
    plt.xlabel("Re(c)")
    plt.ylabel("Im(c)")
    plt.show()
