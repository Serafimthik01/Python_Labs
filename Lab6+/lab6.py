LAB_SOURCE_FILE = __file__

import math


def num_eights(x):
    """Возвращает количество восьмёрок в записи числа x.
    # >>> num_eights(3)
    # 0
    # >>> num_eights(8)
    # 1
    # >>> num_eights(88888888)
    # 8
    # >>> num_eights(2638)
    # 1
    # >>> num_eights(86380)
    # 2
    # >>> num_eights(12345)
    # 0
    # >>> from construct_check import check
    # >>> # в этом задании запрещено использовать оператор связывания
    # >>> # используйте только рекурсию
    # >>> check(LAB_SOURCE_FILE, 'num_eights',
    # ...       ['Assign', 'AugAssign'])
    True
    """
    if not x:
        return 0
    elif x % 10 == 8:
        return num_eights(x // 10) + 1
    return num_eights(x // 10)


def pingpong(n):
    """Возвращает n-ый элемент пинг-понг последовательности.

    Пинг-понг последовательность начинается с 1.
    Следующий элемент получается прибавлением приращения к предыдущему.
    Начальное приращение: +1.
    Если номер элемента кратен 8 или содержит цифру 8 - знак приращения меняется (обозначено *):

    Номер   1	2	3	4	5	6	7	8*	9	10	11	12	13	14	15	16*	17	18*	19	20	21 ...

    Элемент 1	2	3	4	5	6	7	8*	7	 6	 5	 4	 3	 2	 1	 0*	 1	 2*	 1	 0	-1 ...

    # >>> pingpong(8)
    # 8
    # >>> pingpong(10)
    # 6
    # >>> pingpong(15)
    # 1
    # >>> pingpong(21)
    # -1
    # >>> pingpong(22)
    # -2
    # >>> pingpong(30)
    # -2
    # >>> pingpong(68)
    # 0
    # >>> pingpong(69)
    # -1
    # >>> pingpong(80)
    # 0
    # >>> pingpong(81)
    # 1
    # >>> pingpong(82)
    # 0
    # >>> pingpong(100)
    # -6
    # >>> from construct_check import check
    # >>> # в этом задании запрещено использовать оператор связывания
    # >>> # используйте только рекурсию
    # >>> check(LAB_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """

    def helper(i, adder, ans):
        if i == n + 1:
            return ans
        if (i - 1) % 8 == 0 or num_eights(i - 1) != 0:
            return helper(i + 1, adder * (-1), ans + adder * (-1))
    return helper(1, -1, 0)


def missing_digits(n):
    """Функция принимает число n, цифры которого стоят в порядке возрастания
    и возвращает количество пропущенных цифр в этом числе.
    # >>> missing_digits(1248) # пропущены 3, 5, 6, 7
    # 4
    # >>> missing_digits(1122) # нет пропущенных
    # 0
    # >>> missing_digits(123456) # нет пропущенных
    # 0
    # >>> missing_digits(3558) # пропущены 4, 6, 7
    # 3
    # >>> missing_digits(35578) # пропущены 4, 6
    # 2
    # >>> missing_digits(12456) # пропущена 3
    # 1
    # >>> missing_digits(16789) # пропущены 2, 3, 4, 5
    # 4
    # >>> missing_digits(19) # пропущены 2, 3, 4, 5, 6, 7, 8
    # 7
    # >>> missing_digits(4) # между 4 и 4 нет пропущенных
    # 0
    # >>> from construct_check import check
    # >>> # нельзя использовать циклы
    # >>> check(LAB_SOURCE_FILE, 'missing_digits', ['While', 'For'])
    True
    """
    if n // 10 == 0:
        return 0
    if n // 100 == 0:
        if n % 10 == n // 10:
            return n % 10 - n // 10
    return missing_digits(n // 10) + missing_digits(n % 100)


def next_largest_coin(coin):
    """Возвращает следующую монету.
    # >>> next_largest_coin(1)
    # 5
    # >>> next_largest_coin(5)
    # 10
    # >>> next_largest_coin(10)
    # 25
    # >>> next_largest_coin(2) # остальные возвращают None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    """Возвращает кол-во вариантов размена total используя монеты по 1, 5, 10, 25 коп.

    Например 15 коп. можно разменять так:
    - 15 монет по 1 коп.
    - 10 монет по 1 коп. + 1 монета 5 коп.
    - 5 монет по 1 коп. + 2 по 5 коп.
    - 5 монет по 1 коп. + 1 по 10 коп.
    - 3 монеты по 5 коп.
    - 1 монета 5 коп. + 1 монета 10 коп.
    Итого 6 вариантов.

    # >>> count_coins(15)
    # 6
    # >>> count_coins(10)
    # 4
    # >>> count_coins(20)
    # 9
    # >>> count_coins(100) # как можно разменять рубль (100 копеек)?
    # 242
    # >>> from construct_check import check
    # >>> # нельзя использовать циклы
    # >>> check(LAB_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    def count(coin, n):
        if not coin:
            return 0
        elif coin == n:
            return 1
        elif coin > n:
            return 0
        with_coin = count(coin, n - coin)
        without_coin = count(next_largest_coin(coin), n)
        return with_coin + without_coin
    return count(1, total)

from operator import sub, mul


def make_anonymous_factorial():
    """Возвращает выражение, которое вычисляет факториал.

    # >>> make_anonymous_factorial()(5)
    # 120
    # >>> from construct_check import check
    # >>> # нельзя использовать связывание, рекурсивные вызовы, создавать свои функции
    # >>> check(LAB_SOURCE_FILE, 'make_anonymous_factorial', ['Assign', 'AugAssign', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda f: lambda k: f(f, k))(lambda f, k: k if k == 1 else mul(k, f(f, sub(k, 1))))