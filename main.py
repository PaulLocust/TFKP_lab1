import sys
from fractals import BuddhaBrot, MandelbrotSet, JuliaSet


def get_max_iter():
    """Запрашивает у пользователя max_iter и проверяет его диапазон."""
    while True:
        try:
            max_iter = int(input("Введите количество итераций: (100 <= x <= 1000) или 0 для выхода\n>> "))
            if max_iter == 0:
                print("Выход из программы.")
                sys.exit(0)
            elif 100 <= max_iter <= 1000:
                return max_iter
            else:
                print("Ошибка: введите число в диапазоне от 100 до 1000.\n")
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное целое число.\n")


while True:
    try:
        # Запрос выбора фрактала
        picked = int(input("Выберите, что визуализировать:"
                           "\n1 - Множество Мандельброта."
                           "\n2 - Множество Жюлиа."
                           "\n3 - Буддаброт."
                           "\n0 - Выход из программы.\n>> "))

        if picked == 0:
            print("Выход из программы.")
            sys.exit(0)

        # Проверка на доступные опции
        if picked not in [1, 2, 3]:
            print("Ошибка: такой опции нет. Попробуйте ещё раз или нажмите 0 для выхода.\n")
            continue

        # Ввод max_iter только для нужных фракталов
        if picked in [1, 2, 3]:
            max_iter = get_max_iter()

        # Выполнение выбранной визуализации
        match picked:
            case 1:
                MandelbrotSet.show_mandelbrot_set(max_iter)
            case 2:
                JuliaSet.show_julia_set(max_iter)
            case 3:
                BuddhaBrot.show_buddhabrot(max_iter)

    except ValueError:
        print("Ошибка: пожалуйста, введите целое число для выбора опции.\n")
