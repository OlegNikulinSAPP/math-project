def make_factorize(n: int) -> list[int]:
    """Возвращает список простых множителей числа"""
    lst_factorize = []
    d = 2

    while d * d <= n:
        while n % d == 0:
            lst_factorize.append(d)
            n //= d
        d += 1

    if n > 1:
        lst_factorize.append(n)

    return lst_factorize


def main():
    n = int(input('Введите целое простое число: '))
    lst_factorize = make_factorize(n)
    print(lst_factorize)


if __name__ == "__main__":
    main()
