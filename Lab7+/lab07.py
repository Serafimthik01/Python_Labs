LAB_SOURCE_FILE = __file__

this_file = __file__


def skip_add(n, sum=0):
    """ Принимает число n и возвращает сумму n + n-2 + n-4 + n-6 + ... + 0.
    True
    """
    if n <= 0:
        return 0
    else:
        return n + skip_add(n - 2)


def summation(n, term):
    """Возвращает сумму первых n элементов в поледовательности, заданной term.
    Реализовать с помощью рекурсии!
    True
    """
    assert n >= 1
    if n == 1:
        return term(n)
    else:
        return summation(n - 1, term) + term(n)


def paths(m, n):
    """Возвращает число путей из нижнего левого угла сетки M x N с координатами (0, 0)
    в верхний правый (M-1, N-1), используя только сдвиги вправо или вверх.

        finish
          v
    ---------
    | > | o |
    ---------
    | * | ^ |
    ---------
      ^
    start
    """
    if m <= 0 or n <= 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return paths(m - 1, n) + paths(m, n - 1)


def max_subseq(n, t):
    """
    Возвращает максимальную по значению подпоследовательность длины в интервале [1, t],
    которую можно составить из цифр числа n, следуя по слева направо, но не обязательно подряд.
    Например, для n = 20125 и t = 3, такими подпоследовательностями будут:
        2
        0
        1
        2
        5
        20
        21
        22
        25
        01
        02
        05
        12
        15
        25
        201
        202
        205
        212
        215
        225
        012
        015с
        025
        125
    из них наибольшим будет число 225.
    """
    if not n or not t:
        return 0
    first = max_subseq(n // 10, t - 1) * 10 + n % 10
    second = max_subseq(n // 10, t)
    return first if first > second else second
