def primes_up_to_n(n: int) -> list[int]:
    """Возвращает список простых чисел в диапазоне [2; n) по алгоритму Эратосфена"""
    if n <= 2:
        return []
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    p = 2
    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n, p):
                is_prime[i] = False
        p += 1

    return [i for i in range(len(is_prime)) if is_prime[i]]


def main():
    num = int(input('Введите целое положительное число: '))
    print(primes_up_to_n(num))


if __name__ == "__main__":
    main()
