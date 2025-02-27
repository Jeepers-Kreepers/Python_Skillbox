import math


def sieve_of_eratosthenes(limit):
    """
    Находит простые числа до заданного предела (используя решето Эратосфена).

    Args:
        limit: Максимальное число для поиска простых чисел.

    Returns:
        Список простых чисел, не превышающих limit.
    """
    if limit < 2:
        return []

    # Создаем список boolean значений, представляющих числа от 0 до limit
    # Изначально помечаем все как простые (True), кроме 0 и 1
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    # print(is_prime)

    # Оптимизация: Перебираем делители только до корня из limit
    for p in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[p]:
            # Отмечаем кратные p как непростые (False), начиная с p*p
            # Оптимизация:  Начинаем с p*p, потому что все меньшие кратные p
            # уже были отмечены предыдущими простыми числами.
            for i in range(p * p, limit + 1, p):
                is_prime[i] = False

    # Собираем простые числа в список
    primes = [p for p in range(2, limit + 1) if is_prime[p]]
    return primes


def print_primes_by_ten(primes):
    """
    Выводит простые числа, разбивая их на десятки.

    Args:
        primes: Список простых чисел.
    """
    print("Простые числа:")
    for i in range(0, len(primes), 4):  # изменяем значение на 4, чтоб числа выводились по одному десятку
        print(", ".join(map(str, primes[i:i + 4])))  # изменяем значение на 4, чтоб числа выводились по одному десятку
        # print(f"") #добавил пустую строку для более красивого вывода


# Основная часть программы
limit = int(input("Введите максимальное число: "))
limit = min(limit, 1000)  # Ограничиваем предел 1000
primes = sieve_of_eratosthenes(limit)
print_primes_by_ten(primes)
