from math_lib.matrix_snake import make_matrix, print_matrix
from math_lib.factorize import make_factorize


def run_matrix_snake() -> None:
    n = int(input('Введите размер матрицы N: '))
    print_matrix(make_matrix(n))


def run_factorize() -> None:
    n = int(input("Введите целое число для разложения на множители: "))
    print(make_factorize(n))


def main() -> None:
    menu = {
        '1': ('Спиральная матрица N x N', run_matrix_snake),
        '2': ('Разложение числа на простые множители', run_factorize),
        '0': ('Выход', None)
    }

    while True:
        print('\n=== Меню ===')
        for key, (title, _) in menu.items():
            print(f'{key}: {title}')

        choice = input('Выберите пункт меню: ').strip()

        if choice == '0':
            print('До свидания!')
            break

        action = menu.get(choice)

        if action is None:
            print('Такого пункта меню нет')
            continue

        title, func = action
        try:
            print(f'\n--- {title} ---')
            func()
            print()
        except ValueError as e:
            print(f'Неверный ввод: {e}')


if __name__ == "__main__":
    main()
