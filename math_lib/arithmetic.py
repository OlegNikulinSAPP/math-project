def make_arithmetic(exam: str) -> int:
    """Возвращает результат арифметической операции для целых чисел"""

    exam = exam.replace(' ', '')
    exam = exam.split('+')
    lst_result = []

    for item in exam:
        i = 0
        n = len(item)
        sign = 1

        while i < n:
            if item[i] == '-':
                sign = -1
                i += 1
                continue
            if item[i] == '+':
                sign = 1
                i += 1
                continue

            s = ''
            while i < n and item[i].isdigit():
                s += item[i]
                i += 1

            lst_result.append(sign * int(s))

    return sum(lst_result)


def main():
    exam = input()
    print(make_arithmetic(exam))


if __name__ == "__main__":
    main()
