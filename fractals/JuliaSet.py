import time

import numpy as np
import matplotlib.pyplot as plt

# Параметры изображения
width, height = 800, 800  # разрешение изображения

# Параметры окна (область видимости фрактала)
x_min, x_max = -1.5, 1.5
y_min, y_max = -1.5, 1.5

# Параметр C для множества Жюлиа
c = complex(-0.5251993, 0.5251993)  # задаем значение c


# Создание двумерной сетки для отображения фрактала
x, y = np.linspace(x_min, x_max, width), np.linspace(y_min, y_max, height)
X, Y = np.meshgrid(x, y)
Z = X + 1j * Y  # комплексные числа, представляющие каждую точку сетки

# Массив для хранения информации об итерациях
julia_set = np.zeros(Z.shape, dtype=int)


# Алгоритм построения множества Жюлиа
def generate_julia_set(max_iter):
    print("Starting generation...")
    start_time = time.time()

    for i in range(max_iter):
        mask = np.abs(Z) <= 2  # фильтр, отсеивающий точки вне множества
        Z[mask] = Z[mask]**2 + c
        julia_set[mask] = i

    end_time = time.time()
    final_time = end_time - start_time
    print("Generation done! Время выполнения: " + str(final_time) + "c\n")


# Преобразуем значения для более контрастной визуализации
def show_julia_set(max_iter):
    generate_julia_set(max_iter)
    plt.imshow(np.log(julia_set + 1), cmap='inferno', extent=(x_min, x_max, y_min, y_max))
    plt.colorbar(label='Итерации')
    plt.title(f"Заполненное множество Жюлиа для c = {c} и {max_iter} итераций")
    plt.xlabel("Re(z)")
    plt.ylabel("Im(z)")
    plt.show()