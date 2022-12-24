def falling(n, k):
    """Рассчитать убывающий факториал от n глубины k."""

    factorial = 1
    s = 1

    for i in range(-n, 1):
        factorial *= i
        if (s == k):
            break
        else:
            s += 1

    print(abs(factorial))


def sum_digits(y):
    """Сложить все цифры числа y."""

    sum = 0
    while (y != 0):
        sum = sum + y % 10
        y = sum // 10
    return sum


def double_eights(n):
    """Возвращает True если в n есть две цифры 8 подряд."""

    return '88' in str(n)
