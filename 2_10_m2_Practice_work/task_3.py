import math


def taylor_sin(x, n):
    """
    Генератор для элементов разложения sin(x) в ряд Тейлора.

    Args:
        x: Значение угла в радианах.
        n: Количество элементов ряда.
    Yields:
        Значения элементов ряда Тейлора для sin(x).
    """
    term = x
    yield term
    for k in range(1, n):
        term *= -x ** 2 / ((2 * k + 1) * (2 * k))
        yield term


def taylor_cos(x, n):
    """
    Генератор для элементов разложения cos(x) в ряд Тейлора.

    Args:
        x: Значение угла в радианах.
        n: Количество элементов ряда.
    Yields:
        Значения элементов ряда Тейлора для cos(x).
    """
    term = 1
    yield term
    for k in range(1, n):
        term *= -x**2 / (2*k * (2*k-1))
        yield term


def taylor_exp(x, n):
    """
    Генератор для элементов разложения exp(x) в ряд Тейлора.

    Args:
        x: Значение угла в радианах.
        n: Количество элементов ряда.
    Yields:
        Значения элементов ряда Тейлора для exp(x).
    """
    term = 1
    yield term
    for k in range(1, n):
        term *= x / k
        yield term


def sum_taylor_series(generator):
    """
    Вычисляет сумму элементов ряда Тейлора, используя генератор.

    Args:
        generator: Генератор, выдающий элементы ряда Тейлора.
    Returns:
        Сумма элементов ряда.
    """
    return sum(generator)



# x = float(input("Введите значение угла в радианах: "))
# n = int(input("Введите количество элементов ряда: "))
x = 1
n = 5

# Sin
sin_taylor = sum_taylor_series(taylor_sin(x, n))
sin_math = math.sin(x)
sin_diff = sin_taylor - sin_math
print(f"Sin(x): Тейлор = {sin_taylor}, math.sin(x) = {sin_math}, Разница = {sin_diff:.1e}")

# Cos
cos_taylor = sum_taylor_series(taylor_cos(x, n))
cos_math = math.cos(x)
cos_diff = cos_taylor - cos_math
print(f"Cos(x): Тейлор = {cos_taylor}, math.cos(x) = {cos_math}, Разница = {cos_diff:.1e}")

# Exp
exp_taylor = sum_taylor_series(taylor_exp(x, n))
exp_math = math.exp(x)
exp_diff = exp_taylor - exp_math
print(f"Exp(x): Тейлор = {exp_taylor}, math.exp(x) = {exp_math}, Разница = {exp_diff:.1e}")